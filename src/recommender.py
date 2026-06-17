import pandas as pd

# ==========================
# Load files
# ==========================

topic_df = pd.read_csv(
    "data/processed/topic_analysis.csv"
)

problem_df = pd.read_csv(
    "data/problem_bank.csv"
)

solved_df = pd.read_csv(
    "data/processed/solved_problems.csv"
)

# ==========================
# Solved titles
# ==========================

solved_titles = set(
    solved_df[
        solved_df["solved"] == 1
    ]["title"]
)

# ==========================
# 3 Weakest Topics
# ==========================

weak_topics = (
    topic_df
    .sort_values("SkillScore")
    .head(3)["topic"]
    .tolist()
)

print("Weakest Topics:")
for topic in weak_topics:
    print("-", topic)

# ==========================
# Recommendations
# ==========================

recommendations = problem_df[
    problem_df["topic"].isin(weak_topics)
]

recommendations = recommendations[
    ~recommendations["title"].isin(solved_titles)
]

recommendations = recommendations[
    ["title", "difficulty", "topic"]
]

recommendations = recommendations.head(5)

# ==========================
# Save
# ==========================

recommendations.to_csv(
    "data/processed/recommended_problems.csv",
    index=False
)

print("\nRecommended Problems:\n")

if recommendations.empty:
    print("No unsolved problems found.")
else:
    print(recommendations)