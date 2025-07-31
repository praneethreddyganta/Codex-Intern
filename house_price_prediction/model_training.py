import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from preprocessing import preprocess_data  # Import our function

# Step 1: Get preprocessed data
X_train, X_test, y_train, y_test = preprocess_data("train.csv")

# Step 2: Build the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Predict on test set
y_pred = model.predict(X_test)

# Step 4: Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Step 5: Visualization - Actual vs Predicted
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
