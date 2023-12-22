"""CTK-test_runner.py: Run tests from excel file.
version: 0.0"""
# import customtkinter as ctk
import pandas as pd
import os
import sys




# Load the CSV file
df_path = r'C:\Users\edenh\PycharmProjects\CTK-Test-runner\test-scripts-example.csv'

def process_csv(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Initialize an empty dictionary to hold the tables
    tables = {}
    tables_info = {}
    infocolumns = []
    # Initialize an empty DataFrame to hold the current table
    current_table = pd.DataFrame()

    # Iterate over the DataFrame rows
    for _, row in df.iterrows():
        # Check if the current row has information in columns 1, 2, and 3
        if pd.notna(row['ID']) and pd.notna(row['Work Item Type']) and pd.notna(row['Title']):
            # If it does, start a new table and add the current row to it
            if not current_table.empty:
                current_table['Test Step'] = current_table['Test Step'].fillna(0).astype(int)
                first_row = current_table.iloc[0].dropna().tolist()
                first_row[0] = int(first_row[0])
                first_row.remove(0)
                tables_info[first_row[0]] = first_row
                tables[first_row[0]] = current_table[1:]
            current_table = pd.DataFrame([row])
        else:
            # If it doesn't, add the current row to the current table
            current_table = current_table._append(row)
    if infocolumns.__len__() == 0:
        infocolumns = list(current_table.columns)
        infocolumns.remove('Test Step')
        infocolumns.remove('Step Action')
        infocolumns.remove('Step Expected')
        tables_info['columns'] = infocolumns

    if not current_table.empty:
        # Convert 'ID' and 'Test Step' columns to int
        # current_table['ID'] = current_table['ID'].astype(int)
        current_table['Test Step'] = current_table['Test Step'].fillna(0).astype(int)
    return tables_info, tables
# def process_firstrow(first_row: list, tables_info=None):
#     for i in first_row:
#         if i ==


   # tables_info['ID'] = first_row
   #
   #  return tables
    # Now, 'tables'


tabels_info, tabels = process_csv(df_path)
print(tabels, tabels_info)
