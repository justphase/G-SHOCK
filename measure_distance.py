import geopandas as gpd

# 1. Load the data
gdf = gpd.read_file("jaipur_issues.gpkg")

# 2. Check what we have
print(f"Loaded {len(gdf)} points.")

# 3. THE CRITICAL STEP: Convert Lat/Lon to Meters
# We switch from EPSG:4326 (World) to EPSG:3857 (Google Maps Meters)
gdf_meters = gdf.to_crs(epsg=3857)

# 4. Measure Distance
# Let's take the first point and the second point in your list
point1 = gdf_meters.geometry.iloc[0]  # First row
point2 = gdf_meters.geometry.iloc[1]  # Second row

distance = point1.distance(point2)

print("\n--- RESULTS ---")
print(f"Distance between Point 1 and Point 2 is: {distance:.2f} meters")