import logging
import os

import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def main():
    log.info("Starting watershed overlay")

    muni_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["municipal_clean"]
    )

    water_path = os.path.join(
        config["data"]["clean_dir"], config["files"]["watersheds_clean"]
    )

    enriched_path = os.path.join(
        config["data"]["enriched_dir"], config["files"]["enriched_overlay"]
    )

    muni = gpd.read_file(muni_path)
    water = gpd.read_file(water_path)

    log.info(f"Municipalities: {len(muni)}, Watersheds: {len(water)}")

    clipped = gpd.overlay(water, muni, how=config["overlay"]["method"])

    log.info(f"Generated {len(clipped)} clipped watershed features")

    clipped.to_file(enriched_path, driver="GeoJSON")
    log.info(f"Saved enriched overlay → {enriched_path}")


if __name__ == "__main__":
    main()
