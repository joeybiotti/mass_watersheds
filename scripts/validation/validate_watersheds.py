import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def validate_watersheds(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Pure validation logic for watershed boundaries."""
    if gdf.empty:
        raise ValueError("Watersheds dataset is empty")

    if not gdf.geometry.is_valid.all():
        raise ValueError("Watershed geometries contain invalid shapes")

    if "WATERSHED" not in gdf.columns:
        raise ValueError("Missing required column: WATERSHED")

    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        raise ValueError("Watersheds must use EPSG:4326")

    return gdf


def main():
    log.info("Validating watersheds")

    clean_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["watersheds_clean"]
    )

    gdf = gpd.read_file(clean_path)
    validated = validate_watersheds(gdf)

    log.info(f"Watersheds validated → {len(validated)} features")


if __name__ == "__main__":
    main()
