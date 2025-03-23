import os
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_osim_data(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            header_end_line = next(i for i, line in enumerate(lines) if 'endheader' in line)
        df = pd.read_csv(filepath, sep='\t', skiprows=header_end_line + 1)
        return df
    except Exception as e:
        print(f"Error loading osim data: {e}")
        return None

def calculate_impulse(df):
    impulse_dict = {}
    for col in df.columns:
        if 'time' not in col:
            impulse = np.trapz(df[col], x=df['time'])
            impulse_dict[col + '_impulse'] = impulse
    return pd.DataFrame(impulse_dict, index=[0])

def parse_muscle_groups(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        muscle_groups = {}
        for force_set in root.find('.//ForceSet'):
            for group in force_set.findall('ObjectGroup'):
                group_name = group.get('name')
                members = group.find('members').text.split()
                muscle_groups[group_name] = members
        return muscle_groups
    except Exception as e:
        print(f"Error parsing muscle groups: {e}")
        return {}

def process_data(muscle_forces_path, joint_angles_path, muscle_groups_path):
    muscle_forces_df = load_osim_data(muscle_forces_path)
    joint_angles_df = load_osim_data(joint_angles_path)
    impulse_data = calculate_impulse(muscle_forces_df)
    muscle_groups = parse_muscle_groups(muscle_groups_path)

    if muscle_forces_df is None or joint_angles_df is None:
        return None

    data = {
        'muscle_forces': muscle_forces_df.to_dict(orient='list'),
        'joint_angles': joint_angles_df.to_dict(orient='list'),
        'impulse_data': impulse_data.to_dict(orient='list'),
        'muscle_groups': muscle_groups
    }
    return data

def convert_nan_to_none(data):
    if isinstance(data, dict):
        return {k: convert_nan_to_none(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_nan_to_none(v) for v in data]
    elif pd.isna(data):
        return None
    else:
        return data

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    muscle_forces_path = data.get('muscle_forces_path')
    joint_angles_path = data.get('joint_angles_path')
    muscle_groups_path = data.get('muscle_groups_path')

    if not all([muscle_forces_path, joint_angles_path, muscle_groups_path]):
        return jsonify({'error': 'Missing required data'}), 400

    processed_data = process_data(muscle_forces_path, joint_angles_path, muscle_groups_path)
    if processed_data is None:
        return jsonify({'error': 'Error processing data'}), 500

    processed_data = convert_nan_to_none(processed_data)
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
