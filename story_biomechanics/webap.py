from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Important for session management

current_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(current_dir, 'uploads')  # Folder to store uploaded CSV files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist

def load_all_data():
    """Loads data from all CSV files in the upload folder."""
    all_dfs = {}
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            try:
                df = pd.read_csv(filepath)
                username = os.path.splitext(filename)[0]  # Extract username from filename
                all_dfs[username] = df
            except FileNotFoundError:
                pass
    return all_dfs

def generate_comparison_plot(all_dfs, time_range, activity_col):
    """Generates a Plotly bar chart comparing activities from all users."""

    all_activity_counts = {}
    for username, df in all_dfs.items():
        activity_counts = {}
        for activities in df[activity_col]:
            if isinstance(activities, str):
                for activity in activities.split(" | "):
                    if activity not in activity_counts:
                        activity_counts[activity] = 0
                    activity_counts[activity] += 1
        all_activity_counts[username] = activity_counts

    traces = []
    all_activities = set()
    for counts in all_activity_counts.values():
        all_activities.update(counts.keys())

    all_activities = sorted(list(all_activities)) #sort the activities

    for username, counts in all_activity_counts.items():
        y_values = [counts.get(activity, 0) for activity in all_activities]
        traces.append(go.Bar(name=username, x=all_activities, y=y_values))

    layout = go.Layout(
        title=f"Activity Comparison ({time_range})",
        xaxis=dict(title="Activity"),
        yaxis=dict(title="Count"),
        barmode='group'  # Group bars for comparison
    )
    fig = go.Figure(data=traces, layout=layout)
    plot_div = pyo.plot(fig, output_type='div')
    return plot_div

@app.route("/", methods=["GET", "POST"])
def index():
    all_dfs = load_all_data()

    if not all_dfs:
        return "No CSV files found in the uploads folder."

    now = datetime.now()
    week_ago = now - timedelta(weeks=1)
    month_ago = now - timedelta(days=30)
    year_ago = now - timedelta(days=365)

    for username, df in all_dfs.items():
        df['full_date'] = pd.to_datetime(df['full_date'])

    week_dfs = {username: df[df['full_date'] >= week_ago] for username, df in all_dfs.items()}
    month_dfs = {username: df[df['full_date'] >= month_ago] for username, df in all_dfs.items()}
    year_dfs = {username: df[df['full_date'] >= year_ago] for username, df in all_dfs.items()}

    week_plot = generate_comparison_plot(week_dfs, "Week", "activities")
    month_plot = generate_comparison_plot(month_dfs, "Month", "activities")
    year_plot = generate_comparison_plot(year_dfs, "Year", "activities")

    return render_template("index.html", week_plot=week_plot, month_plot=month_plot, year_plot=year_plot)

@app.route("/login", methods=["GET", "POST"])
def login():
    return redirect(url_for("index")) #skip login and go to index

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('file') #get list of uploaded files

        for file in files:
            if file.filename == '':
                continue
            if file and file.filename.endswith('.csv'):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)

        return redirect(url_for("index"))

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)