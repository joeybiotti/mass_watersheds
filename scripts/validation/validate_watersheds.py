import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def main():
    log.info("Validating watersheds")

    clean_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["watersheds_clean"]
    )

    gdf = gpd.read_file(clean_path)
    log.info("Loaded watersheds for validation")

    # Correct emptiness check
    if gdf.empty:
        log.error("Watersheds dataset is empty")
        return

    # Optional geometry validity check
    if not gdf.geometry.is_valid.all():
        log.error("Some watershed geometries are invalid")
        return

    log.info("Watersheds validation passed")


if __name__ == "__main__":
    main()
