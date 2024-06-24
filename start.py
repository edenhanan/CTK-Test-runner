"""CTK-test_runner.py: Run tests from excel file.
version: 0.0"""
# import customtkinter as ctk
import pandas as pd
import os
import sys
import credentials as cr


df_path = cr.example_path


# new comment
def process_csv(file_path):
    df = pd.read_csv(file_path)

    tables = {}
    tables_info = {}
    infocolumns = []
    current_table = pd.DataFrame()

    for _, row in df.iterrows():
        if pd.notna(row['ID']) and pd.notna(row['Work Item Type']) and pd.notna(row['Title']):
            if not current_table.empty:
                current_table['Test Step'] = current_table['Test Step'].fillna(0).astype(int)
                first_row = current_table.iloc[0].dropna().tolist()
                first_row[0] = int(first_row[0])
                first_row.remove(0)
                tables_info[first_row[0]] = first_row
                tables[first_row[0]] = current_table[1:]
            current_table = pd.DataFrame([row])
        else:
            current_table = current_table._append(row)
    if infocolumns.__len__() == 0:
        infocolumns = list(current_table.columns)
        infocolumns.remove('Test Step')
        infocolumns.remove('Step Action')
        infocolumns.remove('Step Expected')
        tables_info['columns'] = infocolumns

    if not current_table.empty:
        current_table['Test Step'] = current_table['Test Step'].fillna(0).astype(int)
    return tables_info, tables


tabels_info, tabels = process_csv(df_path)
print(tabels, tabels_info)
