# ETL script for importing assets from CSV/Excel
import pandas as pd
from utils.db import insert_device, insert_software, insert_license

def import_csv_devices(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        insert_device(row)

def import_csv_software(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        insert_software(row)

def import_csv_licenses(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        insert_license(row)

if __name__ == "__main__":
    # Example usage
    import_csv_devices('../data/sample_assets.csv')
    import_csv_software('../data/sample_software.csv')
    import_csv_licenses('../data/sample_licenses.csv')
