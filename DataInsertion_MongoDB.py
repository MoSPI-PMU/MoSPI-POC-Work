import pymongo
import pandas as pd
import pprint
mongo_uri = "mongodb://localhost:27017/"  
client = pymongo.MongoClient(mongo_uri)
read_file = pd.read_excel("C:\\Users\\FJ795RQ\\Downloads\\Number of Schools by School Management and School Category_Report type - National_21.xlsx")
data = pd.DataFrame(pd.read_excel("C:\\Users\\FJ795RQ\\Downloads\\Number of Schools by School Management and School Category_Report type - National_21.xlsx",header=3))
db = client['EData']
collection = db['ED1']
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
# Insert collection
collection.insert_many(data_dict)
