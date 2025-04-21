# 💰 Loan Default Prediction App

This is a simple machine learning web application built using **Shiny for Python**. The app predicts the likelihood of a loan default based on user-provided inputs such as home ownership, income, debt-to-income ratio, and FICO score.

## Features
- **Interactive UI**: Users can input customer details using sliders and checkboxes.
- **Prediction**: The app uses a pre-trained logistic regression model to predict the probability of loan default.
- **Visualization**: Displays a bar chart showing the breakdown of the prediction probabilities.

## How It Works
1. Users provide the following inputs:
   - **Own Their Home?**: Checkbox to indicate home ownership.
   - **Family Income**: Slider to input annual income.
   - **Debt-to-Income Ratio**: Slider to input the debt-to-income ratio.
   - **FICO Score**: Slider to input the FICO credit score.
2. The app uses a pre-trained logistic regression model (`lend_logistic_model.pkl`) to calculate:
   - The probability of default.
   - The predicted class (Default or Not Default).
3. The results are displayed as:
   - A textual prediction summary.
   - A bar chart showing the probability breakdown.

## Installation

### Prerequisites
- Python 3.7 or later
- Required Python packages:
  - `shiny`
  - `pandas`
  - `matplotlib`
  - `pickle`

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd LoanDefaultShiny_DEMO
