import os
import dotenv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(ROOT_DIR, ".env"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
