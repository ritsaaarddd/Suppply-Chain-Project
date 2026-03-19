import pandas as pd
import numpy as np


def load_data(path):
    return pd.read_csv(path)


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )
    return df


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    text_cols = df.select_dtypes(include="object").columns

    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace("nan", np.nan)

    # Standardize known categorical values
    if "transportation_modes" in df.columns:
        df["transportation_modes"] = (
            df["transportation_modes"]
            .str.strip()
            .str.lower()
            .replace({
                "road": "Road",
                "ro ad": "Road",
                "air": "Air",
                "rail": "Rail",
                "sea": "Sea",
                "road ": "Road",
                "road": "Road",
                "ROad": "Road"
            })
        )

    if "product_type" in df.columns:
        df["product_type"] = df["product_type"].str.lower().str.strip().str.title()

    if "customer_demographics" in df.columns:
        df["customer_demographics"] = df["customer_demographics"].str.strip().str.title()

    if "inspection_results" in df.columns:
        df["inspection_results"] = df["inspection_results"].str.strip().str.title()

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(include="object").columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")

    return df


def fix_data_types(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = [
        "price", "availability", "number_of_products_sold", "revenue_generated",
        "stock_levels", "lead_times", "order_quantities", "shipping_times",
        "shipping_costs", "lead_time", "production_volumes",
        "manufacturing_lead_time", "manufacturing_costs",
        "defect_rates", "costs"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def create_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    if {"stock_levels", "number_of_products_sold"}.issubset(df.columns):
        df["inventory_turnover_ratio"] = df["number_of_products_sold"] / (df["stock_levels"] + 1)

    if {"revenue_generated", "costs"}.issubset(df.columns):
        df["estimated_profit"] = df["revenue_generated"] - df["costs"]

    return df

def drop_unnecessary_columns(df):
    columns_to_drop = ["customer_demographics"]

    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    return df

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_column_names(df)
    df = fix_data_types(df)
    df = remove_duplicates(df)
    df = clean_text_columns(df)
    df = fill_missing_values(df)
    df = drop_unnecessary_columns(df)
    df = format_decimal_places(df)
    df = create_derived_columns(df)
    return df

def format_decimal_places(df):
    decimal_cols = [
        "price",
        "availability",
        "number_of_products_sold",
        "revenue_generated",
        "stock_levels",
        "lead_times",
        "order_quantities",
        "shipping_times",
        "shipping_costs",
        "lead_time",
        "production_volumes",
        "manufacturing_lead_time",
        "manufacturing_cost",
        "costs"  # make sure column name matches your dataset
    ]

    for col in decimal_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].round(2)

    return df