from pathlib import Path

import geopandas as gpd


def fetch_municipal_boundaries():
    return gpd.read_file(Path("data/raw/municipalities.geojson"))
