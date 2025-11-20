import pandas as pd
import numpy as np
import glob
import csv

def csv_merger(path_pattern):
    dfs = []
    for filepath in glob.glob(path_pattern):
        with open(filepath, newline='') as f:
            #Todo: Skip first three lines when reading to get correct columns
            data = pd.DataFrame(csv.reader(f))
            dfs.append(data)
    return pd.concat(dfs, ignore_index=True)

path = "/Users/theodorselimovic/Library/CloudStorage/OneDrive-Personal/Work/Ratio/email scraping/adresses/*.csv"

merged_csvs = csv_merger(path)

urls = merged_csvs[merged_csvs["website"]]
