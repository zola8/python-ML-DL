# Step 1 - Select CSV file

import gradio as gr
import pandas as pd


def process_upload_and_advance(file):
    if file is None:
        gr.Warning("⚠️ No file selected. Please upload a CSV file.")
        return None, gr.Walkthrough(selected=1)

    try:
        df = pd.read_csv(file)
        gr.Info("✅ Data loaded successfully! Moving to Preview...")

        return df, gr.Walkthrough(selected=2)

    except Exception as e:
        gr.Warning(f"❌ Failed to read CSV. Details: {str(e)}")
        return None, gr.Walkthrough(selected=1)


def build_step_01(walkthrough):
    df_state = gr.State()

    with gr.Column():
        gr.Markdown("### 📂 Step 1: Select Data Source")
        gr.Markdown("Upload your dataset to begin the workflow.")

        file_input = gr.File(label="Upload CSV File", file_types=[".csv"], type="filepath")
        with gr.Row():
            with gr.Column(scale=2):
                pass
            with gr.Column(scale=2):
                load_btn = gr.Button("Load Data & Proceed ➡️", variant="primary")
            with gr.Column(scale=2):
                pass

    load_btn.click(
        fn=process_upload_and_advance,
        inputs=[file_input],
        outputs=[df_state, walkthrough]
    )

    return df_state
