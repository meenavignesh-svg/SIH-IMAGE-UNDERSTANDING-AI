from src.vision import generate_caption, answer_question, get_scene_summary
from PIL import Image

class Drishti:
    """
    Main conversation handler for the image understanding chatbot.
    Named Drishti (vision/sight).
    """

    def __init__(self):
        self.history = []
        self.image = None
        self.scene_info = None

    def load_image(self, image: Image.Image):
        self.image = image
        self.history = []
        self.scene_info = get_scene_summary(image)

        intro = (
            f"I have analyzed the image.\n\n"
            f"**What I see:** {self.scene_info['caption']}\n\n"
            f"You can ask me questions about it."
        )
        self.history.append({"role": "assistant", "content": intro})

    def ask(self, question: str) -> str:
        if self.image is None:
            return "Please upload an image first so I can look at it."

        q = question.lower().strip()

        # handle common patterns better
        if any(x in q for x in ["describe", "what do you see", "what's in the image", "what is in the image", "caption", "tell me about the image"]):
            answer = self.scene_info["caption"]

        elif any(x in q for x in ["hello", "hi", "hey"]):
            answer = "Hello! I am Drishti. Upload an image and ask me anything about it."

        elif "who are you" in q or "your name" in q:
            answer = "I am Drishti, an image understanding assistant built for Smart India Hackathon."

        else:
            answer = answer_question(self.image, question)

        self.history.append({"role": "user", "content": question})
        self.history.append({"role": "assistant", "content": answer})

        return answer

    def get_history(self):
        return self.history

    def reset(self):
        self.history = []
        self.image = None
        self.scene_info = None
