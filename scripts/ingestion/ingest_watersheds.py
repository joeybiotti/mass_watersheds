import logging
import os
from pathlib import Path

import geopandas as gpd

from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def ingest_watersheds():
    os.environ["SHAPE_RESTORE_SHX"] = "Yes"

    src = Path("data/raw/watshdp1.shp")
    dst = Path("data/clean/watersheds_clean.geojson")

    log.info("Loading watershed shapefile...")
    gdf = gpd.read_file(src)

    gdf = gdf.set_geometry(gdf.geometry.buffer(0))

    if gdf.crs and gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    dst.parent.mkdir(parents=True, exist_ok=True)

    log.info("Saving cleaned watershed GeoJSON...")
    gdf.to_file(dst, driver="GeoJSON")

    log.info(f"Saved watershed boundaries to {dst}")


if __name__ == "__main__":
    ingest_watersheds()
