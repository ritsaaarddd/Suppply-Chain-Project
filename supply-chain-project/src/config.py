from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "dirty_supply_chain_inventory_dataset.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_supply_chain_inventory_dataset.csv"
FIGURES_DIR = BASE_DIR / "outputs" / "figures"