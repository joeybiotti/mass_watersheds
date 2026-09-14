import logging
import os
from pathlib import Path

import geopandas as gdp

from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def main():
    # Rebuild missing SHX if needed
    os.environ["SHAPE_RESTORE_SHX"] = "Yes"

    shp_path = Path("data/raw/TOWNSSURVEY_POLY.shp")
    output_path = Path("data/clean/municipalities_clean.geojson")

    log.info("Loading municipal shapefile...")
    gdf = gdp.read_file(shp_path)

    # Fix geometry
    gdf = gdf.set_geometry(gdf.geometry.buffer(0))

    # Pick dissolve field
    town_field = "TOWN" if "TOWN" in gdf.columns else "TOWN_ID"

    # Keep only needed columns
    gdf = gdf[[town_field, "geometry"]]

    # Dissolve into single polygon
    gdf = gdf.dissolve(by=town_field).reset_index()

    gdf = gdf.to_crs(4326)

    log.info("Saving cleaned GeoJSON...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(output_path, driver="GeoJSON")

    log.info(f"Saved municipal boundaries to {output_path}.")


if __name__ == "__main__":
    main()
