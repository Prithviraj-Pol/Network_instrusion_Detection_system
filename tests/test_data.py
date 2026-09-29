"""Unit tests for NIDS dataset configuration and integrity."""

import csv
import pytest
from pathlib import Path
from src.utils.config import (
    PROJECT_ROOT,
    DATA_RAW,
    SAMPLE_RAW_CSV,
    CLASS_NAMES,
    TARGET_COLUMN
)
from src.utils.logger import get_logger


def test_directory_structure():
    """Verify that expected project directories exist."""
    assert PROJECT_ROOT.exists()
    assert DATA_RAW.exists()
    assert (PROJECT_ROOT / "src").exists()
    assert (PROJECT_ROOT / "reports").exists()
    assert (PROJECT_ROOT / "models").exists()
    assert (PROJECT_ROOT / "results").exists()


def test_sample_dataset_exists():
    """Verify that the raw sample dataset file is present and non-empty."""
    assert SAMPLE_RAW_CSV.exists(), f"Missing dataset file: {SAMPLE_RAW_CSV}"
    assert SAMPLE_RAW_CSV.stat().st_size > 0, "Dataset file is empty"


def test_dataset_schema_and_distribution():
    """Verify dataset columns, row count, and attack class coverage."""
    with open(SAMPLE_RAW_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        # Verify columns
        assert TARGET_COLUMN in header, f"Expected '{TARGET_COLUMN}' in header"
        assert len(header) >= 78, f"Expected at least 78 columns, found {len(header)}"
        
        label_idx = header.index(TARGET_COLUMN)
        classes_found = set()
        row_count = 0
        
        for row in reader:
            row_count += 1
            classes_found.add(row[label_idx])
            
        # Verify row count and classes
        assert row_count == 56661, f"Expected 56,661 rows, got {row_count}"
        for expected_class in CLASS_NAMES:
            assert expected_class in classes_found, f"Missing class: {expected_class}"


def test_logger():
    """Verify that the logger initializes and logs properly."""
    logger = get_logger("TestLogger")
    assert logger is not None
    logger.info("Test logging message for verification.")
