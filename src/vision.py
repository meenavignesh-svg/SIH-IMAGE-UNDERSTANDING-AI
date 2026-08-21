from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

_processor = None
_model = None

def _get_model():
    global _processor, _model
    if _model is None:
        print("Loading vision model...")
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        _model.eval()
    return _processor, _model


def generate_caption(image: Image.Image) -> str:
    """Get a detailed caption of the image."""
    processor, model = _get_model()
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=60, num_beams=3)

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption.strip().capitalize()


def answer_question(image: Image.Image, question: str) -> str:
    """
    Visual question answering.
    We use a conditional generation approach with BLIP.
    """
    processor, model = _get_model()

    # better prompt format helps a bit
    prompt = question.strip()
    if not prompt.endswith("?"):
        prompt += "?"

    inputs = processor(image, text=prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=40,
            num_beams=4,
            early_stopping=True
        )

    answer = processor.decode(output[0], skip_special_tokens=True)

    # clean common artifacts
    answer = answer.replace(prompt, "").strip()
    if answer.lower().startswith("answer:"):
        answer = answer[7:].strip()

    if not answer or len(answer) < 2:
        return "I am not completely sure about that from the image."

    return answer.capitalize()


def get_scene_summary(image: Image.Image) -> dict:
    """
    Returns a structured summary that we can use in chat.
    """
    caption = generate_caption(image)

    return {
        "caption": caption,
        "raw_description": caption
    }
