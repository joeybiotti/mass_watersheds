import logging
from pathlib import Path

import geopandas as gpd

from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def validate_municipal_boundaries():
    src = Path("data/clean/municipalities_clean.geojson")
    dst = Path("data/validated/municipalities.geojson")

    gdf = gpd.read_file(src)

    invalid_before = ~gdf.geometry.is_valid

    gdf.loc[invalid_before, "geometry"] = gdf.loc[invalid_before].buffer(0)

    invalid_after = ~gdf.geometry.is_valid

    log.info(f"Invalid before fix: {invalid_before.sum()}")
    log.info(f"Invalid after fix: {invalid_after.sum()}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(dst, driver="GeoJSON")


if __name__ == "__main__":
    validate_municipal_boundaries()
