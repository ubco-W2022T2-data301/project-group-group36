import pandas as pd
import math

def load_and_process(file_path):
    fhdf = (
        pd.read_csv(file_path)
          .rename(columns={'CPI': 'inflation'})
          .assign(avg_sales=lambda x: x.groupby(['inflation', 'Temperature'])['Weekly_Sales'].transform('mean'))
          .assign(Temperature_C=lambda x: round((x['Temperature'] - 32) * 5/9))
          .assign(avg_sales_ceil=lambda x: x['avg_sales'].apply(lambda y: math.ceil(y)))
          .groupby(['Temperature_C', 'inflation'])
          .agg({'avg_sales_ceil': 'mean'})
          .reset_index()
    )
    return fhdf
