import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv("IPL.csv")

# Basic dataset information
# print(df.head())
# print(df.info())
# print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
# print(df.isnull().sum())


# --------------------------------------------------
# 1. Which team won the most matches?
# --------------------------------------------------

match_wins = df["match_winner"].value_counts()

sns.barplot(
    y=match_wins.index,
    x=match_wins.values
)

plt.title("Most Wins by a Team")
plt.xlabel("Number of Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 2. What are the toss decision trends?
# --------------------------------------------------

sns.countplot(
    data=df,
    x="toss_decision"
)

plt.title("Toss Decision Trends")
plt.xlabel("Toss Decision")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 3. How often did the toss winner also win the match?
# --------------------------------------------------

toss_winner_match_winner = (
    df["toss_winner"] == df["match_winner"]
).sum()

toss_win_percentage = (
    toss_winner_match_winner / len(df)
) * 100

print(
    f"Toss winner also won the match in "
    f"{toss_win_percentage:.2f}% of matches."
)


# --------------------------------------------------
# 4. How do teams win — by runs or wickets?
# --------------------------------------------------

sns.countplot(
    data=df,
    x="won_by"
)

plt.title("How Teams Won Matches")
plt.xlabel("Won By")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 5. Which players won Player of the Match awards most often?
# --------------------------------------------------

player_of_match = (
    df["player_of_the_match"]
    .value_counts()
    .head(10)
)

sns.barplot(
    y=player_of_match.index,
    x=player_of_match.values
)

plt.title("Top 10 Players by Player of the Match Awards")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. Which players had the highest total recorded scores?
# --------------------------------------------------

top_scorers = (
    df.groupby("top_scorer")["highscore"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    y=top_scorers.index,
    x=top_scorers.values
)

plt.title("Top 10 Scorers by Total Recorded Score")
plt.xlabel("Total Runs")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. Which bowlers took the most wickets in their best figures?
# --------------------------------------------------

df["highest_wickets"] = (
    df["best_bowling_figure"]
    .astype(str)
    .str.split("--")
    .str[0]
)

df["highest_wickets"] = pd.to_numeric(
    df["highest_wickets"],
    errors="coerce"
)

top_bowlers = (
    df.groupby("best_bowling")["highest_wickets"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    y=top_bowlers.index,
    x=top_bowlers.values
)

plt.title("Top 10 Bowlers by Wickets")
plt.xlabel("Wickets")
plt.ylabel("Bowler")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 8. Which venue hosted the most matches?
# --------------------------------------------------

venue_count = df["venue"].value_counts()

sns.barplot(
    y=venue_count.index,
    x=venue_count.values
)

plt.title("Matches Played by Venue")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 9. Which team won by the highest margin of runs?
# --------------------------------------------------

highest_run_margin = (
    df[df["won_by"] == "Runs"]
    .sort_values(by="margin", ascending=False)
    .head(1)[["match_winner", "margin"]]
)

print("\nHighest Run-Margin Victory:")
print(highest_run_margin)


# --------------------------------------------------
# 10. Which player had the highest individual score?
# --------------------------------------------------

highest_score = (
    df.loc[
        df["highscore"].idxmax(),
        ["top_scorer", "highscore"]
    ]
)

print("\nHighest Individual Score:")
print(highest_score)


# --------------------------------------------------
# 11. Which bowler had the best bowling figures?
# --------------------------------------------------

best_bowling = (
    df.loc[
        df["highest_wickets"].idxmax(),
        ["best_bowling", "best_bowling_figure"]
    ]
)

print("\nBest Bowling Figures:")
print(best_bowling)