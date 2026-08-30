# 🏏 IPL 2025 Analysis

A data analysis and visualization project exploring the Indian Premier League (IPL) 2025 using Python, Pandas, Matplotlib, and Seaborn.

The project uses ball-by-ball IPL data to analyze team performance, toss decisions, match outcomes, batting performance, strike rates, scoring patterns, and innings phases.

---

## 🎯 Project Objective

The goal of this project is to explore IPL 2025 data and answer meaningful cricket-related questions using data analysis and visualization.

The project focuses on:

- Team performance
- Toss decisions
- Impact of winning the toss
- Match-winning methods
- Batting performance
- Runs vs Strike Rate
- Scoring patterns across overs
- Powerplay, Middle Overs, and Death Overs

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Dataset

The project uses a ball-by-ball IPL dataset stored in:

iplall.csv

The dataset is loaded using Pandas and filtered to extract IPL 2025 data.

The analysis uses information such as:

- Match ID
- Season
- Teams
- Winner
- Toss Winner
- Toss Decision
- Batter
- Batting Team
- Runs Scored
- Over
- Match Result

---

# 📊 Analysis & Visualizations

## 1. Teams with the Most Wins

The project calculates the number of matches won by each team during IPL 2025.

A bar chart is used to visualize the results.

### Question

Which teams had the most wins in IPL 2025?

---

## 2. Toss Decision Trends

The project analyzes what teams chose after winning the toss.

Possible decisions include:

- Bat
- Field

A bar chart is used to visualize the results.

### Question

What did teams choose after winning the toss?

---

## 3. Does Winning the Toss Lead to Winning the Match?

The project compares:

- Toss Winner + Match Winner
- Toss Winner + Match Loser

A pie chart is used to visualize the results.

### Question

Does winning the toss lead to winning the match?

---

## 4. How Teams Won Their Matches

The project analyzes the match result field to understand how teams won their matches.

A bar chart is used to visualize the different winning methods.

### Question

How did teams win their matches?

---

## 5. Top 10 Run Scorers

The project calculates total runs scored by each batter and identifies the top 10 run scorers of IPL 2025.

A bar chart is used to visualize the results.

Team-inspired colors are used to make the visualization easier to interpret.

### Question

Who were the top run scorers of IPL 2025?

---

## 6. Runs vs Strike Rate

Player statistics are calculated using:

- Total runs
- Total balls
- Strike rate

Strike Rate = (Runs / Balls) × 100

Only players with at least 100 runs are included to focus on meaningful batting contributions.

A scatter plot is used to compare total runs with strike rate.

### Question

How does a batter's scoring volume relate to their strike rate?

---

## 7. Runs Scored Across Overs

The project calculates the total runs scored in each over across IPL 2025 matches.

A line graph is used to visualize how scoring changes throughout an innings.

### Question

How does scoring change across the innings?

---

## 8. Powerplay vs Middle Overs vs Death Overs

The innings are divided into three phases:

- Powerplay → Overs 1–6
- Middle Overs → Overs 7–15
- Death Overs → Overs 16–20

The project calculates the total runs scored during each phase.

A bar chart is used to compare the three phases.

### Question

Which phase of an innings produces the most runs?

---

# 📈 Visualizations

The project includes:

- Team Wins Bar Chart
- Toss Decision Bar Chart
- Toss Impact Pie Chart
- Winning Method Bar Chart
- Top 10 Run Scorers Bar Chart
- Runs vs Strike Rate Scatter Plot
- Runs Across Overs Line Graph
- Innings Phase Comparison Bar Chart

---

# 🧠 Data Analysis Concepts Used

This project demonstrates practical use of:

- Data loading with Pandas
- Data filtering
- Data cleaning
- groupby()
- value_counts()
- agg()
- sort_values()
- head()
- nunique()
- Conditional filtering
- Creating derived columns
- pd.cut()
- Data aggregation
- Matplotlib
- Seaborn
- Bar charts
- Line charts
- Pie charts
- Scatter plots
- Cricket performance analysis

---

# 📁 Project Structure

ipl-2025-analysis/
│
├── iplall.csv
├── ipl_2025_analysis.py
│
├── screenshots/
│   ├── team_wins.png
│   ├── toss_decision.png
│   ├── toss_impact.png
│   ├── top_run_scorers.png
│   ├── runs_vs_strike_rate.png
│   ├── runs_across_overs.png
│   └── innings_phase.png
│
└── README.md

---

# ▶️ How to Run

## 1. Clone the Repository

git clone <your-repository-url>

## 2. Navigate to the Project

cd ipl-2025-analysis

## 3. Install Required Libraries

pip install pandas matplotlib seaborn

## 4. Run the Project

python ipl_2025_analysis.py

The program will load the IPL dataset, filter IPL 2025 data, perform the analysis, and generate the visualizations.

---

# 📸 Visualizations

Selected graphs from the project are included in the screenshots folder.

These screenshots provide a quick overview of the analysis directly from the GitHub repository.

---

# 🚀 Future Improvements

Possible future improvements include:

- Player-wise bowling analysis
- Team batting comparisons
- Team bowling comparisons
- Venue-wise analysis
- Powerplay strike-rate analysis
- Death-over performance analysis
- Partnership analysis
- Player consistency analysis
- Team performance trends
- More advanced cricket analytics
- SQL-based analysis
- Interactive Power BI dashboard

---

# 📚 Learning Outcomes

This project helped me practice real-world data analysis using cricket data.

Through this project, I learned how to:

- Work with a ball-by-ball dataset
- Filter data for a specific season
- Aggregate match statistics
- Calculate player statistics
- Create meaningful cricket metrics
- Ask analytical questions
- Convert analytical results into visualizations
- Use Pandas for data analysis
- Use Matplotlib and Seaborn for visualization
- Present data-driven results visually

---

# 👨‍💻 Author

**Revanth Bhanu**

A cricket-focused data analysis project exploring IPL 2025 using Python, Pandas, Matplotlib, and Seaborn.
