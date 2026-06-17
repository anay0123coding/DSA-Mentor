import pandas as pd
import json

# ==========================
# Load Data
# ==========================

topic_df = pd.read_csv(
    "data/processed/topic_analysis.csv"
)

recommend_df = pd.read_csv(
    "data/processed/recommended_problems.csv"
)

# ==========================
# Weak Topics
# ==========================

weak_topics = (
    topic_df
    .sort_values("SkillScore")
    .head(3)["topic"]
    .tolist()
)

# ==========================
# Build Plan
# ==========================

study_plan = {}

day = 1

for topic in weak_topics:

    topic_problems = recommend_df[
        recommend_df["topic"] == topic
    ]

    for _, row in topic_problems.iterrows():

        study_plan[f"Day {day}"] = {
            "Topic": row["topic"],
            "Problem": row["title"],
            "Difficulty": row["difficulty"]
        }

        day += 1

# ==========================
# Save
# ==========================

with open(
    "data/processed/study_plan_v2.json",
    "w"
) as f:

    json.dump(
        study_plan,
        f,
        indent=4
    )

print(json.dumps(
    study_plan,
    indent=4
))