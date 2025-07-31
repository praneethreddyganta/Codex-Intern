# Advanced House Price Prediction using Linear Regression

## 1. Project Overview

This project presents a comprehensive, step-by-step methodology for predicting house prices using the Ames Housing dataset from Kaggle. The primary objective is to develop a robust linear regression model through rigorous data preprocessing, insightful exploratory data analysis (EDA), and creative feature engineering. The project also explores advanced regularization techniques (Ridge and Lasso) to improve model performance and prevent overfitting.

This repository serves as a demonstration of a complete data science workflow, from initial data exploration to final model evaluation and interpretation.

## 2. Table of Contents

- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Workflow](#project-workflow)
- [Data Cleaning & Preprocessing](#data-cleaning--preprocessing)
- [Feature Engineering](#feature-engineering)
- [Modeling & Evaluation](#modeling--evaluation)
- [How to Use](#how-to-use)
- [Acknowledgements](#acknowledgements)

## 3. Project Structure
house-price-prediction/
├── data/
│   ├── raw/
│   │   └── house-prices.csv
│   └── processed/
│       └── cleaned_data.csv
├── notebooks/
│   └── 01_data_exploration_and_modeling.ipynb
├── src/
│   ├── data_preprocessing.py
│   └── model_training.py
├── models/
│   └── linear_regression_model.pkl
├── reports/
│   └── figures/
│       ├── price_vs_size_scatterplot.png
│       └── feature_correlation_heatmap.png
└── README.md

- `data/`: Contains datasets. `raw/` for original, untouched data; `processed/` for cleaned/preprocessed data.
- `notebooks/`: Jupyter Notebooks for exploration and analysis.
- `src/`: Source code for data processing and modeling.
- `models/`: Saved, trained model files.
- `reports/`: Generated figures and analysis.

## 4. Technologies Used

- Python 3.8+
- Pandas
- NumPy
- Matplotlib & Seaborn
- Scikit-learn
- JupyterLab

## 5. Installation
1. Clone the repository
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install required packages
pip install -r requirements.txt

> **Note:** You need a `requirements.txt` listing all mentioned libraries.

## 6. Project Workflow

1. **Data Loading**: Load raw `train.csv` and `test.csv` files.
2. **Data Preprocessing**: Clean data and handle missing values/outliers.
3. **EDA**: Analyze target (`SalePrice`) and relationships.
4. **Feature Engineering**: Create features to improve model accuracy.
5. **Modeling**: Train and evaluate:
    - Baseline Linear Regression
    - Ridge Regression (L2)
    - Lasso Regression (L1, automatic feature selection)
6. **Evaluation**: Metrics include RMSLE, R², MAE, and RMSE.

## 7. Data Cleaning & Preprocessing

- **Missing Values**:
    - Categorical: Replace `NA` with `'None'` for features like `PoolQC`, `Alley`, `Fence`, and garage/basement columns.
    - Numerical: Impute `LotFrontage` by median, grouped by `Neighborhood`.
- **Outlier Detection**: Remove extreme outliers (e.g., from `GrLivArea` vs. `SalePrice` plots).
- **Target Transformation**: Apply `np.log1p(SalePrice)` to reduce right skew.

## 8. Feature Engineering

- **TotalSF**: Total basement, 1st, and 2nd floor square footage.
- **TotalBath**: Weighted sum of all bathrooms.
- **HouseAge**: `YrSold - YearBuilt`
- **Qual_SF**: `OverallQual` x `TotalSF`
- **Encoding**: One-Hot for nominal features; Label Encoding for ordinal.

## 9. Modeling & Evaluation

| Model                  | Test R² | Test RMSLE | Features Used |
|------------------------|---------|------------|--------------|
| OLS Linear Regression  | 0.88    | 0.145      | 220          |
| Ridge Regression       | 0.90    | 0.132      | 220          |
| Lasso Regression       | 0.91    | 0.128      | 115          |

- **Final Model:** Lasso Regression (best score, automatic feature selection).

## 10. How to Use

1. Install dependencies from `requirements.txt`.
2. Put `train.csv` and `test.csv` in `data/raw/`.
3. Run `notebooks/01_data_exploration_and_modeling.ipynb` for the full pipeline.
4. The trained model (`lasso`) is saved in `models/`.

## 11. Acknowledgements

This project was undertaken as part of a learning curriculum. Special thanks to CodexIntern for their guidance and for providing the foundational knowledge and project framework.

