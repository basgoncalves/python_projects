from instaloader import Instaloader
import folium
import os

current_path = os.path.dirname(__file__)

# Change the working directory to the current file's directory
os.chdir(current_path)

# Initialize Instaloader
L = Instaloader()

# Target Instagram username
username = "bas_goncalves" 
password = "picklerick_IG7"

# Login to Instagram
L.login(username, password)

# Get the profile
profile = L.check_profile_id(username)

followers = profile.get_followers()

print(f"Followers: {len(followers)}")
exit()

# Create a map centered around a default location (you can adjust this)
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10) 

for follower in profile.get_followers():
    # Extract location information (if available) 
    # Note: This requires followers to have their location publicly visible in their profile
    try:
        location = follower.biography.split('\n')[-1] 
        # Assuming location is the last line of the biography 
    except:
        location = None 

    if location:
        # Use a geocoding service to get coordinates (replace with your preferred service)
        try:
            from geopy.geocoders import Nominatim 
            geolocator = Nominatim(user_agent="my_geocoder")
            location = geolocator.geocode(location)
            if location:
                latitude = location.latitude
                longitude = location.longitude
                folium.Marker([latitude, longitude], popup=follower.username).add_to(m) 
        except:
            pass # Skip if geocoding fails

# Save the map as an HTML file
current_file_path = os.path.abspath(__file__)
m.save(f"{os.path.dirname(current_file_path)}/followers_map.html")