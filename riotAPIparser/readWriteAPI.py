import json

def loadAPIKey():
    with open("data/key/apiKey.json") as jsonFileRead:
        apiKey = json.load(jsonFileRead)
        
    return apiKey["1"]
    
def writeAPIKey(userKey):
    with open("data/key/apiKey.json") as jsonFileRead:
        apiKey = json.load(jsonFileRead)
        apiKey["1"] = userKey
    
    with open("data/key/apiKey.json", "w") as jsonFileWrite:
            json.dump(apiKey, jsonFileWrite)
