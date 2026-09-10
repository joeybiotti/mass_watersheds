from scripts.ingestion.ingest_municipal_boundaries import main as ingest_municipal
from scripts.ingestion.ingest_watersheds import ingest_watersheds
from scripts.overlays.clip_watersheds_to_municipalities import (
    clip_watersheds_to_municipalities,
)
from scripts.validation.validate_municipal_boundaries import (
    validate_municipal_boundaries,
)
from scripts.validation.validate_watersheds import validate_watershed


def main():
    ingest_municipal()
    ingest_watersheds()
    validate_municipal_boundaries()
    validate_watershed()
    clip_watersheds_to_municipalities()


if __name__ == "__main__":
    main()
