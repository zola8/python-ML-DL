import gradio as gr

from shopping_cart import add_item, remove_item, clear_cart

css = """
    footer {visibility: hidden}
"""

with gr.Blocks(title="Sim-Shopping") as demo:
    # Session-isolated state: each user gets their own independent list
    cart_state = gr.State([])

    gr.Markdown("# --- Shopping Cart & Vision Station ---")

    with gr.Row(equal_height=False):
        # LEFT COLUMN: Shopping Cart
        with gr.Column(scale=1):
            gr.Markdown("### Shopping List")
            cart_display = gr.Markdown(value="*Your shopping cart is empty.*")

            with gr.Row():
                item_input = gr.Textbox(
                    placeholder="Enter item name...",
                    label="Add Item",
                    scale=3,
                    container=False
                )
                add_btn = gr.Button("➕ Add", variant="primary", scale=1)

            with gr.Row():
                remove_dropdown = gr.Dropdown(
                    label="Remove Item",
                    choices=[],
                    interactive=True,
                    allow_custom_value=True,
                    scale=3
                )
                remove_btn = gr.Button("❌ Remove", variant="secondary", scale=1)

            clear_btn = gr.Button("🗑️ Clear All", variant="stop")

        # RIGHT COLUMN: Camera & Vision
        with gr.Column(scale=1):
            gr.Markdown("### Camera & Vision")
            camera_feed = gr.Image(
                sources=["webcam"],
                type="numpy",
                label="Live Camera Feed",
                streaming=True,
                height=300
            )
            frame_output = gr.Image(label="Processed Frame / Detection Result", height=300)
            vision_status = gr.Textbox(label="Vision Status",
                                       value="Camera ready. Capture or upload a frame to process.", interactive=False)

        add_outputs = [cart_state, item_input, cart_display, remove_dropdown]
        add_btn.click(fn=add_item, inputs=[item_input, cart_state], outputs=add_outputs)
        item_input.submit(fn=add_item, inputs=[item_input, cart_state], outputs=add_outputs)

        remove_outputs = [cart_state, cart_display, remove_dropdown]
        remove_btn.click(fn=remove_item, inputs=[remove_dropdown, cart_state], outputs=remove_outputs)

        clear_outputs = [cart_state, cart_display, remove_dropdown]
        clear_btn.click(fn=clear_cart, inputs=[cart_state], outputs=clear_outputs)

if __name__ == "__main__":
    print('http://localhost:7860')

    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        theme=gr.themes.Soft(),
        css=css,
    )
