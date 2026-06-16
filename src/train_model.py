import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"

FEATURES_FILE = PROCESSED_DIR / "leetcode_features.csv"
PROFILE_FILE = PROCESSED_DIR / "user_profile.json"
SKILL_REPORT_FILE = PROCESSED_DIR / "skill_report.csv"
OUTPUT_FILE = PROCESSED_DIR / "readiness_report.json"

# =====================================================
# Generate Synthetic Training Data
# =====================================================

np.random.seed(42)

rows = []

for _ in range(1000):

    total = np.random.randint(20, 600)

    easy = np.random.randint(0, total // 3 + 1)
    medium = np.random.randint(0, total // 2 + 1)

    remaining = max(total - easy - medium, 0)
    hard = remaining

    strength = np.random.uniform(40, 100)
    weakness = np.random.uniform(0, 60)

    readiness_score = (
        total * 0.10 +
        medium * 0.15 +
        hard * 0.20 +
        strength * 0.50 -
        weakness * 0.30
    )

    readiness_score = min(max(readiness_score, 0), 100)

    rows.append([
        total,
        easy,
        medium,
        hard,
        strength,
        weakness,
        readiness_score
    ])

train_df = pd.DataFrame(
    rows,
    columns=[
        "total_solved",
        "easy_solved",
        "medium_solved",
        "hard_solved",
        "strength_score",
        "weakness_score",
        "readiness_score"
    ]
)

# =====================================================
# Train Model
# =====================================================

X = train_df.drop("readiness_score", axis=1)
y = train_df["readiness_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print(f"MAE: {mae:.4f}")

# =====================================================
# Load User Data
# =====================================================

feature_df = pd.read_csv(FEATURES_FILE)
row = feature_df.iloc[0]

profile = json.load(open(PROFILE_FILE))

skill_report = pd.read_csv(SKILL_REPORT_FILE)

strength_score = skill_report["skill_score"].max()
weakness_score = skill_report["skill_score"].min()

# =====================================================
# User Feature Vector
# =====================================================

user_features = pd.DataFrame([{
    "total_solved": row["total_solved"],
    "easy_solved": row["easy_solved"],
    "medium_solved": row["medium_solved"],
    "hard_solved": row["hard_solved"],
    "strength_score": strength_score,
    "weakness_score": weakness_score
}])

# =====================================================
# Predict Readiness
# =====================================================

readiness_score = float(
    model.predict(user_features)[0]
)

# =====================================================
# Readiness Category
# =====================================================

if readiness_score >= 80:
    level = "Interview Ready"

elif readiness_score >= 60:
    level = "Almost Ready"

elif readiness_score >= 40:
    level = "Needs Practice"

else:
    level = "Beginner"

report = {
    "username": profile.get("username", "leetcode"),
    "readiness_score": round(readiness_score, 2),
    "level": level
}

# =====================================================
# Save Report
# =====================================================

with open(OUTPUT_FILE, "w") as f:
    json.dump(report, f, indent=4)

print("\nReadiness Report")
print(json.dumps(report, indent=4))