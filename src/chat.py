from src.vision import get_image_description, answer_about_image
from PIL import Image

class ConversationManager:
    def __init__(self):
        self.history = []
        self.image = None
        self.base_caption = None

    def set_image(self, image: Image.Image):
        self.image = image
        self.history = []
        # get a basic description once when image is uploaded
        self.base_caption = get_image_description(image)
        self.history.append({
            "role": "assistant",
            "content": f"I can see the image. Here's a quick description: {self.base_caption}"
        })

    def ask(self, question: str) -> str:
        if self.image is None:
            return "Please upload an image first."

        # simple context awareness
        lower_q = question.lower().strip()

        if any(word in lower_q for word in ["describe", "what do you see", "what's in the image", "caption"]):
            answer = self.base_caption
        else:
            answer = answer_about_image(self.image, question)

        self.history.append({"role": "user", "content": question})
        self.history.append({"role": "assistant", "content": answer})

        return answer

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
        self.image = None
        self.base_caption = None
