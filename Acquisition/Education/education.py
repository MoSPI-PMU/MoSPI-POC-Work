from education_scrapper import education_scrapper
from education_formatter import education_formatter
import glob

if __name__ == "__main__":
    
    year = '2020-21'
    state = 'Punjab'
    
    list_of_files_before_download = glob.glob('C:\\Users\\FJ795RQ\\POC\\Downloads\\*.xlsx')
    print("Before : ", list_of_files_before_download)
    education_scrapper(year, state)
    
    list_of_files_after_download = glob.glob('C:\\Users\\FJ795RQ\\POC\\Downloads\\*.xlsx')
    print("After :", list_of_files_after_download)
    newfile = list(set(list_of_files_after_download).difference(list_of_files_before_download))
    print("File downloaded :", newfile[0])
    file_downloaded = newfile[0]
    
    #file_downloaded = 'C:\\Users\\FJ795RQ\\POC\\Downloads\\Number of Schools by School Management and School Category_State Name _Haryana_21.xlsx'
    result_json = education_formatter(file_downloaded, year, state)
    
    
    # Upload result_json in MongoDB
    import pymongo
    from pymongo import MongoClient
    
    mongo_uri = "mongodb://localhost:27017/"  
    client = pymongo.MongoClient(mongo_uri)
    db = client['Government']
    collection = db['Education']
    
    import json
    #print(result_json)
    
    result_List = json.loads(result_json)
    
    if isinstance(result_List, list):
        collection.insert_many(result_List)
    else:
        collection.insert_one(result_List)
    print("data inserted")
