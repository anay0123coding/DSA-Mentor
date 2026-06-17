# 🚀 DSA Mentor Platform

An end-to-end Data Structures & Algorithms (DSA) analytics platform that analyzes a user's LeetCode progress, identifies strengths and weaknesses, recommends problems, generates study roadmaps, tracks growth over time, and predicts interview readiness using Machine Learning.

---

## 📌 Overview

DSA Mentor Platform helps users evaluate their coding interview preparation by transforming LeetCode data into actionable insights.

The platform:

Collects and processes DSA problem-solving data
Performs topic-wise skill analysis
Identifies strengths and weaknesses
Tracks progress over time
Generates adaptive problem recommendations
Creates personalized study plans based on weak topics
Predicts interview readiness using Machine Learning
Visualizes insights through an interactive Streamlit dashboard

---

## ✨ Features

### 🎯 Skill Analysis

* Calculates overall skill score
* Determines user level
* Identifies strengths
* Identifies weaknesses

### 📚 Problem Recommendations

* Recommends practice problems
* Prioritizes improvement areas

### 🗺️ Study Roadmap Generation

* Generates a structured multi-week plan
* Organizes recommended problems into weekly schedules

### 📈 Progress Tracking

* Records historical snapshots
* Tracks growth over time
* Visualizes progress trends

### 🤖 Interview Readiness Prediction

* Uses Machine Learning (Random Forest Regressor)
* Predicts readiness score (0–100)
* Categorizes users into readiness levels

### 🎯 Topic-wise Skill Analysis

- Calculates completion rate for every DSA topic
- Generates topic skill scores
- Identifies strongest and weakest topics
- Provides explainable analytics

### 🔥 Adaptive Recommendation Engine

- Detects weakest topics automatically
- Filters already solved problems
- Recommends unsolved questions
- Prioritizes improvement areas

### 🗺️ Personalized Study Planner

- Builds study plans from weak topics
- Uses adaptive recommendations
- Generates day-wise practice schedules

### 📊 Interactive Dashboard

* User summary
* Skill metrics
* Difficulty distribution
* Progress analytics
* Readiness prediction
* Roadmap visualization

---

## 🏗️ Project Architecture

```text
LeetCode Dataset
        ↓
Feature Engineering
        ↓
Skill Analysis
        ↓
Topic Analysis
        ↓
Adaptive Recommendation Engine
        ↓
Personalized Study Planner
        ↓
Progress Tracker
        ↓
Random Forest Readiness Predictor
        ↓
Streamlit Dashboard
```

---

## 📂 Project Structure

```text
DSA_MENTOR/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── leetcode.json
│   │
│   ├── processed/
│   │   ├── leetcode_dataset.csv
│   │   ├── leetcode_features.csv
│   │   ├── skill_report.csv
│   │   ├── user_profile.json
│   │   ├── recommended_problems.csv
│   │   ├── study_plan.json
│   │   └── readiness_report.json
│   │
│   └── history/
│       └── progress.csv
│
├── src/
│   ├── scraper.py
│   ├── dataset_builder.py
│   ├── feature_engineering.py
│   ├── skill_analysis.py
│   ├── recommender.py
│   ├── roadmap.py
│   ├── progress_tracker.py
│   └── train_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Machine Learning Model

### Model

Random Forest Regressor

### Features Used

* Total Solved
* Easy Solved
* Medium Solved
* Hard Solved
* Strength Score
* Weakness Score

### Output

* Interview Readiness Score (0–100)

### Readiness Levels

| Score Range | Level           |
| ----------- | --------------- |
| 80+         | Interview Ready |
| 60–79       | Almost Ready    |
| 40–59       | Needs Practice  |
| Below 40    | Beginner        |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DSA-Mentor-Platform.git
cd DSA-Mentor-Platform
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Pipeline

Generate datasets:

```bash
python src/dataset_builder.py
```

Generate features:

```bash
python src/feature_engineering.py
```

Run skill analysis:

```bash
python src/skill_analysis.py
```

Generate recommendations:

```bash
python src/recommender.py
```

Generate roadmap:

```bash
python src/roadmap.py
```

Track progress:

```bash
python src/progress_tracker.py
```

Train readiness model:

```bash
python src/train_model.py
```

Launch dashboard:

```bash
streamlit run dashboard/app.py
```

---

## 📊 Sample Output

### User Summary

* Username: leetcode
* Problems Solved: 45
* Skill Score: 89
* Level: Intermediate

### Interview Readiness

```json
{
    "username": "leetcode",
    "readiness_score": 37.93,
    "level": "Beginner"
}
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Requests

---


## 🚀 Future Improvements

- XGBoost-based readiness prediction
- Contest performance analytics
- Real-time LeetCode API integration
- Multi-user support
- User authentication
- Cloud database integration
- Advanced visualization with Plotly
- LLM-powered interview preparation assistant

---
## 🎓 Key Highlights

- Built an end-to-end DSA analytics platform using Python and Machine Learning.
- Developed an adaptive recommendation system based on topic-wise weaknesses.
- Implemented a personalized study planner using recommendation outputs.
- Trained a Random Forest model for interview readiness prediction.
- Created an interactive Streamlit dashboard with real-time analytics.
- Designed a modular data pipeline following software engineering best practices.
- 
## 👨‍💻 Author

Built as a Machine Learning + Data Engineering + Data Visualization project demonstrating:

* Data Collection
* Feature Engineering
* Machine Learning
* Recommendation Systems
* Dashboard Development
* Software Engineering Practices

---

⭐ If you found this project useful, consider giving it a star.
