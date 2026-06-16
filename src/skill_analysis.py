import pandas as pd
import json


def load_features(path):
    """
    Load engineered feature dataset
    """
    return pd.read_csv(path)


def calculate_skill_score(row):
    """
    Weighted skill score

    Easy   = 1 point
    Medium = 2 points
    Hard   = 3 points
    """

    score = (
        row["easy_solved"] * 1
        + row["medium_solved"] * 2
        + row["hard_solved"] * 3
    )

    return score


def classify_level(score):
    """
    Convert score into skill level
    """

    if score >= 150:
        return "Advanced"

    elif score >= 75:
        return "Intermediate"

    else:
        return "Beginner"


def find_strengths(row):
    """
    Identify strengths
    """

    strengths = []

    if row["hard_pct"] >= 20:
        strengths.append("Hard Problems")

    if row["medium_pct"] >= 45:
        strengths.append("Medium Problems")

    if row["hard_easy_ratio"] >= 0.8:
        strengths.append("Problem Solving")

    return strengths


def find_weaknesses(row):
    """
    Identify weaknesses
    """

    weaknesses = []

    if row["easy_pct"] > 40:
        weaknesses.append("Too Many Easy Problems")

    if row["hard_pct"] < 15:
        weaknesses.append("Need More Hard Problems")

    if row["total_solved"] < 100:
        weaknesses.append("Need More Practice")

    return weaknesses


def build_profile(df):

    row = df.iloc[0]

    score = int(calculate_skill_score(row))

    profile = {
        "username": str(row["username"]),
        "total_solved": int(row["total_solved"]),
        "skill_score": int(score),
        "level": str(classify_level(score)),
        "strengths": list(find_strengths(row)),
        "weaknesses": list(find_weaknesses(row))
    }

    return profile


def save_profile(profile, path):
    """
    Save profile as JSON
    """

    with open(path, "w") as file:
        json.dump(profile, file, indent=4)

    print(f"\nUser profile saved to: {path}")


def save_report(profile):
    """
    Save profile as CSV
    """

    report_df = pd.DataFrame([profile])

    report_df.to_csv(
        "data/processed/skill_report.csv",
        index=False
    )

    print("Skill report saved to: data/processed/skill_report.csv")


def main():

    print("\nLoading feature dataset...")

    df = load_features(
        "data/processed/leetcode_features.csv"
    )

    profile = build_profile(df)

    print("\n========== USER SKILL PROFILE ==========")
    print(f"Username      : {profile['username']}")
    print(f"Total Solved  : {profile['total_solved']}")
    print(f"Skill Score   : {profile['skill_score']}")
    print(f"Level         : {profile['level']}")
    print(f"Strengths     : {profile['strengths']}")
    print(f"Weaknesses    : {profile['weaknesses']}")
    print("========================================")

    save_profile(
        profile,
        "data/processed/user_profile.json"
    )

    save_report(profile)


if __name__ == "__main__":
    main()