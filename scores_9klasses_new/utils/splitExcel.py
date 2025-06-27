import pandas as pd
import os

folder_path = "data"

excel_files = [file for file in os.listdir(folder_path) if file.endswith(('.xlsx', '.xls'))]


dfs = []

for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_excel("data/Scores_AZ.xlsx", index=False)