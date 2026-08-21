import streamlit as st
from src.utils import load_image, resize_for_display
from src.chat import Drishti

st.set_page_config(
    page_title="Drishti | Image Understanding AI",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Session State ----------
if "bot" not in st.session_state:
    st.session_state.bot = Drishti()

if "image_loaded" not in st.session_state:
    st.session_state.image_loaded = False

# ---------- Sidebar ----------
with st.sidebar:
    st.title("Drishti")
    st.caption("Conversational Image Understanding")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Supports JPG, PNG and WebP"
    )

    if uploaded_file is not None:
        image = load_image(uploaded_file)
        if image is not None and not st.session_state.image_loaded:
            st.session_state.bot.load_image(image)
            st.session_state.image_loaded = True
            st.session_state.current_image = image

    if st.button("Clear & Reset", use_container_width=True):
        st.session_state.bot.reset()
        st.session_state.image_loaded = False
        if "current_image" in st.session_state:
            del st.session_state.current_image
        st.rerun()

    st.markdown("---")
    st.markdown("**Example questions you can try:**")
    st.markdown("""
    - What do you see in the image?
    - How many people are there?
    - What is the main object?
    - Describe the scene
    - What colors are dominant?
    """)

    st.markdown("---")
    st.markdown("**SIH 2024**  
    Problem Statement: SIH1604  
    Organization: Bharat Electronics Limited")

# ---------- Main UI ----------
st.title("Drishti")
st.markdown("##### Upload an image and have a conversation about it")

if not st.session_state.image_loaded:
    st.info("Upload an image from the sidebar to begin.")
else:
    col_img, col_chat = st.columns([1, 1.2], gap="large")

    with col_img:
        st.subheader("Image")
        st.image(
            resize_for_display(st.session_state.current_image, max_width=520),
            use_container_width=True
        )

    with col_chat:
        st.subheader("Conversation")

        # display chat history
        chat_container = st.container(height=420)
        with chat_container:
            for msg in st.session_state.bot.get_history():
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        # user input
        user_input = st.chat_input("Ask something about the image...")

        if user_input:
            # show user message immediately
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(user_input)

            # get response
            with st.spinner("Analyzing..."):
                response = st.session_state.bot.ask(user_input)

            st.rerun()
