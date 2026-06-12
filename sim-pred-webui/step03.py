# Step 3 - Delete unnecessary data

import gradio as gr

def build_step_03():
    with gr.Column():
        gr.Markdown("### ⚙️ Step 3: Data Preprocessing")
        gr.Markdown("*Placeholder: Handle missing values, encode categoricals, scale features, etc.*")
        gr.Button("Run Preprocessing", variant="secondary")
        gr.Markdown("*(You can implement this logic later)*")
