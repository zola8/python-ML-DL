# Main Orchestrator app

import gradio as gr

from step01 import build_step_01
from step02 import build_step_02
from step03 import build_step_03
from step04 import build_step_04
from step05 import build_step_05


# Initialize the main Gradio Blocks interface
with gr.Blocks(title="Sim-Pred data science workflow (by Zoltan)") as app:
    gr.Markdown("# Data Science Workflow App")
    gr.Markdown("A modular, 5-step pipeline for your data science/predictions tasks.")

    with gr.Walkthrough(selected=1) as walkthrough:
        with gr.Step("Data Source", id=1):
            dataframe_state = build_step_01(walkthrough)

        with gr.Step("Data Preview & Select Columns", id=2):
            build_step_02(dataframe_state, walkthrough)

        with gr.Step("Preprocessing", id=3):
            build_step_03()

        with gr.Step("Modeling", id=4):
            build_step_04()

        with gr.Step("Evaluation", id=5):
            build_step_05()


if __name__ == "__main__":
    print('Running on local URL:  http://127.0.0.1:7860')
    app.queue()
    app.launch(
        server_name="0.0.0.0", server_port=7860,
        css="footer {visibility: hidden}",
        theme=gr.themes.Glass(),
        show_error=True,
        # share=True
    )
