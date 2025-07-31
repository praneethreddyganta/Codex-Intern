import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")
print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# Step 2: Calculate average math score
avg_math = df['math score'].mean()
print(f"Average Math Score: {avg_math:.2f}")

# Step 3: Bar chart - Average Math Score by Gender
plt.figure(figsize=(6,4))
df.groupby('gender')['math score'].mean().plot(kind='bar', color=['lightblue', 'pink'])
plt.title("Average Math Score by Gender")
plt.ylabel("Average Score")
plt.savefig("visuals/bar_chart.png")
plt.show()

# Step 4: Scatter plot - Math vs Reading scores
plt.figure(figsize=(7,5))
plt.scatter(df['math score'], df['reading score'], alpha=0.5)
plt.title("Math vs Reading Scores")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.savefig("visuals/scatter_plot.png")
plt.show()

# Step 5: Heatmap - Correlation between scores
plt.figure(figsize=(6,4))
sns.heatmap(df[['math score','reading score','writing score']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Scores")
plt.savefig("visuals/heatmap.png")
plt.show()
