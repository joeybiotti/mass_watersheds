import logging

from scripts.config import load_config
from scripts.ingestion.ingest_municipal_boundaries import (
    main as ingest_municipal_boundaries,
)
from scripts.ingestion.ingest_watersheds import main as ingest_watersheds
from scripts.logging_setup import setup_logging
from scripts.overlays.clip_watersheds_to_municipalities import (
    main as clip_watersheds_to_municipalities,
)
from scripts.validation.validate_municipal_boundaries import (
    main as validate_municipal_boundaries,
)
from scripts.validation.validate_watersheds import main as validate_watersheds

setup_logging()
log = logging.getLogger(__name__)
config = load_config()


def main():
    log.info("Pipeline started")

    log.info("Ingestion: municipal boundaries")
    ingest_municipal_boundaries()

    log.info("Ingestion: watersheds")
    ingest_watersheds()

    log.info("Validation: municipal boundaries")
    validate_municipal_boundaries()

    log.info("Validation: watersheds")
    validate_watersheds()

    log.info("Overlay: clip watersheds to municipalities")
    clip_watersheds_to_municipalities()

    log.info("Pipeline completed")


if __name__ == "__main__":
    main()
