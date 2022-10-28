import pandas as pd
import json as j
from pprint import pprint    
read_file = pd.read_excel("C:\\Users\\FJ795RQ\\Downloads\\population.xlsx")
df = pd.DataFrame(read_file)
#print (df)

df = df.melt(['State Code','State','Census Year'], var_name='Population', value_name='Value')
#df = df.groupby('School Management').agg({'column2': lambda x: list(x)})
df_json = (df.groupby(['State Code','State','Census Year'])
            .apply(lambda x: x[['Population','Value']].to_dict('records'))
            .reset_index()
            .rename(columns={0: 'Population'})
            .to_json(orient='records'))
print(df_json)
# Upload result_json in MongoDB
import pymongo
from pymongo import MongoClient
mongo_uri = "mongodb://localhost:27017/"  
client = pymongo.MongoClient(mongo_uri)
db = client['Government']
collection = db['Population Census']
import json
#print(result_json)
result_List = json.loads(df_json)    
if isinstance(result_List, list):
 collection.insert_many(result_List)
else:
 collection.insert_one(result_List)
print("data inserted")