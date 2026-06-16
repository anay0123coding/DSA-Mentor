import pandas as pd
from datetime import datetime


def load_dataset():

    return pd.read_csv(
        "data/processed/leetcode_dataset.csv"
    )


def append_progress(df):

    row = df.iloc[0]

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "total_solved": row["total_solved"],
        "easy_solved": row["easy_solved"],
        "medium_solved": row["medium_solved"],
        "hard_solved": row["hard_solved"]
    }

    history_path = "data/history/progress.csv"

    history_df = pd.read_csv(history_path)

    # Don't append identical latest entry
    today = new_entry["date"]

    if not history_df.empty:

        # If today's entry already exists
        if today in history_df["date"].values:

            idx = history_df[
                history_df["date"] == today
            ].index[-1]

            history_df.loc[idx] = new_entry

            history_df.to_csv(
                history_path,
                index=False
            )

            print(
                "\nToday's progress updated."
            )

            return

    history_df = pd.concat(
        [history_df, pd.DataFrame([new_entry])],
        ignore_index=True
    )

    history_df.to_csv(
        history_path,
        index=False
    )

    print(
        "\nProgress history updated successfully."
    )


def main():

    dataset = load_dataset()

    append_progress(dataset)


if __name__ == "__main__":
    main()