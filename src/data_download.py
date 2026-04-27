import os
import requests

def download_kepler_data():
    # 1. Define where to save the data
    data_dir = "data"
    file_name = "cumulative_koi.csv"
    file_path = os.path.join(data_dir, file_name)

    # 2. NASA API URL for the Cumulative KOI table (CSV format)
    # This query selects all columns from the 'cumulative' table
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+cumulative&format=csv"

    # 3. Create the data directory if it doesn't exist
    if not os.path.exists(data_dir):
        print(f"Creating directory: {data_dir}")
        os.makedirs(data_dir)

    # 4. Download the file
    print("Connecting to NASA Exoplanet Archive...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for errors

        print(f"Downloading {file_name}...")
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"Successfully downloaded to: {file_path}")
        print(f"File size: {os.path.getsize(file_path) / 1024 / 1024:.2f} MB")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_kepler_data()

import pandas as pd
df = pd.read_csv("../data/cumulative_koi.csv", comment='#')
print(df['koi_disposition'].value_counts())