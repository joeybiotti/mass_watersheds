.PHONY: all ingest validate overlay enriched test clean

# Run the entire pipeline
all: ingest validate overlay

# Ingestion steps
ingest:
	python scripts/ingestion/ingest_municipal_boundaries.py
	python scripts/ingestion/ingest_watersheds.py

# Validation steps
validate:
	python scripts/validation/validate_municipal_boundaries.py
	python scripts/validation/validate_watersheds.py

# Overlay step
overlay:
	python scripts/overlays/clip_watersheds_to_municipalities.py

# Run main orchestrator
run:
	python main.py

# Run tests
test:
	pytest -q

# Clean generated data
clean:
	rm -rf data/clean/*
	rm -rf data/validated/*
	rm -rf data/enriched/*
