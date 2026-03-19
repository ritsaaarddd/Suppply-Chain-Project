import matplotlib.pyplot as plt


def plot_missing_summary(df, output_path):
    missing = df.isnull().sum().sort_values(ascending=False)
    missing = missing[missing > 0]

    plt.figure(figsize=(10, 6))
    missing.plot(kind="bar")
    plt.title("Missing Values per Column")
    plt.xlabel("Columns")
    plt.ylabel("Count of Missing Values")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()