import gradio as gr

from app_commons import css, WELCOME
from decision_tree_classifier import example_dt01
from knn_classifier import example_knnc01
from linear_regression_01 import example01
from linear_regression_02 import example02
from logistic_regression import example_lr01
from random_forest_classifier import example_rfc01
from random_forest_regression import example03
from svm_classifier import example_svmc01
from wordcloud_examples import wordcloud_example


def submenu_linear_regression():
    with gr.Tabs():
        with gr.Tab("Study Hours example"):
            example01()
        with gr.Tab("California Housing"):
            example02()


def menu_regression():
    with gr.Tabs():
        with gr.Tab("Linear Regression"):
            submenu_linear_regression()
        with gr.Tab("Random Forest"):
            example03()


def menu_classification():
    with gr.Tabs():
        with gr.Tab("Logistic Regression"):
            example_lr01()
        with gr.Tab("Decision Tree"):
            example_dt01()
        with gr.Tab("Random Forest"):
            example_rfc01()
        with gr.Tab("K-Nearest Neighbours"):
            example_knnc01()
        with gr.Tab("Support Vector Machine"):
            example_svmc01()


def main_menu():
    with gr.Tabs():
        with gr.Tab("Welcome!"):
            gr.Markdown(WELCOME)
        with gr.Tab("Regression"):
            menu_regression()
        with gr.Tab("Classification"):
            menu_classification()
        # with gr.Tab("Wordcloud"):
        #     wordcloud_example()


with gr.Blocks(title="Sim-Pred") as app:
    gr.Markdown("# Data Science Workflow App (by Zoltan)", elem_classes="tight_layout")
    main_menu()

if __name__ == '__main__':
    print("Local URL: http://localhost:7860")
    app.queue()
    app.launch(
        css=css,
        server_name="0.0.0.0",
        server_port=7860,
    )
