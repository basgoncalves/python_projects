import json
import os
import pandas as pd
import opensim as osim


def import_data(data_path):
    if not os.path.isfile(data_path):
        print(f"File not found: {data_path}")
        return None
    
    if data_path.endswith('.csv'):
        data = pd.read_csv(data_path)
    elif data_path.endswith('.json'):
        with open(data_path, 'r') as f:
            data = json.load(f)
    elif data_path.endswith('.sto'):
        data = osim.TimeSeriesTableVec3(data_path)
    elif data_path.endswith('.mot'):
        data = osim.TimeSeriesTable(data_path)
    else:
        print(f"Unsupported file format: {data_path}")
    
    
    return data

def load_session_data(session_path):
    settings_file = os.path.join(session_path, "settings.json")
    
    if not os.path.isfile(settings_file):
        print(f"Settings file not found: {settings_file}")
        return None
    
    with open(settings_file, 'r') as f:
        settings = json.load(f)
    
    trials_data = {}
    for trial_name, trial_info in settings["trials"].items():
        trial_path = os.path.join(session_path, trial_name)
        if os.path.isdir(trial_path):
            start_time = trial_info["start_time"]
            end_time = trial_info["end_time"]
            trials_data[trial_name] = {
                "start_time": start_time,
                "end_time": end_time,
                "kinematics": import_data(os.path.join(trial_path, settings["kinematics"])),
                "moments": import_data(os.path.join(trial_path, settings["moments"])),
                "emg": import_data(os.path.join(trial_path, settings["emg"])),
                "muscle_forces": import_data(os.path.join(trial_path, settings["muscle_forces"])),
                "joint_loads": import_data(os.path.join(trial_path, settings["joint_loads"]))
            }
        else:
            trials_data[trial_name] = None
    
    return trials_data

# Example usage
session_path = r'C:\Git\python_projects\story_biomechanics\app2\users\bas68\0102223'
session_data = load_session_data(session_path)
print(session_data)
