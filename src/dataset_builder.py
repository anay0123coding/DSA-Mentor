import pandas as pd

from scraper import get_leetcode_profile, extract_stats


def build_dataset(usernames):
    dataset = []

    for username in usernames:
        try:
            print(f"Fetching data for {username}...")

            data = get_leetcode_profile(username)
            stats = extract_stats(data)

            row = {
                "username": username,
                "total_solved": stats.get("All", 0),
                "easy_solved": stats.get("Easy", 0),
                "medium_solved": stats.get("Medium", 0),
                "hard_solved": stats.get("Hard", 0)
            }

            dataset.append(row)

        except Exception as e:
            print(f"Error processing {username}: {e}")

    return pd.DataFrame(dataset)


def save_dataset(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")


def main():
    usernames = [
        "leetcode"
    ]

    df = build_dataset(usernames)

    print("\nDataset Preview:")
    print(df)

    save_dataset(
        df,
        "data/processed/leetcode_dataset.csv"
    )


if __name__ == "__main__":
    main()