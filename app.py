import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# --- 1. Business Understanding ---
# Objective: Create an interactive web application to demonstrate simple linear regression.

# --- 6. Deployment (UI Development) ---
st.title("Interactive Simple Linear Regression")

st.sidebar.header("Model Parameters")
slope_a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 100.0, 10.0, 1.0)
num_points = st.sidebar.slider("Number of Points", 50, 500, 100, 10)
intercept_b = 5 # Fixed intercept as per steps.md

# --- 2. Data Understanding & 3. Data Preparation ---
# Generate data
np.random.seed(42)
X = np.linspace(0, 10, num_points)
y = slope_a * X + intercept_b + np.random.normal(0, noise, num_points)

df = pd.DataFrame({'X': X, 'y': y})

# --- 4. Modeling ---
st.header("Linear Regression Model")
model = LinearRegression()
X_reshaped = df['X'].values.reshape(-1, 1)
model.fit(X_reshaped, df['y'])
y_pred = model.predict(X_reshaped)

st.write(f"Model Coefficients: Slope = {model.coef_[0]:.2f}, Intercept = {model.intercept_:.2f}")


# --- 5. Evaluation ---
st.header("Model Evaluation")

r2 = r2_score(df['y'], y_pred)
mse = mean_squared_error(df['y'], y_pred)

col1, col2 = st.columns(2)
col1.metric("R-squared", f"{r2:.2f}")
col2.metric("Mean Squared Error", f"{mse:.2f}")

# Calculate residuals
df['y_pred'] = y_pred
df['residual'] = df['y'] - df['y_pred']
df['abs_residual'] = np.abs(df['residual'])

# Identify top 5 outliers
top_5_outliers = df.nlargest(5, 'abs_residual')

st.header("Data Visualization")
fig, ax = plt.subplots()
ax.scatter(df['X'], df['y'], label='Generated Data')
ax.plot(df['X'], y_pred, color='red', linewidth=2, label='Regression Line')

# Mark outliers on the plot
ax.scatter(top_5_outliers['X'], top_5_outliers['y'], color='purple', s=100, marker='o', edgecolor='black', label='Top 5 Outliers')

# Add outlier IDs to the plot
for index, row in top_5_outliers.iterrows():
    ax.annotate(f'ID:{index}', (row['X'], row['y']), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='purple')


ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# --- Display Outliers Table ---
st.header("Top 5 Outliers (by Absolute Residual)")
st.dataframe(top_5_outliers[['X', 'y', 'y_pred', 'residual']])

# --- 6. Deployment (continued) ---
# More to come
