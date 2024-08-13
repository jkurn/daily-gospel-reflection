import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
