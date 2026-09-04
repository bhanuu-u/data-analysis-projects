import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# -----------------------------------------------------
# Project Paths
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "kohli_stats.csv"

VISUALIZATION_DIR = BASE_DIR / "visualizations"

# Create visualization folder if it doesn't exist
VISUALIZATION_DIR.mkdir(exist_ok=True)


# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

df = pd.read_csv(DATA_FILE)


# -----------------------------------------------------
# Data Cleaning & Transformation
# -----------------------------------------------------

# Extract Runs and Balls Faced separately
df["Balls"] = df["Run"].str.extract(r"\((\d+)\)").astype(int)
df["Run"] = df["Run"].str.extract(r"(\d+)").astype(int)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%y")

# Extract Year
df["Year"] = df["Date"].dt.year

# Extract opponent from Match
df["Opponent"] = df["Match"].str.extract(r"vs ([A-Za-z]+)")


# -----------------------------------------------------
# 1. Kohli's Average Runs Over the Years
# -----------------------------------------------------

avg_runs = df.groupby("Year")["Run"].mean()

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=avg_runs.index,
    y=avg_runs.values,
    hue=avg_runs.index,
    palette="viridis",
    legend=False
)

ax.bar_label(
    ax.containers[0],
    fmt="%.1f",
    padding=3
)

plt.title("Virat Kohli's Average Runs Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Runs")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "average_runs_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 2. Average Runs Against Each Opponent
# -----------------------------------------------------

avg_against_team = (
    df.groupby("Opponent")["Run"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=avg_against_team.index,
    y=avg_against_team.values,
    hue=avg_against_team.index,
    palette="rainbow",
    legend=False
)

ax.bar_label(
    ax.containers[0],
    fmt="%.1f",
    padding=3
)

plt.title("Virat Kohli's Average Runs Against Each Opponent")
plt.xlabel("Opponent")
plt.ylabel("Average Runs")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "average_runs_by_opponent.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 3. Kohli's Scoring Consistency
# -----------------------------------------------------

plt.figure(figsize=(8, 6))

sns.boxenplot(
    y=df["Run"],
    color=None
)

plt.title("Virat Kohli's Scoring Consistency")
plt.ylabel("Runs")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "scoring_consistency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 4. Runs by Dismissal Type
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

sns.boxenplot(
    data=df,
    x="Out",
    y="Run",
    hue="Out",
    palette="muted",
    legend=False
)

plt.title("Virat Kohli's Runs by Dismissal Type")
plt.xlabel("Dismissal Type")
plt.ylabel("Runs")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "runs_by_dismissal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 5. Average Strike Rate Against Each Opponent
# -----------------------------------------------------

avg_sr = (
    df.groupby("Opponent")["SR"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=avg_sr.index,
    y=avg_sr.values,
    hue=avg_sr.index,
    palette="viridis",
    legend=False
)

ax.bar_label(
    ax.containers[0],
    fmt="%.1f",
    padding=3
)

plt.title("Virat Kohli's Average Strike Rate Against Each Opponent")
plt.xlabel("Opponent")
plt.ylabel("Strike Rate")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "strike_rate_by_opponent.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 6. Kohli's ODI Scoring Distribution
# -----------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Run",
    bins=20,
    kde=True
)

plt.title("Virat Kohli's ODI Scoring Distribution")
plt.xlabel("Runs")
plt.ylabel("Number of Innings")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "scoring_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 7. Average Strike Rate Over the Years
# -----------------------------------------------------

avg_sr_year = df.groupby("Year")["SR"].mean()

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=avg_sr_year.index,
    y=avg_sr_year.values,
    marker="o"
)

plt.title("Virat Kohli's Average Strike Rate Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Strike Rate")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "strike_rate_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------------------------
# 8. Balls Faced vs Runs Scored
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

sns.scatterplot(
    data=df,
    x="Balls",
    y="Run",
    hue="Out",
    alpha=0.7
)

plt.title("Virat Kohli: Balls Faced vs Runs Scored")
plt.xlabel("Balls Faced")
plt.ylabel("Runs Scored")
plt.legend(title="Dismissal")

plt.tight_layout()

plt.savefig(
    VISUALIZATION_DIR / "balls_vs_runs.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()