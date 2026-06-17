import pandas as pd

# ==========================
# Load Files
# ==========================

solved_df = pd.read_csv(
    "data/processed/solved_problems.csv"
)

problem_df = pd.read_csv(
    "data/problem_bank.csv"
)

# ==========================
# Total Problems Per Topic
# ==========================

total_topics = (
    problem_df
    .groupby("topic")
    .size()
    .reset_index(name="TotalProblems")
)

# ==========================
# Solved Problems Per Topic
# ==========================

solved_topics = (
    solved_df[solved_df["solved"] == 1]
    .groupby("topic")
    .size()
    .reset_index(name="Solved")
)

# ==========================
# Merge
# ==========================

topic_df = pd.merge(
    total_topics,
    solved_topics,
    on="topic",
    how="left"
)

topic_df["Solved"] = (
    topic_df["Solved"]
    .fillna(0)
    .astype(int)
)

# ==========================
# Completion Rate
# ==========================

topic_df["CompletionRate"] = (
    topic_df["Solved"]
    / topic_df["TotalProblems"]
)

topic_df["SkillScore"] = (
    topic_df["CompletionRate"] * 100
).round(2)

# ==========================
# Level
# ==========================

def get_level(score):

    if score >= 80:
        return "Strong"

    elif score >= 60:
        return "Medium"

    return "Weak"

topic_df["Level"] = (
    topic_df["SkillScore"]
    .apply(get_level)
)

# ==========================
# Sort Weakest First
# ==========================

topic_df = topic_df.sort_values(
    by="SkillScore"
)

# ==========================
# Save
# ==========================

topic_df.to_csv(
    "data/processed/topic_analysis.csv",
    index=False
)

print(topic_df)