#!/usr/bin/env python3

import os
import sys
import pandas as pd

def excel2tsv(file_excel, file_tsv):
    try:
        df = pd.read_excel(file_excel)
        df.to_csv(file_tsv, sep='\t', index=False)
        print(f"Successfully converted '{file_excel}' to '{file_tsv}'")
    except FileNotFoundError:
        print(f"Error: File '{file_excel}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_excel_path = sys.argv[1]
file_base = os.path.splitext(os.path.basename(file_excel_path))[0]
file_tab_path  = str(file_base)+".tab"

excel2tsv(file_excel_path, file_tab_path)
