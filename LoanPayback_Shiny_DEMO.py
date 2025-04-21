from shiny import App, ui, render
import pandas as pd
import pickle

# Load the model
file_to_load = 'lend_logistic_model.pkl'
with open(file_to_load, 'rb') as file:
    loaded_model = pickle.load(file)

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("💰 Loan Default Prediction"),
    ui.p("Enter a potential loan customer's details to predict their risk of default."),
    ui.input_checkbox("ownhome", "Own Their Home?", value=False),
    ui.input_slider("income", "Family Income", min=20000, max=200000, value=80000),
    ui.input_slider("dti", "Debt-to-Income Ratio", min=0, max=40, value=10),
    ui.input_slider("fico", "FICO Score", min=300, max=850, value=650),
    ui.input_action_button("predict", "Predict Loan Default"),
    ui.output_text_verbatim("prediction"),
    ui.output_plot("probability_chart"),
    ui.hr(),
    ui.p("Developed by Matt Bailey as simple ML Web App Demo | Powered by Shiny for Python")
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def prediction():
        if input.predict():  # Check if the button is clicked
            # Create a new customer DataFrame
            new_customer = pd.DataFrame({
                'home_ownership': [int(input.ownhome())],
                'income': [input.income()],
                'dti': [input.dti()],
                'fico': [input.fico()]
            })

            # Predict probability and class
            predicted_prob = loaded_model.predict_proba(new_customer)[:, 0]
            predicted_class = loaded_model.predict(new_customer)

            # Format the predicted probability
            formatted_prob = f"{predicted_prob[0]:.2f}"

            # Return the prediction result
            if predicted_class[0] == 0:
                return f"Predicted Class: Default\nPredicted Probability of Default: {formatted_prob}"
            else:
                return f"Predicted Class: Not Default\nPredicted Probability of Default: {formatted_prob}"

    @output
    @render.plot
    def probability_chart():
        if input.predict():  # Check if the button is clicked

            # Create a new customer DataFrame
            new_customer = pd.DataFrame({
                'home_ownership': [int(input.ownhome())],
                'income': [input.income()],
                'dti': [input.dti()],
                'fico': [input.fico()]
            })

            # Predict probability and class
            predicted_prob = loaded_model.predict_proba(new_customer)[:, 0]
            predicted_class = loaded_model.predict(new_customer)

            # Create a bar chart
            probabilities = [predicted_prob[0], 1 - predicted_prob[0]]
            labels = ['Default', 'Not Default']
            chart_data = pd.DataFrame({'Label': labels, 'Probability': probabilities})

            # Plot the bar chart
            # add a color to the bars based on the predicted class
            ax = chart_data.plot(
                x='Label', y='Probability', kind='bar', legend=False, color=['orange', 'blue']
            )
            ax.set_title("Prediction Breakdown")
            ax.set_ylabel("Probability")
            ax.set_xlabel("")
            # rotate x-axis labels for better readability
            ax.set_xticklabels(labels, rotation=0)
            return ax.get_figure()
   
# Create the app
app = App(app_ui, server)