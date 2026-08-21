from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# loading once so it doesn't keep reloading on every run
_processor = None
_model = None

def _load_model():
    global _processor, _model
    if _model is None:
        print("Loading BLIP model... this might take a few seconds")
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        _model.eval()
    return _processor, _model


def get_image_description(image: Image.Image) -> str:
    """Generate a basic caption for the image."""
    processor, model = _load_model()

    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs, max_length=50)

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption.strip()


def answer_about_image(image: Image.Image, question: str) -> str:
    """
    Very basic visual question answering using BLIP.
    For better results later we can swap this with a stronger VLM.
    """
    processor, model = _load_model()

    # BLIP can do conditional generation with a question-like prompt
    prompt = f"Question: {question} Answer:"
    inputs = processor(image, text=prompt, return_tensors="pt")

    with torch.no_grad():
        out = model.generate(**inputs, max_length=60)

    answer = processor.decode(out[0], skip_special_tokens=True)

    # clean up the output a bit
    if "Answer:" in answer:
        answer = answer.split("Answer:")[-1].strip()

    return answer if answer else "I'm not sure about that."
