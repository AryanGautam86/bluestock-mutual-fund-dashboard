import requests
import pandas as pd
from pathlib import Path

# Create output folder if it doesn't exist
output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

# HDFC Top 100 Direct Growth Scheme Code
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

print("Fetching Live NAV Data...\n")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Print scheme details
    print("Scheme Name :", data["meta"]["scheme_name"])
    print("Fund House  :", data["meta"]["fund_house"])
    print("Scheme Code :", data["meta"]["scheme_code"])

    # Convert NAV history to DataFrame
    nav_df = pd.DataFrame(data["data"])

    print("\nLatest NAV Records:")
    print(nav_df.head())

    # Save CSV
    csv_path = output_folder / "hdfc_top100_live_nav.csv"
    nav_df.to_csv(csv_path, index=False)

    print(f"\nCSV saved successfully at:\n{csv_path}")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except KeyError:
    print("Unexpected API response format.")