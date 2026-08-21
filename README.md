# SIH Image Understanding AI

Conversational Image Recognition Chatbot  
Smart India Hackathon 2024 – Problem Statement SIH1604  
Organization: Bharat Electronics Limited (BEL)

---

### What this does

Upload any image → Ask questions about it in normal English → Get accurate answers.

The system detects objects, understands the scene, and maintains a proper multi-turn conversation.

---

### Features

- Image upload & preview
- Object detection + scene understanding
- Multi-turn conversation memory
- Natural language responses
- Clean Streamlit interface

---

### Tech Stack

- Python 3.10+
- Streamlit (frontend)
- Transformers + PIL
- Open-source vision-language models

---

### How to run locally

```bash
git clone https://github.com/meenavignesh-svg/SIH-IMAGE-UNDERSTANDING-AI.git
cd SIH-IMAGE-UNDERSTANDING-AI

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

### Project Structure

```
├── app.py                  # Main Streamlit app
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── vision.py           # Image understanding logic
│   ├── chat.py             # Conversation handling
│   └── utils.py            # Helper functions
├── assets/                 # Sample images (optional)
└── .gitignore
```

---

### Notes

This is a working prototype built for SIH 2024.  
Focus is on clean demonstration of core functionality rather than production hardening.

---

Built for Smart India Hackathon 2024
