import os
from pathlib import Path

import geopandas as gpd


def ingest_watersheds():
    os.environ["SHAPE_RESTORE_SHX"] = "Yes"

    src = Path("data/raw/watshdp1.shp")
    dst = Path("data/clean/watersheds_clean.geojson")

    print("Loading watershed shapefile...")
    gdf = gpd.read_file(src)

    gdf = gdf.set_geometry(gdf.geometry.buffer(0))

    if gdf.crs and gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    dst.parent.mkdir(parents=True, exist_ok=True)

    print("Saving cleaned watershed GeoJSON...")
    gdf.to_file(dst, driver="GeoJSON")

    print(f"Saved watershed boundaries to {dst}")


if __name__ == "__main__":
    ingest_watersheds()
