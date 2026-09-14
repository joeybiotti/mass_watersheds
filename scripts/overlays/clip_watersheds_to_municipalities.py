import logging
from pathlib import Path

import geopandas as gpd

from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def clip_watersheds_to_municipalities():
    muni_path = Path("data/validated/municipalities.geojson")
    ws_path = Path("data/validated/watersheds.geojson")
    dst = Path("data/enriched/watersheds_by_municipality.geojson")

    log.info("Loading validated layers...")
    muni = gpd.read_file(muni_path)
    ws = gpd.read_file(ws_path)

    log.info("Clipping watersheds to municipalities")
    clipped = gpd.overlay(ws, muni, how="intersection")

    clipped = clipped.rename(columns={"TOWN": "municipality", "NAME": "watershed_name"})

    dst.parent.mkdir(parents=True, exist_ok=True)

    log.info("Saving enriched watershed slices...")
    clipped.to_file(dst, driver="GeoJSON")

    log.info(f"Saved watershed slices to {dst}.")


if __name__ == "__main__":
    clip_watersheds_to_municipalities()
