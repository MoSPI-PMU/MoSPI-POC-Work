import pandas as pd
import json as j
from pprint import pprint    
read_file = pd.read_csv('C:\\Users\\FJ795RQ\\POC\\Health.csv',header=1)
df = pd.DataFrame(read_file)
#print (df)

df = df.melt(['Country','State lgd code','State','Year','Nfhs survey number ( nfhs - 4 or nfhs - 5 )','Residence type'], var_name='Health Indicator', value_name='Value')
#df = df.groupby('School Management').agg({'column2': lambda x: list(x)})
df_json = (df.groupby(['Country','State lgd code','State','Year','Nfhs survey number ( nfhs - 4 or nfhs - 5 )','Residence type'])
            .apply(lambda x: x[['Health Indicator','Value']].to_dict('records'))
            .reset_index()
            .rename(columns={0: 'Health Indicator'})
            .to_json(orient='records'))
print(df_json)
# Upload result_json in MongoDB
import pymongo
from pymongo import MongoClient
mongo_uri = "mongodb://localhost:27017/"  
client = pymongo.MongoClient(mongo_uri)
db = client['Government']
collection = db['Health']
import json
#print(result_json)
result_List = json.loads(df_json)    
if isinstance(result_List, list):
 collection.insert_many(result_List)
else:
 collection.insert_one(result_List)
print("data inserted")