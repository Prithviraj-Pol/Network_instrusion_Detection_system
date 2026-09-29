"""Configuration settings and directory paths for the NIDS Machine Learning Project."""

from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW = DATA_DIR / "raw" / "CICIDS2017"
DATA_INTERIM = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / "models"
MODELS_BASELINE = MODELS_DIR / "baseline"
MODELS_TUNED = MODELS_DIR / "tuned"
MODELS_FINAL = MODELS_DIR / "final"

RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_METRICS = RESULTS_DIR / "metrics"
RESULTS_CONFUSION = RESULTS_DIR / "confusion_matrices"
RESULTS_PLOTS = RESULTS_DIR / "plots"
RESULTS_FEATURE_IMPORTANCE = RESULTS_DIR / "feature_importance"
RESULTS_EXPERIMENTS = RESULTS_DIR / "experiments"

REPORTS_DIR = PROJECT_ROOT / "reports"

# Dataset Files
SAMPLE_RAW_CSV = DATA_RAW / "CICIDS2017_sample.csv"
CLEANED_DATA_CSV = DATA_INTERIM / "cleaned_data.csv"
ENCODED_DATA_CSV = DATA_INTERIM / "encoded_data.csv"
BALANCED_DATA_CSV = DATA_INTERIM / "balanced_data.csv"

X_TRAIN_CSV = DATA_PROCESSED / "X_train.csv"
X_TEST_CSV = DATA_PROCESSED / "X_test.csv"
Y_TRAIN_CSV = DATA_PROCESSED / "y_train.csv"
Y_TEST_CSV = DATA_PROCESSED / "y_test.csv"

# Modeling Hyperparameters & Constants
RANDOM_STATE = 42
TEST_SIZE = 0.20
CV_FOLDS = 5
TARGET_COLUMN = "Label"

# Class Label Definitions
CLASS_NAMES = [
    "BENIGN",
    "DoS",
    "PortScan",
    "BruteForce",
    "WebAttack",
    "Bot",
    "Infiltration"
]

LABEL_TO_ID = {name: idx for idx, name in enumerate(CLASS_NAMES)}
ID_TO_LABEL = {idx: name for idx, name in enumerate(CLASS_NAMES)}
