import io

import gradio as gr
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud

EXAMPLE_TEXT_1 = """
Sample text in English is utilized in a variety of fields, helping to streamline processes, ensure readability, and provide a visual idea of how the final content will appear. Below are some key areas where it’s commonly used:
1. Design and Layout Testing
Graphic designers and publishers often use sample text to test layouts and ensure that the design works well with the content. Whether it’s a website, brochure, or book, sample text helps in assessing how readable the content will be once the final text is added.
2. Web Development
In web development, developers use sample text to see how text blocks will look within the layout. This is particularly useful when creating templates, ensuring the design is responsive and readable across various screen sizes.
3. Content Creation and Proofreading
For content creators, sample text can serve as a tool for practicing language skills or testing the flow of writing. Similarly, proofreaders may use it to practice checking for grammatical errors or formatting consistency.
4. Software Development
Sample text in English is also used in software development for testing user interfaces. For example, when developing text-editing software or word processors, placeholder text helps in ensuring that the software correctly handles formatting, text wrapping, and more.
"""

EXAMPLE_TEXT_2 = """
Scrum is an Agile framework that structures work into time-boxed sprints, with defined roles, artifacts, and ceremonies for iterative delivery.
Key roles include product owner, Scrum master, and development team, all collaborating to achieve sprint goals.
Scrum emphasizes transparency, inspection, and adaptation, enabling teams to respond to change and deliver value incrementally.
Start by organizing your team’s work into sprints and adopting Scrum ceremonies to improve focus and project delivery cadence.
"""


def create_image(wordcloud, figsize=(8, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    # Save the figure to an in-memory buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, dpi=150)
    buf.seek(0)
    plt.close(fig)

    return Image.open(buf)


def generate_wordcloud_1():
    wc = WordCloud(width=800, height=400, background_color='white').generate(EXAMPLE_TEXT_1)
    return create_image(wc)


def generate_wordcloud_2():
    wc = WordCloud(width=800, height=400, background_color='white', max_words=40, colormap='coolwarm').generate(
        EXAMPLE_TEXT_1)
    return create_image(wc)


def generate_wordcloud_3():
    wc = WordCloud(width=500, height=500, background_color='black', max_words=150, colormap='tab20c').generate(
        EXAMPLE_TEXT_2)
    return create_image(wc, figsize=(4, 4))


def generate_wordcloud_4():
    stopwords = {'team', 'framework', 'defined'}

    image = Image.open('data/hungary_mask.png')
    hungary_mask = np.array(image)

    wc = WordCloud(scale=3,
                   max_words=150,
                   colormap='RdYlGn',
                   mask=hungary_mask,
                   background_color='white',
                   stopwords=stopwords,
                   collocations=True).generate_from_text(EXAMPLE_TEXT_2)
    return create_image(wc, figsize=(10, 8))


def wordcloud_example():
    gr.Markdown("## <u>Wordcloud</u>", elem_classes="tight_layout")
    gr.Markdown("I show some generated wordcloud images (used with different parameters).", elem_classes="tight_next")

    output_image_1 = gr.Image(type="pil")
    output_image_2 = gr.Image(label="colormap: coolwarm", type="pil")
    output_image_3 = gr.Image(label="Background: black, colormap: tab20c", type="pil")
    output_image_4 = gr.Image(label="Hungary masked wordcloud, colormap: RdYlGn", type="pil")

    with gr.Blocks() as wcblock:
        wcblock.load(fn=generate_wordcloud_1, inputs=None, outputs=output_image_1)
        wcblock.load(fn=generate_wordcloud_2, inputs=None, outputs=output_image_2)
        wcblock.load(fn=generate_wordcloud_3, inputs=None, outputs=output_image_3)
        wcblock.load(fn=generate_wordcloud_4, inputs=None, outputs=output_image_4)
