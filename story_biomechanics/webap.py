from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Important for session management

activities = [
    "work", "relax", "friends", "date", "movies",
    "reading", "gaming", "shopping", "travel", "good meal",
    "cleaning", "walking", "yoga", "nothing", "sex",
    "period", "sick", "exercise", "alcohol", "camping",
    "study", "insomnia", "edit/new"
]

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

    return render_template("index.html", activities=activities, selected_activities=session["selected_activities"])

if __name__ == "__main__":
    app.run(debug=True)