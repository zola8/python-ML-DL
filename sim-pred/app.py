import gradio as gr

from app_commons import css, WELCOME
from linear_regression_01 import example01
from linear_regression_02 import example02
from wordcloud_examples import wordcloud_example
from random_forest_regression import example03

def submenu_linear_regression():
    with gr.Tabs():
        with gr.Tab("Study Hours example"):
            example01()
        with gr.Tab("California Housing"):
            example02()


def submenu_randomforest_regression():
    with gr.Tabs():
        with gr.Tab("Housing Prices example"):
            example03()


def menu_regression():
    with gr.Tabs():
        with gr.Tab("Linear Regression"):
            submenu_linear_regression()
        with gr.Tab("Random Forest"):
            submenu_randomforest_regression()
        with gr.Tab("K-Nearest Neighbours"):
            gr.Markdown("a")
        with gr.Tab("Support Vector Machine"):
            gr.Markdown("a")
        with gr.Tab("Logistic Regression"):
            gr.Markdown("a")


def menu_classification():
    with gr.Tabs():
        with gr.Tab("aaaa"):
            gr.Markdown("a")


def main_menu():
    with gr.Tabs():
        with gr.Tab("Welcome!"):
            gr.Markdown(WELCOME)
        with gr.Tab("Regression"):
            menu_regression()
        with gr.Tab("Classification"):
            menu_classification()
        with gr.Tab("Wordcloud"):
            wordcloud_example()


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
