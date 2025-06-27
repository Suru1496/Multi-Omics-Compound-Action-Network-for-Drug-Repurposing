import os
import pandas as pd
from bioservices import BioMart
import requests

def download_all_data():
    os.makedirs("data/raw", exist_ok=True)
    # Example: Download LINCS or GEO expression data
    # Placeholder for drug + omics data
    print("→ Downloading data placeholders...")
    with open("data/raw/README.txt", "w") as f:
        f.write("Put GEO, PRIDE, LINCS, DrugBank data here.")

    # Optionally automate DrugBank, PubChem, etc. later

