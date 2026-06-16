import gradio as gr
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

DESCRIPTION = """
***Description:*** I use DecisionTree Classifier here to predict if a student is passed an exam or not.

There are 2 features: studied hours and attendance. 

Key points:
- aaa
"""


def visualize_space_separation(X, model, X_train, X_test, y_train, y_test):
    fig, ax = plt.subplots(dpi=150, figsize=(20, 10))

    x_min, x_max = X["hours_studied"].min() - 1, X["hours_studied"].max() + 1
    y_min, y_max = X["attendance"].min() - 10, X["attendance"].max() + 10
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.1),  # Step size 0.1 for smoothness
        np.arange(y_min, y_max, 0.5)  # Step size 0.5 for smoothness
    )
    grid_points = np.c_[xx.ravel(), yy.ravel()]

    # Predict the class for every point in the grid
    Z = model.predict(grid_points)
    Z = Z.reshape(xx.shape)  # Reshape back to grid dimensions

    # Plot the decision boundary (colored regions)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
    plt.colorbar(label="Predicted Class")

    ax.scatter(
        X_train["hours_studied"],
        X_train["attendance"],
        c=y_train,
        edgecolors='k',
        s=100,
        cmap='RdYlBu',
        label="Train Data"
    )

    ax.scatter(
        X_test["hours_studied"],
        X_test["attendance"],
        c=y_test,
        edgecolors='k',
        s=150,
        marker='^',
        cmap='RdYlBu',
        label="Test Data"
    )

    plt.xlabel("Hours Studied")
    plt.ylabel("Attendance (%)")
    plt.title("Decision Tree Feature Space Separation\n(Max Depth = 3)")
    plt.grid(True, linestyle='--', alpha=0.5)
    fig.legend(loc="upper right")
    gr.Plot(value=fig)


def example_dt01():
    # header
    gr.Markdown("## <u>Study Hours example #2</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")

    # 1
    gr.Markdown("### 1. Read Data")
    data = {
        "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4],
        "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 52, 90, 40, 80],
        "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    gr.Dataframe(df, elem_classes="tight_next")

    # 2
    gr.Markdown("### 2. Train + Prediction + Evaluation")

    X = df.drop(["passed"], axis=1)
    y = df["passed"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = DecisionTreeClassifier(random_state=42, max_depth=3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    gr.Markdown(f"Accuracy:  {accuracy_score(y_test, y_pred)}")

    # 3
    gr.Markdown("### 3. Decision Tree Visualization", elem_classes="tight_layout")
    fig, ax = plt.subplots(dpi=150, figsize=(20, 10))
    plot_tree(
        model,
        feature_names=["hours_studied", "attendance"],
        class_names=["fail", "pass"],
        filled=True,
        rounded=True
    )
    gr.Plot(value=fig)

    # 4
    gr.Markdown("### 4. Decision Tree Feature Space Separation")
    gr.Markdown(
        "Together with the 2 features: if enough hours were studied and/or enough attendance has happened, will the student pass the exam?")
    visualize_space_separation(X, model, X_train, X_test, y_train, y_test)
