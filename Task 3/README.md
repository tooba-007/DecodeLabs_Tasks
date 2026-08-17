# Tech Stack Recommender

A content-based AI recommendation engine that maps a user's raw skills and career interests to the most relevant job roles / tech stacks — built as **Project 3 (AI Recommendation Logic)** of the DecodeLabs Industrial Training Kit.

## Overview

Instead of relying on historical user behavior (collaborative filtering), this project uses **content-based filtering**: it compares the *intrinsic attributes* of the user (their stated skills) directly against the *intrinsic attributes* of each job role (its required skills). This avoids the cold-start problem that collaborative systems face with no interaction history.

The engine follows a classic **Input → Process → Output (IPO)** architecture:

| Stage | What happens |
|---|---|
| **Input** | User provides at least 3 skills/interests |
| **Process** | Skills are converted into weighted numerical vectors (TF-IDF) and compared using Cosine Similarity |
| **Output** | The Top-3 highest-scoring job roles are returned |

## How It Works

1. **Vector Mapping** — Every unique skill across the dataset and the user's input forms a shared vocabulary. Each skill list (job role or user) is represented as a vector in that vocabulary space.
2. **TF-IDF Weighting** — Raw term counts alone treat generic skills (e.g. "Python") the same as rare, specific ones. TF-IDF fixes this:
   - **TF** (Term Frequency) — how prominent a skill is within one profile.
   - **IDF** (Inverse Document Frequency) — penalizes skills that appear across many roles, rewarding distinctive ones.
3. **Cosine Similarity** — Measures the angle between the user's vector and each job role's vector, so the *match quality* is judged by orientation (which skills matter) rather than raw overlap count or list length.
4. **4-Step Ranking Pipeline** — Ingestion → Scoring → Sorting → Filtering, producing a clean Top-N list instead of overwhelming the user with every possible match.

All of the math (TF-IDF and cosine similarity) is implemented **from scratch in pure Python** — no external ML libraries — so the logic stays fully transparent and inspectable.

## Project Structure

```
tech-stack-recommender/
├── tech_stack_recommender.py   # Main recommendation engine + CLI
├── raw_skills.csv              # Dataset: job roles mapped to their required skills
└── README.md
```

## Requirements

- Python 3.7+
- No external dependencies (standard library only: `csv`, `math`, `os`)

## Usage

```bash
python tech_stack_recommender.py
```

You'll be prompted to enter at least 3 comma-separated skills:

```
Your skills: Python, Cloud Computing, Automation
```

Example output:

```
Top matching career paths:
1. Data Engineer      (match score: 0.44)
2. Cloud Architect    (match score: 0.33)
3. DevOps Engineer    (match score: 0.25)
```

## Using It Programmatically

```python
from tech_stack_recommender import load_dataset, get_recommendations

dataset = load_dataset("raw_skills.csv")
results = get_recommendations(["Python", "Machine Learning", "Statistics"], dataset, top_n=3)

for role, score in results:
    print(role, score)
```

## Customizing the Dataset

`raw_skills.csv` can be extended with more job roles or more specific skills — no code changes are required. Format:

```csv
job_role,skills
Data Scientist,"Python,SQL,Machine Learning,Data Analysis,Statistics"
```

## Known Limitation: Cold Start

If a user's input shares **no skills at all** with any job role in the dataset, the cosine similarity score will be `0.0` for every role (there's no shared vocabulary to compare). In production systems this is typically handled with onboarding surveys, trending/popularity fallbacks, or metadata inference — this project focuses on the core content-based matching logic itself.

## Author

Built as part of the DecodeLabs AI Industrial Training program (Batch 2026).
