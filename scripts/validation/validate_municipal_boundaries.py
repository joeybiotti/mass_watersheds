import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def main():
    log.info("Validating municipal boundaries")

    clean_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["municipal_clean"]
    )

    gdf = gpd.read_file(clean_path)
    log.info("Loaded municipal boundaries for validation")

    # Correct emptiness check
    if gdf.empty:
        log.error("Municipal boundaries dataset is empty")
        return

    # Optional: check geometry validity
    if not gdf.geometry.is_valid.all():
        log.error("Some municipal geometries are invalid")
        return

    log.info("Municipal boundaries validation passed")


if __name__ == "__main__":
    main()
