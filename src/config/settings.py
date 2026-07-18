import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Hugging Face
# ==========================================

HF_API_KEY = os.getenv("HF_API_KEY")

HF_CHAT_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
HF_TEXT_MODEL = "google/flan-t5-large"
HF_SUMMARIZER_MODEL = "facebook/bart-large-cnn"

# ==========================================
# API
# ==========================================

HF_API_URL = "https://api-inference.huggingface.co/models"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

# ==========================================
# Aplicação
# ==========================================

APP_NAME = "AI Agent Selector"

VERSION = "1.0.0"

AUTHOR = "Davi Santos"

# ==========================================
# Configurações Gerais
# ==========================================

REQUEST_TIMEOUT = 60

MAX_TOKENS = 512