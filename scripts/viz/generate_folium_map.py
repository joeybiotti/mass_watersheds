from pathlib import Path

import folium
import geopandas as gpd


def main():
    overlay_path = Path("data/enriched/watersheds_by_municipality.geojson")

    gdf = gpd.read_file(overlay_path)

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

    output = Path("output/maps/watersheds_map.html")

    m.save(output)

    print(f"Map saved to {output}")


if __name__ == "__main__":
    main()
