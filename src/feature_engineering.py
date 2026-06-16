import pandas as pd


def create_features(df):
    feature_df = df.copy()

    # Percentage features
    feature_df["easy_pct"] = (
        feature_df["easy_solved"] / feature_df["total_solved"]
    ) * 100

    feature_df["medium_pct"] = (
        feature_df["medium_solved"] / feature_df["total_solved"]
    ) * 100

    feature_df["hard_pct"] = (
        feature_df["hard_solved"] / feature_df["total_solved"]
    ) * 100

    # Ratio features
    feature_df["medium_easy_ratio"] = (
        feature_df["medium_solved"] /
        feature_df["easy_solved"].replace(0, 1)
    )

    feature_df["hard_easy_ratio"] = (
        feature_df["hard_solved"] /
        feature_df["easy_solved"].replace(0, 1)
    )

    return feature_df


def save_features(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Feature dataset saved to {output_path}")


def main():
    df = pd.read_csv(
        "data/processed/leetcode_dataset.csv"
    )

    feature_df = create_features(df)

    print("\nFeature Dataset Preview:")
    print(feature_df)

    save_features(
        feature_df,
        "data/processed/leetcode_features.csv"
    )


if __name__ == "__main__":
    main()