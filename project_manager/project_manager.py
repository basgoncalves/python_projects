import csv
import random
import os
import csv
import tkinter as tk
import matplotlib.pyplot as plt

def csv_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'projects.csv')

class Project:
    def __init__(self, name, description, current_state, deadline, people_involved):
        self.name = name
        self.description = description
        self.current_state = current_state
        self.deadline = deadline
        self.people_involved = people_involved

    def __str__(self):
        return f"Project: {self.name}, Description: {self.description}, Current State: {self.current_state}, Deadline: {self.deadline}, People Involved: {self.people_involved}"

    def to_csv(self):
        # Check if the file exists
        file_exists = os.path.isfile(csv_path())

        # Open the CSV file in append mode
        with open(csv_path(), 'a', newline='') as file:
            writer = csv.writer(file)

            # Write the header row if the file is empty
            if not file_exists:
                writer.writerow(list(vars(self).keys()))

            # Write the project to the CSV file
            writer.writerow(list(vars(self).values()))

        print(f"Project added to {csv_path()}")

def create_random_projects(filepath, n = 4):
    # Create 4 random projects
    projects = []
    for _ in range(n):
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        description = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        current_state = random.choice(['In progress', 'Completed', 'On hold'])
        deadline = random.randint(2022, 2025)
        people_involved = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        project = Project(name, description, current_state, deadline, people_involved)
        projects.append(project)

    # Write projects to a CSV file
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Description', 'Current State', 'Deadline', 'People Involved'])
        for project in projects:
            writer.writerow([project.name, project.description, project.current_state, project.deadline, project.people_involved])

    print(f"Projects written to {filepath}")

    import matplotlib.pyplot as plt

def create_pie_chart_from_csv(filepath=csv_path()):
    # Read the CSV file
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        names = [row[0] for row in reader]

    # Count the occurrences of each name
    name_counts = {}
    total_names = len(names)
    for name in names:
        name_counts[name] = name_counts.get(name, 0) + 1

    # Create the values for the pie chart (percentage of appearances)
    values = [count/total_names * 100 for count in name_counts.values()]

    # Create the labels for the pie chart
    labels = list(name_counts.keys())

    # Create the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Projects by Name')

    # Display the chart
    plt.show()

def add_project_to_csv(filepath, project):
    # Check if the file exists
    file_exists = os.path.isfile(filepath)

    # Open the CSV file in append mode
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row if the file is empty
        if not file_exists:
            writer.writerow(['Name', 'Description', 'Current State', 'Deadline', 'People Involved'])

        # Write the project to the CSV file
        writer.writerow([project.name, project.description, project.current_state, project.deadline, project.people_involved])

    print(f"Project added to {filepath}")

def create_window(title, geometry='500x500'):
    
    window = tk.Tk()

    # Set the window title
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the window width and height
    window_width = screen_width // 2
    window_height = screen_height // 2

    # Calculate the x and y coordinates for centering the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window size and position
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    return window

def select_folder():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    print("Selected folder:", folder_path)
    return folder_path

def add_button(window, text, command, padx=5, pady=5, x=0, y=0):
    button = tk.Button(window, text=text, command=command)
    button.pack(padx=padx, pady=pady)
    button.place(x=x, y=y)


if __name__ == '__main__':
    #%% start GUI
    window = create_window("cereated by BG27")

    folder_path = add_button(window, 'select folder', select_folder, padx=5, pady=5)
    add_button(window, 'add_project_to_csv', add_project_to_csv, padx=5, pady=15)
    add_button(window, 'pie chart', create_pie_chart_from_csv, padx=5, pady=25)
       
    try:
        window.mainloop()
    except KeyboardInterrupt:
        window.destroy()


# END

Hans = Project('Hans', 'Ass.Prof', 'In progress', 'Open', 'Hans')
Hans.to_csv()

create_pie_chart_from_csv(csv_path())