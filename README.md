# Drishti – Conversational Image Understanding AI

**Smart India Hackathon 2026**  
**Problem Statement:** SIH1604 – Conversational Image Recognition Chatbot  
**Organization:** Bharat Electronics Limited (BEL)

---

### Overview

Drishti is a conversational AI system that can understand images and answer questions about them in natural language.

Upload any image → Ask questions → Get meaningful answers.

---

### Key Features

- Image understanding using Vision-Language model
- Multi-turn conversation support
- Natural language question answering about visual content
- Clean and focused user interface
- Built specifically for SIH demonstration

---

### Tech Stack

| Component            | Technology                          |
|----------------------|-------------------------------------|
| Frontend             | Streamlit                           |
| Vision Model         | BLIP (Salesforce)                   |
| Image Processing     | Pillow                              |
| Language             | Python 3.10+                        |

---

### Project Structure

```
├── app.py                  # Main application
├── requirements.txt
├── README.md
├── .gitignore
└── src/
    ├── __init__.py
    ├── utils.py            # Image helpers
    ├── vision.py           # Image captioning + VQA
    └── chat.py             # Conversation manager (Drishti)
```

---

### How to Run

```bash
git clone https://github.com/meenavignesh-svg/SIH-IMAGE-UNDERSTANDING-AI.git
cd SIH-IMAGE-UNDERSTANDING-AI

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

### Example Interaction

1. Upload an image of a street or room
2. Ask: "What do you see in the image?"
3. Follow up: "How many people are there?"
4. Ask: "What is the main object?"

---

### Notes for Jury

- This is a focused prototype built for SIH 2026.
- Core pipeline (Image → Understanding → Conversation) is fully working.
- Model used is open-source and runs locally.
- Architecture is modular so stronger models can be swapped in easily.

---

Built for Smart India Hackathon 2026  
Team Project – SIH1604
