import gradio as gr

from linear_regression import submenu_linear_regression

css = """
    footer {visibility: hidden}
    .tight_layout {margin: 1em 0}
    .tight_next {margin-bottom: 1.5em}
"""

with gr.Blocks(title="Sim-Pred") as app:
    gr.Markdown("# Data Science Workflow App (by Zoltan)", elem_classes="tight_layout")

    with gr.Tabs(selected=None):
        with gr.Tab("Welcome!"):
            gr.Markdown("a")
        with gr.Tab("Linear Regression"):
            submenu_linear_regression()
        with gr.Tab("Decision Tree"):
            gr.Markdown("a")
        with gr.Tab("Random Forest"):
            gr.Markdown("a")
        with gr.Tab("K-Nearest Neighbours"):
            gr.Markdown("a")
        with gr.Tab("Support Vector Machine"):
            gr.Markdown("a")
        with gr.Tab("Logistic Regression"):
            gr.Markdown("a")



if __name__ == '__main__':
    app.queue()
    app.launch(
        css=css,
    )
