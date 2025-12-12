import pandas as pd
import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv
import shutil


load_dotenv()
        # FOLDER PATH
UPLOAD = Path(r"C:\MyFile\Python\SingleFileETL\UPLOAD")
RAW = Path(r"C:\MyFile\Python\SingleFileETL\RAW")
FAILED = Path(r"C:\MyFile\Python\SingleFileETL\FAILED")

        # MAKE SURE THE FOLDER EXIST
UPLOAD.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)
FAILED.mkdir(parents=True, exist_ok=True)


        # DATABASE CREDENTIALS
DB_URL = os.getenv("DB_URL")
TABLE = ("roster")

engine = create_engine(DB_URL)

        # REQUIRED COLUMNS
ROSTER_COLS = {"agent_id", "agent_name", "unit_manager", "hire_date", "department", "lob", "username", "wave", "month"}

        # TRANSFORM FUNCTION
def clean(df: pd.DataFrame) -> pd.DataFrame:
    cols = (
        pd.Series(df.columns)
        .str.lower()
        .str.strip()
        .str.replace(" ","_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    df = df.copy()
    df.columns = cols
    return df

for file in UPLOAD.glob("*.xlsx"):
    try:
        df = pd.read_excel(file)
        print(f"Extracting: {file.name}")

        df = clean(df)
        print(f"Transforming: {file.name}")

        missing = ROSTER_COLS - set(df.columns)
        if missing:
            raise ValueError(f"Missing Columns: {sorted(missing)}")
        
        df.to_sql(TABLE, engine, if_exists="append", index=False)
        print("Loading Clean Data to Database")

        shutil.move(str(file), str(RAW / file.name))
        print("Raw file moved to RAW folder")
        
    except Exception as e:
        print(f"Failed to {e}")
        shutil.move(str(file), str(FAILED / file.name))
        print("Moved the raw Data to FAILED folder")














    

