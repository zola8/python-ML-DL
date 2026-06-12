# Step 2 - Show data/table

import gradio as gr
import pandas as pd


def get_column_choices(df):
    """Extract column names for the checkbox group."""
    if df is None or df.empty:
        return gr.CheckboxGroup(choices=[], interactive=False, label="Select columns to drop")
    return gr.CheckboxGroup(choices=list(df.columns), interactive=True, label="Select columns to drop")


def update_table_preview(df):
    """Display only the first 5 rows (Head) of the dataframe."""
    if df is None or df.empty:
        return pd.DataFrame({"Message": ["Please load a valid CSV file in Step 1 first."]})
    return df.head()


def get_navigation_status(df):
    """
    Centralized logic to determine if actions are allowed.
    Rules: Must have data, and must have at least 2 rows remaining.

    Return: Next button, Drop button
    """
    if df is None or df.empty:
        return (
            gr.Button(interactive=False, value="Load data in Step 1 first"),
            gr.Button(interactive=False, value="No data loaded")
        )

    col_count = len(df.columns)

    if col_count < 2:
        return (
            gr.Button(interactive=False, value=f"Need ≥2 columns (Current: {col_count})"),
            gr.Button(interactive=False, value=f"Need ≥2 columns (Current: {col_count})")
        )

    return (
        gr.Button(interactive=True, value="Proceed to preprocessing ➡️"),
        gr.Button(interactive=True, value="Apply drop")
    )


def drop_selected_columns(df, columns_to_drop):
    """Core Logic: Drop selected columns and validate row count."""
    if df is None or df.empty:
        gr.Warning("No data loaded.")
        nav_next, nav_drop = get_navigation_status(df)
        return df, pd.DataFrame(), nav_next, nav_drop, []

    # SAFETY FILTER: Only keep columns that actually exist in the current dataframe
    valid_columns_to_drop = [col for col in columns_to_drop if col in df.columns]

    if not valid_columns_to_drop:
        gr.Info("No columns selected. Nothing to drop.")
        nav_next, nav_drop = get_navigation_status(df)
        # Return current state and CLEAR the checkbox selection
        return df, df.head(), nav_next, nav_drop, []

    try:
        df_cleaned = df.drop(columns=valid_columns_to_drop)
        gr.Info(f"Dropped {len(valid_columns_to_drop)} column(s): {', '.join(valid_columns_to_drop)}")

        nav_next, nav_drop = get_navigation_status(df_cleaned)
        return df_cleaned, df_cleaned.head(), nav_next, nav_drop, []
    except Exception as e:
        gr.Warning(f"❌ Error: {str(e)}")
        nav_next, nav_drop = get_navigation_status(df)
        return df, df.head(), nav_next, nav_drop, list(df.columns)


def build_step_02(df_state, walkthrough):
    with gr.Column():
        gr.Markdown("# Step 2: Data Preview & Select Columns")
        gr.Markdown("Verify that your data has been loaded correctly. Drop unnecessary columns here too.")

        data_table = gr.Dataframe(label="Dataset Preview", interactive=False)

        with gr.Group():
            gr.Markdown("#### 🗑️ Drop Unnecessary Columns")
            col_selector = gr.CheckboxGroup(choices=[], label="Select columns to drop")

            with gr.Row():
                apply_drop_btn = gr.Button("Apply Drop", variant="secondary")
                next_3_btn = gr.Button("Proceed to Preprocessing ➡️", variant="primary")

    # --- Event Listeners ---

    # A. When Data Changes: Update Table, Choices, and Button States
    df_state.change(
        fn=update_table_preview,
        inputs=[df_state],
        outputs=[data_table]
    )

    df_state.change(
        fn=get_column_choices,
        inputs=[df_state],
        outputs=[col_selector]
    )

    df_state.change(
        fn=get_navigation_status,
        inputs=[df_state],
        outputs=[next_3_btn, apply_drop_btn]
    )

    # B. Apply Drop Logic
    apply_drop_btn.click(
        fn=drop_selected_columns,
        inputs=[df_state, col_selector],
        outputs=[df_state, data_table, next_3_btn, apply_drop_btn, col_selector]
    )

    # C. Navigation Logic
    next_3_btn.click(
        fn=lambda: gr.Walkthrough(selected=3),
        inputs=[],
        outputs=[walkthrough]
    )
