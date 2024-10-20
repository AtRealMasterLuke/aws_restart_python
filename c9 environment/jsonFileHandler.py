import json

# function that will read the file
def readJsonFile(fileName):
    data=""
    # try/except block to make this function more reliable:
    try:
        # open the json file using the open function, and parse the file using json.load.
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
'''open returns a file handler to the files/insulin.json file.

json.load reads the JSON file and returns the content as a Python dictionary.'''


