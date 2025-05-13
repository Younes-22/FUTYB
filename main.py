from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
import pandas as pd


from models import Card  # import your Card model

# Load .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print("DB URL:", DATABASE_URL)

# Test parsing
parsed = urlparse(DATABASE_URL)
print("Parsed URL scheme:", parsed.scheme)

# Create engine
engine = create_engine(DATABASE_URL)

# Create tables
SQLModel.metadata.create_all(engine)

df = pd.read_csv("male_players.csv", encoding="utf-8-sig")
print(df.columns.tolist())
