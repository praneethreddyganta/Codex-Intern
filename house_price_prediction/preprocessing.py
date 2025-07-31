import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(train_path):
    # Load dataset
    df = pd.read_csv(train_path)
    
    # Drop ID (not useful)
    df = df.drop(['Id'], axis=1)
    
    # Drop columns with too many missing values
    cols_to_drop = ['PoolQC', 'MiscFeature', 'Alley', 'Fence']
    df = df.drop(cols_to_drop, axis=1)
    
    # Separate features and target
    X = df.drop('SalePrice', axis=1)
    y = df['SalePrice']
    
    # Fill numeric NaNs with median
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        X[col] = X[col].fillna(X[col].median())
    
    # Fill categorical NaNs with mode
    cat_cols = X.select_dtypes(include=['object']).columns
    for col in cat_cols:
        X[col] = X[col].fillna(X[col].mode()[0])
    
    # One-hot encode categorical columns
    X = pd.get_dummies(X, drop_first=True)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Test the function
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data("train.csv")
    print("Training data shape:", X_train.shape)
    print("Test data shape:", X_test.shape)

