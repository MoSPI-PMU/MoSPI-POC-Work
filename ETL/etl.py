
import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
    res = []
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary
        # and add it to data
     
        for row in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            # key = rows['State']
            
            data['State'] = row['State']
            data['Year'] = row['Year']
            
            dimList = []
            dim = {}
            dim['Name'] = 'Gender'
            dim['Value'] = row['Gender']
            dimList.append(dim)
            dim['Name'] = 'Locality'
            dim['Value'] = row['Locality']
            dimList.append(dim)
            
            indList = []
            ind = {}
            ind['Name'] = 'PS'
            ind['Value'] = row['PS']
            indList.append(ind)
            ind['Name'] = 'HSS'
            ind['Value'] = row['HSS']
            indList.append(ind)
            
            data['Dimensions'] = dimList
            data['Indicators'] = indList
            res.append(data)
            #res.append(row)


    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(res, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
csvFilePath = r'data.txt'
jsonFilePath = r'Names.json'
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)