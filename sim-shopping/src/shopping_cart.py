import gradio as gr


def add_item(item: str, cart: list):
    if not item or not item.strip():
        return cart, "", gr.update(value=format_cart(cart)), gr.update(choices=cart, value=None)

    new_item = item.strip()

    if new_item in cart:
        return (
            cart,
            new_item,  # Return the item back to the input field as visual feedback
            gr.update(value=f"**️ '{new_item}' is already in the cart!**\n\n{format_cart(cart)}"),
            gr.update(choices=cart, value=None)
        )

    new_cart = cart + [new_item]

    # Return new state, clear input, update markdown, update dropdown choices
    return (
        new_cart,
        "",
        gr.update(value=format_cart(new_cart)),
        gr.update(choices=new_cart, value=None)  # Reset dropdown selection after add
    )


def remove_item(item_to_remove: str, cart: list):
    if item_to_remove and item_to_remove in cart:
        new_cart = cart.copy()
        new_cart.remove(item_to_remove)
        return (
            new_cart,
            gr.update(value=format_cart(new_cart)),
            gr.update(choices=new_cart, value=None)
        )

    return cart, gr.update(value=format_cart(cart)), gr.update(choices=cart, value=item_to_remove)


def clear_cart(cart: list):
    """Clear all items from cart."""
    return (
        [],
        gr.update(value=format_cart([])),
        gr.update(choices=[], value=None)
    )


def format_cart(cart: list) -> str:
    if not cart:
        return "*Your shopping cart is empty.*"

    items = "\n".join([f"- {item}" for item in cart])
    return f"**🛒 Cart ({len(cart)} items):**\n\n{items}"
