import streamlit as st
import pandas as pd
import json


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="DSA Mentor Platform",
    page_icon="🚀",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

with open(
    "data/processed/user_profile.json",
    "r"
) as file:
    profile = json.load(file)

recommendations = pd.read_csv(
    "data/processed/recommended_problems.csv"
)

with open(
    "data/processed/study_plan.json",
    "r"
) as file:
    roadmap = json.load(file)

features = pd.read_csv(
    "data/processed/leetcode_features.csv"
)

history = pd.read_csv(
    "data/history/progress.csv"
)

try:
    with open(
        "data/processed/readiness_report.json",
        "r"
    ) as file:
        readiness = json.load(file)

except FileNotFoundError:

    readiness = {
        "readiness_score": 0,
        "level": "Unavailable"
    }


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚀 DSA Mentor")

st.sidebar.success("System Status: Active")

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### Features

    ✅ Skill Analysis

    ✅ Problem Recommendations

    ✅ Study Roadmap

    ✅ Progress Tracking

    ✅ Interview Readiness Predictor
    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    f"""
    Username: {profile['username']}

    Level: {profile['level']}

    Skill Score: {profile['skill_score']}

    Readiness: {round(readiness['readiness_score'], 2)}
    """
)


# ==========================================
# TITLE
# ==========================================

st.title("🚀 DSA Mentor Platform")

st.caption(
    "Personalized DSA Analysis, Recommendations and Study Planning"
)

st.divider()


# ==========================================
# USER SUMMARY
# ==========================================

st.header("📊 User Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Username",
        profile["username"]
    )

with col2:
    st.metric(
        "Solved",
        profile["total_solved"]
    )

with col3:
    st.metric(
        "Skill Score",
        profile["skill_score"]
    )

with col4:
    st.metric(
        "Readiness",
        f"{round(readiness['readiness_score'], 2)}/100"
    )

st.divider()

# ==========================================
# INTERVIEW READINESS
# ==========================================

st.header("🤖 Interview Readiness")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Readiness Score",
        f"{round(readiness['readiness_score'], 2)}/100"
    )

with col2:

    st.metric(
        "Current Status",
        readiness["level"]
    )

score = readiness["readiness_score"]

st.progress(score / 100)

st.write(
    f"Interview Readiness: **{round(score, 2)}/100**"
)

if score >= 80:

    st.success(
        "Excellent! You are ready for most coding interviews."
    )

elif score >= 60:

    st.info(
        "You are close to interview-ready. Continue solving medium and hard problems."
    )

elif score >= 40:

    st.warning(
        "More practice is recommended before attempting major interviews."
    )

else:

    st.error(
        "Focus on strengthening your DSA fundamentals and solving more problems."
    )

st.divider()

# ==========================================
# SKILL PROGRESS
# ==========================================

st.header("🎯 Skill Progress")

progress_value = min(
    profile["skill_score"] / 150,
    1.0
)

st.progress(progress_value)

st.write(
    f"Current Skill Score: **{profile['skill_score']} / 150**"
)

st.divider()


# ==========================================
# DIFFICULTY DISTRIBUTION
# ==========================================

st.header("📈 Problem Difficulty Distribution")

chart_df = pd.DataFrame(
    {
        "Difficulty": [
            "Easy",
            "Medium",
            "Hard"
        ],
        "Solved": [
            features["easy_solved"][0],
            features["medium_solved"][0],
            features["hard_solved"][0]
        ]
    }
)

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(
        chart_df.set_index("Difficulty")
    )

with col2:
    st.dataframe(
        chart_df,
        width="stretch"
    )

st.divider()

# ==========================================
# STRENGTHS
# ==========================================

st.header("💪 Strengths")

for strength in profile["strengths"]:
    st.success(strength)

st.divider()


# ==========================================
# WEAKNESSES
# ==========================================

st.header("⚠️ Weaknesses")

for weakness in profile["weaknesses"]:
    st.warning(weakness)

st.divider()

# ==========================================
# TOPIC ANALYSIS
# ==========================================

topic_df = pd.read_csv(
    "data/processed/topic_analysis.csv"
)

st.header("📊 Topic Analysis")

st.dataframe(
    topic_df,
    width="stretch"
)

st.divider()

# ==========================================
# TOPIC SKILL SCORES
# ==========================================

st.header("🎯 Topic Skill Scores")

st.bar_chart(
    topic_df.set_index("topic")["SkillScore"]
)

st.divider()
# ==========================================
# RECOMMENDED PROBLEMS
# ==========================================

st.header("📚 Recommended Problems")

st.dataframe(
    recommendations,
    width="stretch"
)
st.divider()

with open(
    "data/processed/study_plan_v2.json",
    "r"
) as f:
    plan = json.load(f)

st.header("🗺️ Personalized Study Plan")

for day, details in plan.items():

    st.markdown(
        f"""
        **{day}**

        Topic: {details['Topic']}

        Problem: {details['Problem']}

        Difficulty: {details['Difficulty']}
        """
    )

    
# ==========================================
# PROGRESS OVER TIME
# ==========================================

st.header("📈 Progress Over Time")

if not history.empty:

    history["date"] = pd.to_datetime(
        history["date"]
    )

    chart_data = history[
        ["date", "total_solved"]
    ].set_index("date")

    st.line_chart(chart_data)
    latest = history.iloc[-1]

    st.caption(
        f"Latest Snapshot: {latest['total_solved']} problems solved"
    )

    st.write(
        f"Snapshots Recorded: {len(history)}"
    )

else:

    st.info(
        "No historical progress data available yet."
    )

st.divider()


# ==========================================
# STUDY ROADMAP
# ==========================================

st.header("🗺️ Study Roadmap")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Week 1")

    for problem in roadmap.get("week_1", []):
        st.write(f"✅ {problem}")

with col2:

    st.subheader("Week 2")

    for problem in roadmap.get("week_2", []):
        st.write(f"✅ {problem}")

with col3:

    st.subheader("Week 3")

    for problem in roadmap.get("week_3", []):
        st.write(f"✅ {problem}")

st.divider()





# ==========================================
# MODEL INFORMATION
# ==========================================

st.header("🧠 Model Information")

st.info(
    """
    Model: Random Forest Regressor

    Training Samples: 1000

    Features:
    • Total Solved
    • Easy Solved
    • Medium Solved
    • Hard Solved
    • Strength Score
    • Weakness Score

    Output:
    • Interview Readiness Score (0-100)
    """
)

st.divider()

# ==========================================
# PROJECT STATS
# ==========================================

st.header("📌 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Problems Solved",
        profile["total_solved"]
    )

with col2:
    st.metric(
        "Recommendations",
        len(recommendations)
    )

with col3:
    st.metric(
        "History Records",
        len(history)
    )

with col4:
    st.metric(
        "Readiness Score",
        round(readiness["readiness_score"], 2)
    )

st.divider()




# ==========================================
# FOOTER
# ==========================================

st.caption(
    "DSA Mentor Platform v3.0 | Skill Analysis • Recommendations • Roadmap • Progress Tracking • ML Readiness Prediction"
)