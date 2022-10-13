import pandas as pd
import json as j
from pprint import pprint

def education_formatter(file_downloaded, year, state):
    
    read_file = pd.read_excel(file_downloaded, header=3)
    df = pd.DataFrame(read_file)
    # Logic to add year and state column to each row
    df.insert(0,"Academic Year",year)
    df.insert(1,"State Name",state)   

    df = df.melt(['Academic Year','State Name','School Management'], var_name='School Type', value_name='Value')

    #df = df.groupby('School Management').agg({'column2': lambda x: list(x)})

    df_json = (df.groupby(['Academic Year','State Name','School Management'])
            .apply(lambda x: x[['School Type','Value']].to_dict('records'))
            .reset_index()
            .rename(columns={0: 'School'})
            .to_json(orient='records'))
    return df_json
   