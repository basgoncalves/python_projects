import json
import folium

def plot_timeline_data(json_file):
    """
    Loads timeline data from a JSON file and plots points on a map.

    Args:
        json_file (str): Path to the JSON file.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
        return

    # Create a map centered on the first point, or Vienna if no points.
    if data and 'semanticSegments' in data:
        first_point = None
        for segment in data['semanticSegments']:
            if 'timelinePath' in segment and segment['timelinePath']:
                first_point = segment['timelinePath'][0]['point'].split('°, ')
                break
        if first_point:
            # Remove the Â character using strip()
            map_center = [float(first_point[0].replace('Â', '').replace('°', '').strip()), float(first_point[1].replace('Â', '').replace('°', '').strip())]
            
        else:
            #default to Vienna, Austria if no points are found.
            map_center = [48.2082, 16.3738] #Vienna Coordinates
        m = folium.Map(location=map_center, zoom_start=12)

        # Plot points from timelinePath
        for segment in data['semanticSegments']:
            if 'timelinePath' in segment and segment['timelinePath']:
                for point_data in segment['timelinePath']:
                    lat, lon = map(float, point_data['point'].split('°, '))
                    time = point_data['time']
                    folium.Marker(location=[lat, lon], popup=f"Time: {time}").add_to(m)

        # Plot visit location if available.
        for segment in data['semanticSegments']:
            if 'visit' in segment and segment['visit'] and segment['visit']['topCandidate'] and segment['visit']['topCandidate']['placeLocation']:
                lat, lon = map(float, segment['visit']['topCandidate']['placeLocation']['latLng'].split('°, '))
                folium.Marker(location=[lat, lon], popup="Visit Location", icon=folium.Icon(color='red')).add_to(m)

        #Plot trip destinations if available.
        for segment in data['semanticSegments']:
          if 'timelineMemory' in segment and segment['timelineMemory'] and 'trip' in segment['timelineMemory'] and segment['timelineMemory']['trip'] and 'destinations' in segment['timelineMemory']['trip']:
            for destination in segment['timelineMemory']['trip']['destinations']:
              if 'placeId' in destination['identifier']:
                place_id = destination['identifier']['placeId']
                #place id is not enough to get the coordinates. more work is needed here.
                folium.Marker(location=map_center, popup=f"Trip destination place ID: {place_id}", icon=folium.Icon(color='green')).add_to(m) #place holder

        m.save('timeline_map.html')
        print("Map saved to 'timeline_map.html'")
    else:
        print("No valid timeline data found in the JSON file.")

# Example usage:

json_file_path = r'C:\Git\python_projects\story_biomechanics\uploads\google_miriam69.json'
plot_timeline_data(json_file_path)