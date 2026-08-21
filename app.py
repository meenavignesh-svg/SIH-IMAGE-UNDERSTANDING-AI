import streamlit as st
from PIL import Image
from src.utils import load_image, resize_for_display
from src.chat import ConversationManager

st.set_page_config(
    page_title="Image Understanding AI",
    page_icon="🖼️",
    layout="centered"
)

# keep conversation state across reruns
if "chat" not in st.session_state:
    st.session_state.chat = ConversationManager()

st.title("Conversational Image Understanding")
st.caption("Upload an image and ask questions about it")

# ---- Sidebar ----
with st.sidebar:
    st.header("Controls")
    uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "webp"])

    if st.button("Clear conversation"):
        st.session_state.chat.clear()
        st.rerun()

    st.markdown("---")
    st.markdown("**SIH 2024 – SIH1604**")
    st.markdown("Bharat Electronics Limited")

# ---- Main area ----
if uploaded is not None:
    image = load_image(uploaded)

    if image is not None:
        # only set image if it's a new one
        if st.session_state.chat.image is None:
            st.session_state.chat.set_image(image)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(resize_for_display(image), caption="Uploaded Image", use_container_width=True)

        with col2:
            st.subheader("Chat")

            # show previous messages
            for msg in st.session_state.chat.get_history():
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            # input box
            user_q = st.chat_input("Ask something about the image...")

            if user_q:
                with st.chat_message("user"):
                    st.write(user_q)

                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = st.session_state.chat.ask(user_q)
                        st.write(response)

                st.rerun()
else:
    st.info("Upload an image from the sidebar to get started.")
