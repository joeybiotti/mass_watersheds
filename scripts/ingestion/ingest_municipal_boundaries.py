import geopandas as gpd
from pathlib import Path

def main():
    shp_path = Path("data/raw/TOWNSSURVEY_POLY.shp")
    out_path = Path("data/raw/municipalities.geojson")

    print("Loading municipal shapefile...")
    gdf = gpd.read_file(shp_path)

    print("Converting to GeoJSON...")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(out_path, driver="GeoJSON")

    print(f"Saved municipal boundaries to {out_path}")

if __name__ == "__main__":
    main()
