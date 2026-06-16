import gradio as gr


DESCRIPTION = """
***Description:*** ... 

Key points:
- aaa
"""


def example_knnc01():
    # header
    gr.Markdown("## <u>...</u>", elem_classes="tight_layout")
    gr.Markdown(DESCRIPTION, elem_classes="tight_next")
