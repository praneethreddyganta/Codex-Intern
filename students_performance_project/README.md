# 🎓 Students Performance Analysis & Visualization

This project analyzes student performance using **Pandas** for data handling and **Matplotlib/Seaborn** for insightful visualizations. It provides statistical analysis, correlation mapping, and visual representations to uncover patterns in student exam scores across gender, parental education, and other demographics.

---

## 📁 Project Structure

```
students_performance_project/
│
├── data/
│   └── StudentsPerformance.csv        # Dataset used for analysis
│
├── report/
│   └── insights.md                    # Written observations and insights
│
├── visuals/
│   ├── bar_chart.png                  # Bar chart visualization
│   ├── scatter_plot.png              # Scatter plot visualization
│   └── heatmap.png                   # Correlation heatmap
│
├── analysis_and_visualization.py     # Python script for loading, analyzing, and plotting
└── README.md                          # Project documentation (this file)
```

---

## 🚀 Getting Started

### 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/praneethreddyganta/Codex-Intern.git
   cd Codex-Intern/students_performance_project
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install pandas matplotlib seaborn
   ```

4. **Run the analysis:**
   ```bash
   python analysis_and_visualization.py
   ```

---

## 📊 What This Project Does

- Loads and processes the `StudentsPerformance.csv` dataset using `pandas`
- Calculates basic statistics: mean, median, and standard deviation for scores
- Generates visualizations:
  - **Bar Chart** – average scores by gender or parental education
  - **Scatter Plot** – math vs reading/writing score relationships
  - **Heatmap** – correlation matrix across all score columns

---

## 📌 Example Code Snippets

### Load CSV and Calculate Average
```python
import pandas as pd
df = pd.read_csv("data/StudentsPerformance.csv")
average_math = df["math score"].mean()
```

### Bar Chart
```python
import matplotlib.pyplot as plt
df.groupby("gender")["math score"].mean().plot(kind="bar")
plt.title("Average Math Score by Gender")
plt.savefig("visuals/bar_chart.png")
```

### Heatmap
```python
import seaborn as sns
sns.heatmap(df.corr(), annot=True)
plt.savefig("visuals/heatmap.png")
```

---

## 🔍 Sample Insights (from `report/insights.md`)

- Male students score slightly higher in math, while females outperform in reading and writing.
- Parental level of education correlates positively with student performance.
- There is a strong positive correlation between reading and writing scores.

---

## 📦 Requirements

- pandas  
- matplotlib  
- seaborn

---

## 🙏 Acknowledgements

- Dataset sourced from Kaggle’s [Students Performance in Exams Dataset](https://www.kaggle.com/spscientist/students-performance-in-exams)
- Visualization support from [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)

---

## 👨‍💻 Author

**Praneeth Reddy Ganta**  
[GitHub Profile](https://github.com/praneethreddyganta)

