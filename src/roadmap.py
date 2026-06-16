import pandas as pd
import json


def load_profile():
    """
    Load user profile
    """
    with open(
        "data/processed/user_profile.json",
        "r"
    ) as file:
        return json.load(file)


def load_recommendations():
    """
    Load recommended problems
    """
    return pd.read_csv(
        "data/processed/recommended_problems.csv"
    )


def generate_study_plan(profile, recommendations):
    """
    Generate a 3-week study roadmap
    """

    problems = recommendations["title"].tolist()

    study_plan = {
        "username": profile["username"],
        "level": profile["level"],
        "week_1": [],
        "week_2": [],
        "week_3": []
    }

    # Distribute problems across weeks
    for i, problem in enumerate(problems):

        if i % 3 == 0:
            study_plan["week_1"].append(problem)

        elif i % 3 == 1:
            study_plan["week_2"].append(problem)

        else:
            study_plan["week_3"].append(problem)

    return study_plan


def save_study_plan(plan):
    """
    Save roadmap as JSON
    """

    output_path = (
        "data/processed/study_plan.json"
    )

    with open(output_path, "w") as file:
        json.dump(
            plan,
            file,
            indent=4
        )

    print(
        f"\nStudy plan saved to: {output_path}"
    )


def display_plan(plan):
    """
    Display roadmap in terminal
    """

    print("\n========== STUDY ROADMAP ==========")

    print(f"\nUser : {plan['username']}")
    print(f"Level: {plan['level']}")

    print("\nWeek 1")
    print("-" * 20)

    for problem in plan["week_1"]:
        print(f"• {problem}")

    print("\nWeek 2")
    print("-" * 20)

    for problem in plan["week_2"]:
        print(f"• {problem}")

    print("\nWeek 3")
    print("-" * 20)

    for problem in plan["week_3"]:
        print(f"• {problem}")

    print("\n===================================")


def main():

    profile = load_profile()

    recommendations = load_recommendations()

    study_plan = generate_study_plan(
        profile,
        recommendations
    )

    display_plan(study_plan)

    save_study_plan(study_plan)


if __name__ == "__main__":
    main()