import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

files = list(RAW_PATH.glob("*.csv"))

for file in files:
    print("="*50)
    print(file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print(df.head())