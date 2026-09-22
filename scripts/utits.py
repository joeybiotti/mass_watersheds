import logging

import geopandas as gpd

log = logging.getLogger(__name__)


def clean_geometries(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Fix invalid geometries using buffer(0) trick."""
    if not gdf.geometry.is_valid.all():
        log.warning("Found invalid geometries, attempting repair.")
        gdf["geometry"] = gdf.geometry.apply(
            lambda x: x.buffer(0) if not x.is_valid() else x
        )

    return gdf
