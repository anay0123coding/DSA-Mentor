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
    
    🔜 Rating Prediction (ML)
    """
)

st.sidebar.markdown("---")

st.sidebar.info(
    f"""
    Username: {profile['username']}
    
    Level: {profile['level']}
    
    Skill Score: {profile['skill_score']}
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
        "Level",
        profile["level"]
    )

st.divider()


# ==========================================
# SKILL SCORE PROGRESS
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

st.bar_chart(
    chart_df.set_index("Difficulty")
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
# RECOMMENDATIONS
# ==========================================

st.header("📚 Recommended Problems")

st.dataframe(
    recommendations,
    width="stretch"
)

st.divider()


# ==========================================
# ROADMAP
# ==========================================

st.header("🗺️ Study Roadmap")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Week 1")

    for problem in roadmap["week_1"]:
        st.write(f"✅ {problem}")

with col2:

    st.subheader("Week 2")

    for problem in roadmap["week_2"]:
        st.write(f"✅ {problem}")

with col3:

    st.subheader("Week 3")

    for problem in roadmap["week_3"]:
        st.write(f"✅ {problem}")

st.divider()


# ==========================================
# FUTURE ML SECTION
# ==========================================

st.header("🤖 Future Rating Prediction")

st.info(
    """
    This section will be powered by a Machine Learning model.

    Planned Features:
    
    • Estimated Contest Rating
    
    • Future Rating Projection
    
    • Growth Analysis
    
    • Personalized Improvement Suggestions
    """
)

st.divider()


# ==========================================
# FOOTER
# ==========================================

st.caption(
    "DSA Mentor Platform v1.0 | Built using Python, Pandas and Streamlit"
)