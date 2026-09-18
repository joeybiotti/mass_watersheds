import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def validate_municipal_boundaries(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Pure validation logic for tests."""
    if gdf.empty:
        raise ValueError("Municipal boundaries are empty")

    if not gdf.geometry.is_valid.all():
        raise ValueError("Invalid geometries in municipal boundaries")

    if "TOWN" not in gdf.columns:
        raise ValueError("Missing TOWN column")

    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        raise ValueError("Municipal boundaries must be in EPSG:4326")

    return gdf


def main():
    log.info("Validating municipal boundaries")

    raw_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["municipal_clean"]
    )

    gdf = gpd.read_file(raw_path)
    validated = validate_municipal_boundaries(gdf)

    log.info(f"Municipal boundaries validated → {len(validated)} features")


if __name__ == "__main__":
    main()
