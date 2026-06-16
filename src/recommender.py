import pandas as pd
import json


def load_profile():

    with open(
        "data/processed/user_profile.json",
        "r"
    ) as file:

        return json.load(file)


def load_problem_bank():

    return pd.read_csv(
        "data/problem_bank.csv"
    )


def recommend_problems(profile, problems):

    level = profile["level"]

    if level == "Beginner":

        recommended = problems[
            problems["difficulty"] == "Easy"
        ]

    elif level == "Intermediate":

        recommended = problems[
            problems["difficulty"] == "Medium"
        ]

    else:

        recommended = problems[
            problems["difficulty"] == "Hard"
        ]

    return recommended.head(5)


def save_recommendations(df):

    output_path = (
        "data/processed/recommended_problems.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nRecommendations saved to: {output_path}"
    )


def main():

    profile = load_profile()

    problems = load_problem_bank()

    recommendations = recommend_problems(
        profile,
        problems
    )

    print("\n===== RECOMMENDED PROBLEMS =====")

    print(
        recommendations[
            ["title", "difficulty", "topic"]
        ]
    )

    save_recommendations(
        recommendations
    )


if __name__ == "__main__":
    main()