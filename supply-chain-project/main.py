from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH, FIGURES_DIR
from src.cleaning import load_data, clean_dataset
from src.visualize import plot_missing_summary


def main():
    df = load_data(RAW_DATA_PATH)

    print("Original shape:", df.shape)
    print("Original missing values:\n", df.isnull().sum())

    cleaned_df = clean_dataset(df)

    print("Cleaned shape:", cleaned_df.shape)
    print("Cleaned missing values:\n", cleaned_df.isnull().sum())

    cleaned_df.to_csv(PROCESSED_DATA_PATH, index=False)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plot_missing_summary(cleaned_df, FIGURES_DIR / "missing_summary.png")

    print(f"Cleaned dataset saved to: {PROCESSED_DATA_PATH}")
    print("Cleaning complete.")


if __name__ == "__main__":
    main()