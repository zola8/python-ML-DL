# Step 1 - Select CSV file

import gradio as gr
import pandas as pd

from datasets import get_sample_dataset, get_dataset_names


def process_upload_and_advance(file, sample_dataset):
    df = None

    # Priority 1: User uploaded a file
    if file is not None:
        try:
            df = pd.read_csv(file)
            gr.Info("File loaded successfully.")
        except Exception as e:
            gr.Warning(f"❌ Failed to read CSV file. Details: {str(e)}")
            return None, gr.Walkthrough(selected=1)

    # Priority 2: User selected a sample dataset
    elif sample_dataset:
        try:
            df = get_sample_dataset(sample_dataset)
            if df is not None:
                gr.Info(f"Sample dataset '{sample_dataset}' loaded...")
            else:
                raise ValueError("Unknown sample dataset selected.")
        except Exception as e:
            gr.Warning(f"❌ Failed to generate sample data. Details: {str(e)}")
            return None, gr.Walkthrough(selected=1)

    # Priority 3: Neither was provided
    else:
        gr.Warning("No data source selected. Please upload a file or choose a sample.")
        return None, gr.Walkthrough(selected=1)

    return df, gr.Walkthrough(selected=2)


def build_step_01(walkthrough):
    df_state = gr.State()

    with gr.Column():
        gr.Markdown("# Step 1: Select Data Source")

        with gr.Row(equal_height=True):
            with gr.Column():
                gr.Markdown("### 📁 Option 1: Upload file")
                file_input = gr.File(
                    label="Upload CSV file",
                    file_types=[".csv"],
                    type="filepath"
                )

            with gr.Column():
                gr.Markdown("### 🎲 Option 2: Generate or fetch sample")
                sample_dropdown = gr.Dropdown(
                    choices=get_dataset_names(),
                    label="Select a sample dataset",
                    value=None,
                    allow_custom_value=False
                )

        with gr.Row():
            with gr.Column(scale=2):
                pass
            with gr.Column(scale=2):
                load_btn = gr.Button("Load Data & Proceed ➡️", variant="primary")
            with gr.Column(scale=2):
                pass

    load_btn.click(
        fn=process_upload_and_advance,
        inputs=[file_input, sample_dropdown],
        outputs=[df_state, walkthrough]
    )

    return df_state
