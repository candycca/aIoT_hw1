# Interactive Simple Linear Regression Web App

This project implements an interactive web application using Streamlit to demonstrate simple linear regression. It allows users to generate synthetic data, fit a linear regression model, visualize the results, and identify outliers. The development process follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.

## Features

*   **Adjustable Parameters:** Easily modify the slope (`a` in `ax+b`), the amount of random noise, and the number of data points generated.
*   **Real-time Visualization:** See the generated data points and the fitted regression line update instantly as parameters are changed.
*   **Model Evaluation:** Displays key regression metrics including R-squared and Mean Squared Error (MSE).
*   **Outlier Identification:** Automatically identifies and highlights the top 5 data points with the largest absolute residuals on the plot.
*   **Outlier Details Table:** A table at the bottom of the page provides detailed information (X, actual y, predicted y, residual) for the top 5 outliers.
*   **CRISP-DM Approach:** The project structure and implementation reflect the CRISP-DM steps for a data science project.

## Setup

To run this application locally, follow these steps:

### Prerequisites

*   Python 3.7+
*   pip (Python package installer)

### Installation

1.  **Clone the repository (if applicable) or navigate to the project directory:**
    ```bash
    cd /Users/tianxinqiao/Desktop/aiotHW1
    ```
2.  **Install the required Python packages:**
    ```bash
    pip install streamlit numpy pandas scikit-learn matplotlib
    ```

## How to Run

Once the dependencies are installed, you can run the Streamlit application using the following command:

```bash
streamlit run app.py
```

This command will start a local server and open the application in your default web browser (usually at `http://localhost:8501`).

## Usage

*   Use the sliders in the sidebar to adjust the **Slope (a)**, **Noise**, and **Number of Points**.
*   Observe how the generated data, regression line, and evaluation metrics change in real-time.
*   The **Top 5 Outliers** are marked in purple on the plot with their corresponding IDs.
*   Scroll to the bottom of the page to view the **Top 5 Outliers (by Absolute Residual)** table, which includes their X, actual y, predicted y, and residual values.
