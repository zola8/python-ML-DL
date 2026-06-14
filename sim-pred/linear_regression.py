import gradio as gr

from linear_regression_01 import example01


def example02():
    gr.Markdown("b", elem_classes="tight_layout")


def submenu_linear_regression():
    with gr.Tabs():
        with gr.Tab("Study Hours example"):
            example01()
        with gr.Tab("Random example 2"):
            example02()
