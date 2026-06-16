import gradio as gr
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

DESCRIPTION = """
***Description:*** Random Forest Regression for predict house sale price. 

I created 8 different models including **DecisionTreeRegressor** and **RandomForestRegressor**.

I will compare their MAE scoring to evaluate them to find out, which model (parameters) is the better for later prediction.

Key points:
- DecisionTreeRegressor and RandomForestRegressor models
- Multiple model comparison
- Visualize DecisionTree
"""


def score_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = mean_absolute_error(y_test, y_pred)
    return score


def get_model_scores(X_test, X_train, y_test, y_train):
    model_1 = ('model_1', 'DecisionTreeRegressor(max_depth=5)', DecisionTreeRegressor(max_depth=5, random_state=1))
    model_2 = ('model_2', 'DecisionTreeRegressor(max_leaf_nodes=100)',
               DecisionTreeRegressor(max_leaf_nodes=100, random_state=1))
    model_3 = ('model_3', 'RandomForestRegressor()', RandomForestRegressor(random_state=1))
    model_4 = ('model_4', 'RandomForestRegressor(n_estimators=50)',
               RandomForestRegressor(n_estimators=50, random_state=0))
    model_5 = ('model_5', 'RandomForestRegressor(n_estimators=100)',
               RandomForestRegressor(n_estimators=100, random_state=0))
    model_6 = ('model_6', 'RandomForestRegressor(n_estimators=100, criterion="absolute_error")',
               RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0))
    model_7 = ('model_7', 'RandomForestRegressor(n_estimators=200, min_samples_split=20)',
               RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0))
    model_8 = ('model_8', 'RandomForestRegressor(n_estimators=100, max_depth=7)',
               RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0))
    models = [model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8]
    cols = ['Model', 'MAE Score']
    arr = []
    for model_name, model_description, model in models:
        score = score_model(model, X_train, X_test, y_train, y_test)
        arr.append([model_description, score])

    df_scores = pd.DataFrame(arr, columns=cols)
    return df_scores


def example03():
    # header
    gr.Markdown("## <u>Housing Prices with Decision Tree and Random Forest</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")

    # 1
    df = pd.read_csv('../src/data/housing_prices_train.csv')
    features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
    df = df[features + ['SalePrice']]
    X_train, X_test, y_train, y_test = train_test_split(df[features], df.SalePrice, random_state=42)

    gr.Markdown("### 1. Read Data and select Features")
    gr.Dataframe(df[:5], elem_classes="tight_next")

    # 2
    gr.Markdown("### 2. Create and score Models")
    gr.Markdown("Here I created different models and run calculations.")
    gr.Markdown("The less is the MAE score is the better.")
    df_scores = get_model_scores(X_test, X_train, y_test, y_train)
    winner = df_scores[df_scores['MAE Score'] == df_scores['MAE Score'].min()].iloc[0]

    gr.Dataframe(df_scores, elem_classes="tight_next")

    gr.Markdown(f"So the winner model is **{winner['Model']}** with score **{winner['MAE Score']:.3f}**")

    # 3
    gr.Markdown("### 3. Visualizing a Single Decision Tree from Random Forest", elem_classes="tight_layout")

    model7 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
    model7.fit(X_train, y_train)
    model7.predict(X_test)

    # 4
    fig, ax = plt.subplots(dpi=150, figsize=(20, 10))
    tree_to_plot = model7.estimators_[0]
    plot_tree(tree_to_plot, feature_names=df.columns.tolist(), filled=True, rounded=True, fontsize=10)
    gr.Plot(value=fig)
