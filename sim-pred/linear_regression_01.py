import gradio as gr
import pandas as pd

def example01():
    df = pd.read_csv('../src/data/study_hours.csv')

    gr.Markdown("## <u>Study Hours example</u>", elem_classes="tight_layout")
    gr.Markdown("***Description:*** This is a simple example of linear regression with one single feature.", elem_classes="tight_next")
    gr.Markdown("1. Read Data")
    gr.Dataframe(df[:5], elem_classes="tight_next")
    gr.Markdown("2. Data Structure")
    gr.Markdown("aaaa")
