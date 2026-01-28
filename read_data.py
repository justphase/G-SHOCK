import geopandas as gpd

# 1. Read the file
# Since the script and file are in the SAME folder, we don't need a long path!
print("Loading Jaipur Data...")
data = gpd.read_file("jaipur_issues.gpkg")

# 2. Show me the data
print("\n--- ATTRIBUTE TABLE ---")
print(data[['issue_type', 'geometry']]) 
# (We only print specific columns to keep it clean)

# 3. Prove it's Spatial
print("\n--- COORDINATE SYSTEM ---")
print(data.crs)