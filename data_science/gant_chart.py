import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define tasks, start dates, and durations
tasks = ['Task 1', 'Task 2', 'Task 3']
start_dates = [datetime(2023, 10, 1), datetime(2023, 10, 15), datetime(2023, 11, 1)]
durations = [20, 45, 15]  # Durations in days

# Convert start dates to days since epoch (Matplotlib's format)
start_dates = [(date - datetime(1970, 1, 1)).days for date in start_dates]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each task on the Gantt chart
for i, task in enumerate(tasks):
    ax.broken_barh([(start_dates[i], durations[i])], (i, 1), facecolors='tab:blue')

# Set labels for tasks
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks)

# Set labels and title
ax.set_xlabel('Date')
ax.set_title('Gantt Chart Example')

plt.show()
