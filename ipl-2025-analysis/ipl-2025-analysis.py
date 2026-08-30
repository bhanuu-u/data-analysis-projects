import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# IPL 2025 — Analysis & Visualization
# ============================================================

# Load IPL 2025 dataset
df_2025 = pd.read_csv("ipl2025.csv", low_memory=False)

print(f"IPL 2025 matches: {df_2025['match_id'].nunique()}")
print(f"IPL 2025 rows: {len(df_2025)}")


# ============================================================
# 1. Which teams had the most wins?
# ============================================================

match_wins = (
    df_2025.groupby("match_id")["winner"]
    .first()
    .value_counts()
)

plt.figure(figsize=(10, 6))

sns.barplot(
    y=match_wins.index,
    x=match_wins.values,
    palette="rainbow"
)

plt.title("IPL 2025 — Matches Won by Each Team")
plt.xlabel("Number of Wins")
plt.ylabel("Team")

for i, value in enumerate(match_wins.values):
    plt.text(value, i, str(value), va="center")

plt.tight_layout()
plt.show()


# ============================================================
# 2. What did teams choose after winning the toss?
# ============================================================

toss_decisions = (
    df_2025.groupby("match_id")["toss_decision"]
    .first()
    .value_counts()
)

plt.figure(figsize=(8, 6))

sns.barplot(
    x=toss_decisions.index,
    y=toss_decisions.values,
    palette=["orange", "skyblue"]
)

plt.title("Toss Decision Trends — IPL 2025")
plt.xlabel("Toss Decision")
plt.ylabel("Number of Matches")

plt.tight_layout()
plt.show()


# ============================================================
# 3. Does winning the toss lead to winning the match?
# ============================================================

toss_and_match_winner = (
    df_2025[
        df_2025["toss_winner"] == df_2025["winner"]
    ]["match_id"]
    .nunique()
)

total_matches = df_2025["match_id"].nunique()

toss_and_match_loser = (
    total_matches - toss_and_match_winner
)

labels = [
    "Toss + Match Win",
    "Toss Win + Match Loss"
]

values = [
    toss_and_match_winner,
    toss_and_match_loser
]

plt.figure(figsize=(7, 7))

plt.pie(
    values,
    labels=labels,
    autopct="%.1f%%",
    startangle=90,
    colors=["green", "red"]
)

plt.title("Does Winning the Toss Lead to Winning the Match?")
plt.tight_layout()
plt.show()


# ============================================================
# 4. How are teams winning?
# ============================================================

win_method = (
    df_2025.groupby("match_id")["result"]
    .first()
    .value_counts()
)

plt.figure(figsize=(8, 6))

sns.barplot(
    x=win_method.index,
    y=win_method.values,
    palette="viridis"
)

plt.title("How Teams Won Their Matches — IPL 2025")
plt.xlabel("Winning Method")
plt.ylabel("Number of Matches")

plt.tight_layout()
plt.show()


# ============================================================
# 5. Top 10 Run Scorers
# ============================================================

runs_scored = (
    df_2025.groupby("batter")["runs_scored"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# Team jersey-inspired colors
team_colors = {
    "Royal Challengers Bengaluru": "red",
    "Mumbai Indians": "blue",
    "Punjab Kings": "darkred",
    "Gujarat Titans": "blue",
    "Chennai Super Kings": "yellow",
    "Kolkata Knight Riders": "purple",
    "Rajasthan Royals": "pink",
    "Delhi Capitals": "blue",
    "Sunrisers Hyderabad": "orange",
    "Lucknow Super Giants": "green"
}


# Find each batter's team
player_team = (
    df_2025[
        df_2025["batter"].isin(runs_scored.index)
    ]
    .groupby("batter")["batting_team"]
    .first()
)


# Assign team colors
colors = [
    team_colors[player_team[player]]
    for player in runs_scored.index
]


plt.figure(figsize=(10, 6))

sns.barplot(
    y=runs_scored.index,
    x=runs_scored.values,
    palette=colors
)

plt.title("Top 10 Run Scorers — IPL 2025")
plt.xlabel("Runs")
plt.ylabel("Batter")

for i, value in enumerate(runs_scored.values):
    plt.text(value, i, str(value), va="center")

plt.tight_layout()
plt.show()


# ============================================================
# 6. Runs vs Strike Rate
# ============================================================

player_stats = (
    df_2025.groupby(["batting_team", "batter"])
    .agg(
        runs=("runs_scored", "sum"),
        balls=("ball", "count")
    )
    .reset_index()
)

player_stats["strike_rate"] = (
    player_stats["runs"]
    / player_stats["balls"]
    * 100
)


# Only include meaningful batting contributions
player_stats_filtered = player_stats[
    player_stats["runs"] >= 100
]


plt.figure(figsize=(12, 7))

sns.scatterplot(
    data=player_stats_filtered,
    x="runs",
    y="strike_rate",
    hue="batting_team",
    s=100,
    alpha=0.8,
    palette="tab10"
)

plt.title("Runs vs Strike Rate — IPL 2025")
plt.xlabel("Total Runs")
plt.ylabel("Strike Rate")

plt.legend(
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    title="Team"
)

plt.tight_layout()
plt.show()


# ============================================================
# 7. How does scoring change across the innings?
# ============================================================

runs_per_over = (
    df_2025.groupby("over")["runs_scored"]
    .sum()
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=runs_per_over.index,
    y=runs_per_over.values,
    marker="o",
    color="darkblue"
)

plt.title("Runs Scored Across Overs — IPL 2025")
plt.xlabel("Over")
plt.ylabel("Total Runs")

plt.tight_layout()
plt.show()


# ============================================================
# 8. Powerplay vs Middle Overs vs Death Overs
# ============================================================

df_2025["phase"] = pd.cut(
    df_2025["over"],
    bins=[-1, 5, 14, 19],
    labels=[
        "Powerplay",
        "Middle Overs",
        "Death Overs"
    ]
)

phase_runs = (
    df_2025
    .groupby("phase", observed=True)["runs_scored"]
    .sum()
)

print("\nRuns by innings phase:")
print(phase_runs)


plt.figure(figsize=(8, 6))

sns.barplot(
    x=phase_runs.index,
    y=phase_runs.values,
    palette=["skyblue", "orange", "red"]
)

plt.title("Runs Scored by Innings Phase — IPL 2025")
plt.xlabel("Innings Phase")
plt.ylabel("Total Runs")

plt.tight_layout()
plt.show()