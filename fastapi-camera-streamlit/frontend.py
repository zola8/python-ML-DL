import streamlit as st

# Set page configuration for a nice wide layout
st.set_page_config(page_title="Camera Stream", layout="wide")

st.title("Live Camera Feed")
st.write("Streaming directly from FastAPI via MJPEG.")

# We use st.markdown with an HTML <img> tag because Streamlit's st.image
# doesn't natively support continuous MJPEG streams.
# The browser handles the MJPEG decoding automatically.
stream_url = "http://localhost:8001/video_feed"

st.markdown(
    f"""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <img src="{stream_url}" width="640" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")
st.caption("If the image doesn't load, ensure the FastAPI backend is running on port 8001.")
