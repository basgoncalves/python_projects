from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Important for session management

activities = [
    "work", "relax", "friends", "date", "movies",
    "reading", "gaming", "shopping", "travel", "good meal",
    "cleaning", "walking", "yoga", "nothing", "sex",
    "period", "sick", "exercise", "alcohol", "camping",
    "study", "insomnia", "edit/new"
]

def generate_plot(data, time_range):
    """Generates a Plotly bar chart based on the provided data."""

    activity_counts = {}
    for entry in data:
        for activity in entry["activities"]:
            if activity not in activity_counts:
                activity_counts[activity] = 0
            activity_counts[activity] += 1

    activities = list(activity_counts.keys())
    counts = list(activity_counts.values())

    trace = go.Bar(x=activities, y=counts)
    layout = go.Layout(title=f"Activity Summary ({time_range})", xaxis=dict(title="Activity"), yaxis=dict(title="Count"))
    fig = go.Figure(data=[trace], layout=layout)
    plot_div = pyo.plot(fig, output_type='div')
    return plot_div

@app.route("/", methods=["GET", "POST"])
def index():
    if "selected_activities" not in session:
        session["selected_activities"] = []

    if request.method == "POST":
        selected = request.form.getlist("activity")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        session["selected_activities"].append({
            "activities": selected,
            "timestamp": timestamp
        })

        return redirect(url_for("index"))

    # Generate plots for week, month, and year
    now = datetime.now()
    week_ago = now - timedelta(weeks=1)
    month_ago = now - timedelta(days=30)  # Approximate month
    year_ago = now - timedelta(days=365)

    week_data = [entry for entry in session["selected_activities"] if datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S") >= week_ago]
    month_data = [entry for entry in session["selected_activities"] if datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S") >= month_ago]
    year_data = [entry for entry in session["selected_activities"] if datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S") >= year_ago]

    week_plot = generate_plot(week_data, "Week")
    month_plot = generate_plot(month_data, "Month")
    year_plot = generate_plot(year_data, "Year")

    return render_template("index.html", activities=activities, selected_activities=session["selected_activities"], week_plot=week_plot, month_plot=month_plot, year_plot=year_plot)

if __name__ == "__main__":
    app.run(debug=True)