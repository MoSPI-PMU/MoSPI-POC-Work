index.js

Main.js
    Render:
        - Static filters (State, Year)
        - Dimensions filters (Dimension Names - 1D array, Values per object - 2D array)
        - Data
    Hooks:
        - useEffect - Initialize all dropdown values once. Populate the data
        - useEffect - Track changes to state and year filters and filter the data
        - filter_   - Lift state to Parent from the filter section to populate the filtered Lists

    filterDimensions: Refer below
                      
Filter.js
    - Renders all the filters taking the data and filterName from the parent component
    - filter_ callback to parent to lift the stateup

DimensionsRender.js
    - All render component need to be seperate functional components (child) otherwise the state is messed up

Dimensions.js
    - Create 1D List of Dimensions headers (names)
    - Create 2D filter of the values of the dimensions per object 
    - 'NA' where dimension not present for the object

Card.js
    - Display the data

* filterDimensions()
* 1. Loop through the static filtered items for each object
* 
* 2. Dimension objects
* [ { 'NFHS Survey Number' : 'NHFS5' },
*   { 'Residence type' : 'Urban' }, 
*   { 'Gender' : 'Male' }]
*
* 3. Dimensions Headers
*    ['NFHS Survey Number', 'Residence type', 'Gender'] 
* 
* 4. Dimension List
* [['NHFS5'],
*  ['Urban'],
*  ['Male']]
* 
* [['NHFS5']]
* 
* [[],
*  [],
*  ['Male']]
* 
* [['NHFS5'],
*  [],
*  ['Male', 'Female']]
* 
* [['NHFS5'],
*  [],
*  ['Male', 'NA']]
* 
* 

