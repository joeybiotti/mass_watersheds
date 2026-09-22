import logging
import os

import folium
import geopandas as gpd

from scripts.config import load_config
from scripts.logging_setup import setup_logging

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def main():
    log.info("Starting map generation")

    overlay_path = os.path.join(
        config["data"]["enriched_dir"],
        config["files"]["enriched_overlay"],
    )

    if not os.path.exists(overlay_path):
        raise FileNotFoundError(f"GeoJSON not found: {overlay_path}")

    gdf = gpd.read_file(overlay_path)

    if gdf.empty:
        raise ValueError("GeoJSON is empty")

    if gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    center = [
        gdf.geometry.centroid.y.mean(),
        gdf.geometry.centroid.x.mean(),
    ]

    m = folium.Map(location=center, zoom_start=8, tiles="CartoDB positron")

    folium.GeoJson(
        gdf,
        name="Watersheds by Municipality",
        style_function=lambda _: {
            "fillColor": "#3186cc",
            "color": "#000000",
            "weight": 1,
            "fillOpacity": 0.4,
        },
    ).add_to(m)

    folium.LayerControl().add_to(m)

    output_dir = "output/maps"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "watersheds_map.html")
    m.save(output_path)

    log.info(f"Map saved to {output_path}")


if __name__ == "__main__":
    main()
