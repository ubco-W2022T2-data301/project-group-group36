import pandas as pd



def dataset_processing(url_or_path_to_csv_file, wrangling_method):
    '''
    This functions wrangles the dataset into a more convinient form during data analysis for the relationship between weekly sales, Holidays, WoW changes etc.
    Input path or url as first argument, wrangling method as second argument.
    '''
    
    MFdf1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .copy().drop(['Store', 'Temperature','Fuel_Price','CPI','Unemployment'], axis=1)
        .assign(Date=pd.to_datetime(pd.read_csv(url_or_path_to_csv_file)['Date'], dayfirst=True, yearfirst=False))    
        .groupby('Date').mean().round()
        .sort_values(by=['Date']).reset_index()
        .reset_index()
        .rename(columns={'index': 'Week#'})
        .assign(Previous_Week_Sales=lambda x: x['Weekly_Sales'].shift(1))
        .assign(WoW_Changes=lambda x: (x['Weekly_Sales'] - x['Previous_Week_Sales']) / x['Previous_Week_Sales'])
        .assign(WoW_Changes=lambda x: x['WoW_Changes'].apply(lambda x: f"{x*100:.2f}%"))
    )
    
    MFdf2 = (MFdf1
        .sort_values(by='Weekly_Sales', ascending=False)
        .reset_index().copy().drop(['index'], axis=1)
        .astype({'Week#': str})
    )
    
    if wrangling_method == 'by week':
        return MFdf1
    elif wrangling_method == 'by sales':
        return MFdf2
    else:
        print('Wrangling method input incorrect, try "by week" or "by sales".') 
    