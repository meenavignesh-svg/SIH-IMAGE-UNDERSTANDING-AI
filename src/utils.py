from PIL import Image
import io

def load_image(uploaded_file):
    """Convert streamlit uploaded file into a PIL image."""
    if uploaded_file is None:
        return None
    try:
        image = Image.open(uploaded_file).convert("RGB")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def resize_for_display(image, max_width=600):
    """Keep aspect ratio, just make it smaller for UI."""
    if image is None:
        return None
    w, h = image.size
    if w <= max_width:
        return image
    ratio = max_width / float(w)
    new_h = int(h * ratio)
    return image.resize((max_width, new_h), Image.LANCZOS)
