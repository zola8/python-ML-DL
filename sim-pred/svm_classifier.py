import gradio as gr


DESCRIPTION = """
***Description:*** Linear regression example with multiple features. 

Key points:
- aaa
"""


def example_svmc01():
    # header
    gr.Markdown("## <u>California Housing with Linear Regression</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")
