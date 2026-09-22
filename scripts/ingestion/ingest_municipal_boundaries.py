import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def fetch_municipal_boundaries(path: str) -> gpd.GeoDataFrame:
    """Pure function for tests — loads municipal boundaries from a path."""
    return gpd.read_file(path)


def clean_geometries(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Fix invalid geometries using buffer(0) trick."""
    if not gdf.geometry.is_valid.all():
        log.warning("Found invalid geometries, attempting repair")
        gdf["geometry"] = gdf.geometry.apply(
            lambda x: x.buffer(0) if not x.is_valid else x
        )
    return gdf


def main():
    log.info("Starting municipal boundary ingestion")

    raw_path = os.path.join(config["data"]["raw_dir"], config["files"]["municipal_raw"])
    clean_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["municipal_clean"]
    )

    gdf = fetch_municipal_boundaries(raw_path)
    log.info(f"Loaded {len(gdf)} municipal boundaries")

    # Fix geometries
    gdf = clean_geometries(gdf)

    # Ensure correct CRS
    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    gdf.to_file(clean_path, driver="GeoJSON")
    log.info(f"Saved cleaned municipal boundaries → {clean_path}")


if __name__ == "__main__":
    main()
