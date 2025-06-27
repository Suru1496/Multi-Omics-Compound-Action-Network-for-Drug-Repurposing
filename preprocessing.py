import pandas as pd
import numpy as np

def process_all():
    # Dummy loading for now
    expr_path = "data/raw/omics_expression.csv"
    drug_path = "data/raw/drug_info.csv"
    
    print(f"Loading: {expr_path} and {drug_path}")
    expression_df = pd.read_csv(expr_path)
    drug_df = pd.read_csv(drug_path)

    # Normalize gene expression
    expression_df = (expression_df - expression_df.mean()) / expression_df.std()

    return expression_df, drug_df

