from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import os
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"

current_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(current_dir, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

USER_CONFIG_FILE = os.path.join(UPLOAD_FOLDER, 'users.json')

def load_user_config():
    try:
        with open(USER_CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding user config JSON.")
        return []

def save_user_config(user_config):
    with open(USER_CONFIG_FILE, 'w') as f:
        json.dump(user_config, f, indent=4)

def load_user_data(username):
    user_config = load_user_config()
    print(f"Attempting to load data for user: {username}")
    for user in user_config:
        if user['username'] == username:
            filepath = user.get('filepath')
            print(f"  Filepath: {filepath}")
            if filepath and os.path.exists(filepath):
                try:
                    df = pd.read_csv(filepath)
                    print(f"  Successfully loaded CSV from: {filepath}")
                    return df
                except FileNotFoundError:
                    print(f"  CSV file not found at: {filepath}")
                except pd.errors.ParserError as e:
                    print(f"  Error parsing CSV at {filepath}: {e}")
    print(f"  No data found for {username}")
    return None

def load_all_user_data():
    all_dfs = {}
    user_config = load_user_config()
    print(f"User Config: {user_config}")
    for user in user_config:
        username = user['username']
        df = load_user_data(username)
        if df is not None:
            all_dfs[username] = df
    print(f"Loaded Dataframes: {all_dfs.keys()}")
    return all_dfs

def generate_comparison_plot(all_dfs, time_range, activity_col):
    all_activity_counts = {}
    for username, df in all_dfs.items():
        activity_counts = {}
        if activity_col in df.columns:
            for activities in df[activity_col]:
                if isinstance(activities, str):
                    for activity in activities.split(" | "):
                        activity = activity.strip()
                        if activity:
                            if activity not in activity_counts:
                                activity_counts[activity] = 0
                            activity_counts[activity] += 1
        all_activity_counts[username] = activity_counts

    traces = []
    all_activities = set()
    for counts in all_activity_counts.values():
        all_activities.update(counts.keys())
    all_activities = sorted(list(all_activities))

    for username, counts in all_activity_counts.items():
        y_values = [counts.get(activity, 0) for activity in all_activities]
        traces.append(go.Bar(name=username, x=all_activities, y=y_values))

    layout = go.Layout(
        title=f"Activity Comparison ({time_range})",
        xaxis=dict(title="Activity"),
        yaxis=dict(title="Count"),
        barmode='group'
    )
    fig = go.Figure(data=traces, layout=layout)
    plot_div = pyo.plot(fig, output_type='div')
    return plot_div

@app.route("/", methods=["GET", "POST"])
def index():
    user_config = load_user_config()
    csv_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
    available_users = [f.replace('.csv', '') for f in csv_files]

    if request.method == "POST":
        selected_users = request.form.getlist('users')
    else:
        selected_users = available_users

    for user in selected_users:
        if not any(u['username'] == user for u in user_config):
            user_config.append({'username': user, 'filepath': os.path.join(UPLOAD_FOLDER, f'{user}.csv')})
            save_user_config(user_config)

    all_dfs = {user: load_user_data(user) for user in selected_users if load_user_data(user) is not None}

    if not all_dfs:
        return render_template("index.html", available_users=available_users, week_plot=None, month_plot=None, year_plot=None)

    now = datetime.now()
    week_ago = now - timedelta(weeks=1)
    month_ago = now - timedelta(days=30)
    year_ago = now - timedelta(days=365)

    for username, df in all_dfs.items():
        if 'start_time' in df.columns:
            df['start_time'] = pd.to_datetime(df['start_time'])
            df['full_date'] = df['start_time']
        elif 'full_date' in df.columns:
            df['full_date'] = pd.to_datetime(df['full_date'])
        else:
            continue

    week_dfs = {username: df[df['full_date'] >= week_ago] for username, df in all_dfs.items() if 'full_date' in df.columns}
    month_dfs = {username: df[df['full_date'] >= month_ago] for username, df in all_dfs.items() if 'full_date' in df.columns}
    year_dfs = {username: df[df['full_date'] >= year_ago] for username, df in all_dfs.items() if 'full_date' in df.columns}

    week_plot = generate_comparison_plot(week_dfs, "Week", "activity")
    month_plot = generate_comparison_plot(month_dfs, "Month", "activity")
    year_plot = generate_comparison_plot(year_dfs, "Year", "activity")

    return render_template(
        "index.html",
        available_users=available_users,
        week_plot=week_plot,
        month_plot=month_plot,
        year_plot=year_plot
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    return redirect(url_for("index"))

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        username = request.form.get('username')
        csv_file = request.files.get('csv_file')
        csv_path = request.form.get('csv_path')

        user_config = load_user_config()
        user_found = False
        for user in user_config:
            if user['username'] == username:
                if csv_file and csv_file.filename.endswith('.csv'):
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
                    csv_file.save(filepath)
                    user['filepath'] = filepath
                elif csv_path:
                    user['filepath'] = csv_path
                user_found = True
                break

        if not user_found:
            user_data = {'username': username}
            if csv_file and csv_file.filename.endswith('.csv'):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
                csv_file.save(filepath)
                user_data['filepath'] = filepath
            elif csv_path:
                user_data['filepath'] = csv_path
            user_config.append(user_data)

        save_user_config(user_config)
        return redirect(url_for("index"))

    user_config = load_user_config()
    return render_template("upload.html", users=user_config)

@app.route("/upload_path", methods=["POST"])
def upload_path():
    csv_path = request.form.get('csv_path')
    if csv_path and os.path.exists(csv_path) and csv_path.endswith('.csv'):
        username = os.path.splitext(os.path.basename(csv_path))[0]
        user_config = load_user_config()
        if not any(u['username'] == username for u in user_config):
            user_config.append({'username': username, 'filepath': csv_path})
            save_user_config(user_config)
    return redirect(url_for("index"))

@app.route("/upload_google", methods=["POST"])
def upload_google():
    google_path = request.form.get('google_path')
    if google_path and os.path.exists(google_path) and google_path.endswith('.json'):
        # Add your logic here to process the Google Maps JSON file
        # and generate the plots.
        # Store the plots in variables like google_week_plot, google_month_plot, google_year_plot
        # For now, we'll just set them to None
        google_week_plot = None
        google_month_plot = None
        google_year_plot = None
        return render_template(
            "index.html",
            available_users=[f.replace('.csv', '') for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')],
            week_plot=None,
            month_plot=None,
            year_plot=None,
            google_week_plot=google_week_plot,
            google_month_plot=google_month_plot,
            google_year_plot=google_year_plot
        )
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)