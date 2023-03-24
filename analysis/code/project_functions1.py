import pandas as pd
import numpy as np

def load_and_process(path_to_csv_file):
    
    data = pd.read_csv(path_to_csv_file)

    KBdf_chain1 = pd.DataFrame(data) \
    .drop(['Holiday_Flag','Temperature','CPI','Fuel_Price','Unemployment', 'Store'], axis=1) \
    .assign(Weekly_Sales_Rate_of_Change = (data['Weekly_Sales'].pct_change(periods=2)))\
    .groupby('Date').mean() \
    .reset_index()


    KBdf_chain1

    return KBdf_chain1