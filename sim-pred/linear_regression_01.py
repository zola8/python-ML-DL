import gradio as gr
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def visualize01(df, x_min, x_max, y_min, y_max):
    gr.ScatterPlot(
        df,
        x="Study Hours",
        y="Exam Score",
        title="Study Hours vs Exam Score",
        color="Exam Score",
        x_lim=[x_min, x_max],
        y_lim=[y_min, y_max],
    )


DESCRIPTION = """
***Description:*** This is a simple example of linear regression with one single feature. 

Key points:
- Linear Regression prediction
- Visualization
- Metrics calculation
- Interactive test

This is a linear regression model to predict how many studying hours are needed to reach the required exam score.
"""


def predict_with_model(number, model):
    if number is None:
        return "Please enter a valid number."
    if number < 0:
        return "Please enter a positive number."
    try:
        result = model.predict([[float(number)]])[0]
    except Exception as e:
        return f"Error during prediction: {str(e)}"

    return f"{result:.2f}"


def example01():
    # header
    gr.Markdown("## <u>Study Hours example</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")

    # 1
    gr.Markdown("### 1. Read Data")
    df = pd.read_csv('../src/data/study_hours.csv')
    gr.Dataframe(df[:5], elem_classes="tight_next")
    features = df[["Study Hours"]]
    label = df["Exam Score"]

    # 2
    gr.Markdown("### 2. Visualization")
    x_min, x_max = features.values.min() - 1, features.values.max() + 1
    y_min, y_max = label.min() - 5, label.max() + 5
    visualize01(df, x_min, x_max, y_min, y_max)

    # 3
    gr.Markdown("### 3. Train a LinearRegression model", elem_classes="tight_layout")
    gr.Markdown("I split the dataset into train and test sets (80/20%).")
    gr.Markdown("Then I train the model and visualize the best-fit line.")
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4
    gr.Markdown("### 4. Visualization with best-fit line", elem_classes="tight_layout")

    fig, ax = plt.subplots(dpi=150)
    ax.scatter(X_train, y_train, label="Data Points", color="blue")
    ax.scatter(X_test, y_test, label="Test Points", color="coral")
    ax.legend()
    plt.plot(X_train, model.predict(X_train), "r")
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    gr.Plot(value=fig)

    # 5
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    gr.Markdown("### 5. Metrics", elem_classes="tight_layout")
    with gr.Row():
        gr.Label(f"{model.intercept_:.2f}", label="Intercept (b)")
        gr.Label(f"{model.coef_[0]:.2f}", label="Coefficient (m)")
        gr.Label(f"{mae:.2f}", label="MAE")
        gr.Label(f"{mse:.2f}", label="MSE")
        gr.Label(f"{r2:.2f}", label="R² Score")

    # 6
    gr.Markdown("### 6. Show how accurate the predictions are", elem_classes="tight_layout")

    fig, ax = plt.subplots(dpi=150)
    ax.scatter(y_test, y_pred, color='blue', label='Predictions')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
    ax.legend()
    plt.xlabel('Actual Exam Scores')
    plt.ylabel('Predicted Exam Scores')
    plt.title('Actual vs. Predicted Values')
    gr.Plot(value=fig)

    # 7
    gr.Markdown("### 7. Predictions (concrete values)", elem_classes="tight_layout")
    predictions = pd.DataFrame({
        'Study Hours': X_test["Study Hours"],
        'Actual exam score': y_test,
        'Predicted exam score': y_pred
    })
    gr.Dataframe(predictions, elem_classes="tight_next")

    # 8
    gr.Markdown("### 8. Toy Calculator", elem_classes="tight_layout")

    num_input = gr.Number(
        label="Study hours",
        placeholder="10",
        precision=1
    )

    with gr.Row():
        gr.Column(scale=1)
        submit_btn = gr.Button("Submit", scale=1)
        gr.Column(scale=1)

    output_text = gr.Textbox(label="Prediction Result", interactive=False)
    model_state = gr.State(value=model)

    submit_btn.click(
        fn=predict_with_model,
        inputs=[num_input, model_state],
        outputs=output_text
    )
