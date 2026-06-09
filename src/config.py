from pathlib import Path

# Project root (works from any subdirectory)
ROOT = Path(__file__).resolve().parent.parent

# Paths
DATA_RAW   = ROOT / "data" / "raw"
DATA_PROC  = ROOT / "data" / "processed"
DATA_SPLIT = ROOT / "data" / "splits"
MODELS_DIR = ROOT / "models"
FIGURES    = ROOT / "reports" / "figures"

# Reproducibility
RANDOM_SEED = 42

# Model config
CV_FOLDS   = 5
TEST_SIZE  = 0.15
VAL_SIZE   = 0.15

TARGET_COL = "SalePrice"