import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import datasets

# Load the world map
world = gpd.read_file(datasets.get_path('naturalearth_lowres'))

# Plot the world map
world.plot(color='lightgrey', edgecolor='black', figsize=(10, 6))

# Customize the plot
plt.title("World Map")
plt.show()

exit()


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
file_path = r"C:\Git\personal\Miriam\trip_planner.xlsx"
df = pd.read_excel(file_path)

# Load a world map (replace with your preferred source)
shapefile_path = r"C:\path\to\naturalearth_lowres.shp"
world = gpd.read_file(shapefile_path)


exit()

# Get city coordinates (you'll need a reliable geocoding service)
# Here's a basic example using geopy, but consider using a paid service for better accuracy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_geocoder")

def get_coordinates(city):
    try:
        location = geolocator.geocode(city)
        return location.latitude, location.longitude
    except:
        return None, None

df['latitude'] = df['location'].apply(lambda x: get_coordinates(x)[0])
df['longitude'] = df['location'].apply(lambda x: get_coordinates(x)[1])

# Filter out cities with missing coordinates
df = df.dropna(subset=['latitude', 'longitude'])

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df['longitude'], df['latitude']))

# Plot the map
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color='lightgrey', edgecolor='black') 

# Plot cities with color-coded circles based on overall rating
gdf.plot(ax=ax, column='overall', legend=True, cmap='viridis', markersize=50, alpha=0.7)

# Customize the plot
plt.title("City Ratings")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
 
# save the plot
import os
current_path = os.path.dirname(__file__)
os.chdir(current_path)
fig.savefig(f"{os.path.dirname(current_path)}/city_ratings.png")