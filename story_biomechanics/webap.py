from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import os
import json

class ActivityAnalyzerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "fdg"
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.UPLOAD_FOLDER = os.path.join(self.current_dir, 'uploads')
        self.app.config['UPLOAD_FOLDER'] = self.UPLOAD_FOLDER
        os.makedirs(self.UPLOAD_FOLDER, exist_ok=True)
        self.USER_CONFIG_FILE = os.path.join(self.UPLOAD_FOLDER, 'users.json')
        self.setup_routes()

    def load_user_config(self):
        try:
            with open(self.USER_CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error decoding user config JSON.")
            return []

    def save_user_config(self, user_config):
        with open(self.USER_CONFIG_FILE, 'w') as f:
            json.dump(user_config, f, indent=4)

    def load_user_data(self, username):
        user_config = self.load_user_config()
        print(f"Attempting to load data for user: {username}")
        for user in user_config:
            if user['username'] == username:
                filepath = user.get('filepath')
                print(f"  Filepath: {filepath}")
                if filepath and os.path.exists(filepath):
                    try:
                        if filepath.endswith('.csv'):
                            df = pd.read_csv(filepath)
                            print(f"  Successfully loaded CSV from: {filepath}")
                            return df
                        elif filepath.endswith('.json'):
                            with open(filepath, 'r') as f:
                                data = json.load(f)
                            df = self.process_google_maps_json(data)
                            if df is not None:
                                print(f"  Successfully loaded JSON and processed from: {filepath}")
                                return df
                            else:
                                print(f"  Error processing JSON data from: {filepath}")
                                return None
                        else:
                            print(f"Unsupported file type: {filepath}")
                            return None
                    except FileNotFoundError:
                        print(f"  File not found at: {filepath}")
                    except pd.errors.ParserError as e:
                        print(f"  Error parsing CSV at {filepath}: {e}")
                    except json.JSONDecodeError as e:
                        print(f"  Error parsing JSON at {filepath}: {e}")
        print(f"  No data found for {username}")
        return None

    def process_google_maps_json(self, data):
        try:
            segments = data.get("semanticSegments", [])
            records = []
            for segment in segments:
                start_time = segment.get("startTime")
                end_time = segment.get("endTime")
                if "timelinePath" in segment:
                    for point_data in segment["timelinePath"]:
                        point = point_data.get("point")
                        time = point_data.get("time")
                        if point and time:
                            lat, lon = map(float, point.replace("°", "").split(", "))
                            records.append({
                                "start_time": time,
                                "end_time": time,
                                "latitude": lat,
                                "longitude": lon,
                                "activity": "Path Point"
                            })
                elif "visit" in segment:
                    visit = segment["visit"]
                    top_candidate = visit.get("topCandidate")
                    if top_candidate and top_candidate.get("placeLocation") and top_candidate["placeLocation"].get("latLng"):
                        lat, lon = map(float, top_candidate["placeLocation"]["latLng"].replace("°", "").split(", "))
                        records.append({
                            "start_time": start_time,
                            "end_time": end_time,
                            "latitude": lat,
                            "longitude": lon,
                            "activity": "Visit"
                        })
                elif "activity" in segment:
                    activity_data = segment["activity"]
                    start_lat, start_lon = map(float, activity_data["start"]["latLng"].replace("°", "").split(", "))
                    end_lat, end_lon = map(float, activity_data["end"]["latLng"].replace("°", "").split(", "))
                    activity_type = activity_data["topCandidate"]["type"]
                    records.append({
                        "start_time": start_time,
                        "end_time": end_time,
                        "latitude": start_lat,
                        "longitude": start_lon,
                        "activity": activity_type
                    })
            df = pd.DataFrame(records)
            return df if not df.empty else None
        except Exception as e:
            print(f"Error processing Google Maps JSON: {e}")
            return None

    def load_all_user_data(self):
        all_dfs = {}
        user_config = self.load_user_config()
        print(f"User Config: {user_config}")
        for user in user_config:
            username = user['username']
            df = self.load_user_data(username)
            if df is not None:
                all_dfs[username] = df
        print(f"Loaded Dataframes: {all_dfs.keys()}")
        return all_dfs

    def generate_comparison_plot(self, all_dfs, time_range, activity_col):
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

    def generate_joint_kinematics_plot(self, trial_path):
        mot_file = os.path.join(trial_path, "joint_angles.mot")
        if not os.path.exists(mot_file):
            return None

        try:
            df = pd.read_csv(mot_file, sep='\t', skiprows=6)
            time_col = df.columns[0]
            joint_cols = df.columns[1:]

            traces = []
            for col in joint_cols:
                traces.append(go.Scatter(x=df[time_col], y=df[col], mode='lines', name=col))

            layout = go.Layout(
                title="Joint Kinematics",
                xaxis=dict(title="Time"),
                yaxis=dict(title="Joint Angle (degrees)")
            )
            fig = go.Figure(data=traces, layout=layout)
            plot_div = pyo.plot(fig, output_type='div')
            return plot_div

        except Exception as e:
            print(f"Error generating kinematics plot: {e}")
            return None

    def index(self):
        user_config = self.load_user_config()
        csv_files = [f for f in os.listdir(self.UPLOAD_FOLDER) if f.endswith('.csv')]
        available_users = [f.replace('.csv', '') for f in csv_files]
        return render_template('index.html', users=user_config, available_users=available_users)

    def upload(self):
        if request.method == 'POST':
            username = request.form['username']
            file = request.files['file']
            filepath = os.path.join(self.UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            user_config = self.load_user_config()
            user_config.append({'username': username, 'filepath': filepath})
            self.save_user_config(user_config)
            return redirect(url_for('index'))
        return redirect(url_for('index'))

    def analyze(self):
        username = request.args.get('username')
        time_range = request.args.get('time_range')
        activity_col = request.args.get('activity_col')
        all_dfs = self.load_all_user_data()
        plot_div = self.generate_comparison_plot(all_dfs, time_range, activity_col)
        return render_template('analyze.html', plot_div=plot_div, username=username)

    def load_motion_data(self, trial_path):
        joint_angles = os.path.join(trial_path, "joint_angles.csv")
        if not os.path.exists(joint_angles):
            return None

        try:
            df = pd.read_csv(joint_angles)
            time_col = df.columns[0]
            joint_cols = df.columns[1:]
            return df, time_col, joint_cols
        except Exception as e:
            print(f"Error loading motion data: {e}")
            return None, None, None

    def kinematics(self):
        username = request.args.get('username')
        trial_path = request.args.get('trial_path') 
        df, time_col, joint_cols = self.load_motion_data(trial_path)
        if df is not None:
            plot_div = self.generate_joint_kinematics_plot(trial_path)
            return render_template('kinematics.html', plot_div=plot_div, username=username)  # Corrected template name
        else:
            error_message = "Motion data not found."
            return render_template('error.html', error_message=error_message)

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)  # GET allowed
        self.app.add_url_rule('/upload', 'upload', self.upload, methods=['POST'])  # POST allowed
        self.app.add_url_rule('/upload', 'analyze', self.analyze)  # GET allowed
        self.app.add_url_rule('/kinematics', 'kinematics', self.kinematics)  # GET allowed

    def run(self):
        self.app.run(debug=True)
        
if __name__ == '__main__':
    app = ActivityAnalyzerApp()
    app.run()