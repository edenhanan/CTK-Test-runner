
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

class Functions():
    def __init__(self):
        pass

    def open_excel_or_csv_file_path():
        root = Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        filename = askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")], initialdir=os.getcwd(), title="Select Excel or CSV File")
        return filename
    
    def pandas_read_csv_or_excel(file_path):
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        return df