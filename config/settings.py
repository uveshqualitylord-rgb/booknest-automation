import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE_URL = os.getenv(
    "BASE_URL",
    "https://booknest.niraj.shop",
).rstrip("/")
