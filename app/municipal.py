import geopandas as gpd
from pathlib import Path

def fetch_municipal_boundaries():
    return gpd.read_file(Path("data/raw/municipalities.geojson"))
