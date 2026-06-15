import gradio as gr
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DESCRIPTION = """
***Description:*** Linear regression example with multiple features. 

Key points:
- Dataset describe
- Correlation heatmap
- StandardScalar (normalizing numerical values)
- Linear Regression prediction with multiple features
"""

FEATURES_TXT = """
For simplicity the following features will be selected:
- MedInc
- AveRooms
- HouseAge

Label:
- Price
"""


def generate_heatmap(df):
    plt.figure(figsize=(8, 6), dpi=150)
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    # Return the current figure (gcf = get current figure)
    return plt.gcf()


def example02():
    # header
    gr.Markdown("## <u>California Housing with Linear Regression</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")

    df_data = fetch_california_housing()
    df = pd.DataFrame(df_data.data, columns=df_data.feature_names)
    df['Price'] = df_data.target

    # 2
    gr.Markdown("### 2. Dataset")
    gr.Dataframe(df[:5], elem_classes="tight_next")

    # 3
    df2_desc = df.describe()
    df2_desc[' '] = df.describe().index
    cols = list(df2_desc.columns)
    df2_desc = df2_desc.reindex(columns=cols[-1:] + cols[:-1])

    gr.Markdown("### 3. Dataset describe")
    gr.Dataframe(df2_desc, elem_classes="tight_next")

    # 4
    gr.Markdown("### 4. Correlation Heatmap Display", elem_classes="tight_layout")
    gr.Plot(generate_heatmap(df))
    gr.Markdown("")

    # 5
    gr.Markdown("### 5. Features and Label Selection")
    gr.Markdown(FEATURES_TXT)
    X = df[['MedInc', 'AveRooms', 'HouseAge']]
    y = df['Price']

    # 6
    gr.Markdown("### 6. Linear Regression Prediction", elem_classes="tight_layout")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_squared_error(y_test, y_pred)
    mse = mean_absolute_error(y_test, y_pred)
    with gr.Row():
        gr.Label(f"{mae:.2f}", label="MAE")
        gr.Label(f"{mse:.2f}", label="MSE")
        gr.Column(scale=1)
        gr.Column(scale=1)
        gr.Column(scale=1)

    df_vis = pd.DataFrame({"Test Truth Data": y_test, "Test Predicted Data": y_pred})
    gr.ScatterPlot(df_vis, x="Test Truth Data", y="Test Predicted Data", height=600)

    # 7
    gr.Markdown("### 7. Conclusion", elem_classes="tight_layout")
    gr.Markdown("This model doesn't perform well with this dataset.")
