from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
import pandas as pd
from sqlalchemy.orm import Session
from models import Card
import numpy as np

# 1. Load environment and set up DB engine
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
parsed = urlparse(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

# 2. Clean and normalize dataframe
def clean_card_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    keep_columns = {
        "Name": "name",
        "Position": "position",
        "Nation": "nationality",
        "League": "league",
        "Team": "club",
        "Age": "age",
        "Height": "height",
        "Weight": "weight",
        "OVR": "overall",
        "PAC": "pace",
        "SHO": "shooting",
        "PAS": "passing",
        "DRI": "dribbling",
        "DEF": "defending",
        "PHY": "physical",
        "Skill moves": "skill_moves",
        "Weak foot": "weak_foot",
        "Preferred foot": "preferred_foot",
        "play style": "traits",
        "GK Diving": "gk_diving",
        "GK Handling": "gk_handling",
        "GK Kicking": "gk_kicking",
        "GK Positioning": "gk_positioning",
        "GK Reflexes": "gk_reflexes",
    }

    # Filter and rename columns
    df = df[list(keep_columns.keys())].rename(columns=keep_columns)

    # Extract numerical height/weight
    df["height"] = pd.to_numeric(df["height"].str.extract(r"(\d+)")[0], errors="coerce").astype("Int64")
    df["weight"] = pd.to_numeric(df["weight"].str.extract(r"(\d+)")[0], errors="coerce").astype("Int64")

    # Set GK-only fields to None for non-GKs
    is_gk = df["position"] == "GK"
    gk_cols = ["gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_positioning"]
    for col in gk_cols:
        df[col] = df[col].where(is_gk)

    # Set 'defending' to None for goalkeepers
    df["defending"] = df["defending"].where(~is_gk)

    # Replace any remaining NaNs/infs with None
    df = df.replace([np.nan, np.inf, -np.inf], [None, None, None])

    return df


# 3. Read and clean the CSV
df = pd.read_csv("male_players.csv", encoding="utf-8-sig")
df = clean_card_dataframe(df)

# 4. Convert to SQLModel objects (using just 5 for testing)
sample_rows = df.head(5).to_dict(orient="records")
card_objects = [Card(**row) for row in sample_rows]

# 5. Insert into DB
with Session(engine) as session:
    session.add_all(card_objects)
    session.commit()

print("Sample rows inserted.")
print(df[df["position"] == "CB"][["name", "overall", "weight"]].head())
