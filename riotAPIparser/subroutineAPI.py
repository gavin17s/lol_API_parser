import codecs
import json
import urllib.request

def getChampionName(championID, uRegion, uAPI):

	with open("data/championDict.json") as jsonFileRead:
		championDict = json.load(jsonFileRead)

		championIDStr = str(championID)

	if championIDStr not in championDict:
		apiURL = "https://"+uRegion+".api.pvp.net/api/lol/static-data/"+uRegion+"/v1.2/champion/"+str(championID)+"?dataById=true&api_key="+uAPI
		reader = codecs.getreader("utf-8")
		nameResponse = urllib.request.urlopen(apiURL)
		nameResponse = json.load(reader(nameResponse))

		championDict[championIDStr] = nameResponse["name"]

		with open("data/championDict.json", "w") as jsonFileWrite:
			json.dump(championDict, jsonFileWrite)

	return championDict[championIDStr]

def requestPlayerData(pName, uRegion, uAPI):

	apiURL = "https://"+uRegion+".api.pvp.net/api/lol/"+uRegion+"/v1.4/summoner/by-name/"+pName+"?api_key="+uAPI

	reader = codecs.getreader("utf-8")
	nameResponse = urllib.request.urlopen(apiURL)
	nameResponse = json.load(reader(nameResponse))

	return nameResponse

def requestPlayerRank(pID, uRegion, uAPI):

	apiURL = "https://"+uRegion+".api.pvp.net/api/lol/"+uRegion+"/v2.5/league/by-summoner/"+pID+"/entry?api_key="+uAPI

	reader = codecs.getreader("utf-8")
	rankResponse = urllib.request.urlopen(apiURL)
	rankResponse = json.load(reader(rankResponse))

	return rankResponse

def displayPlayerData(pID, pName, pRank):

	print("\nPlayer {} is {} {} with {} LP.\n".format(pName, pRank[pID][0]['tier'], pRank[pID][0]['entries'][0]['division'], pRank[pID][0]['entries'][0]['leaguePoints']))

def currentGame(pID, uRegion, uAPI):

    platformID = {"br":"BR1", "eune":"EUN1", "euw":"EUW1", "kr":"KR", "lan":"LA1", "las":"LA2", "na":"NA1", "oce":"OC1", "tr":"TR1", "ru":"RU"}
    apiURL = "https://"+uRegion+".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/"+platformID[uRegion]+"/"+pID+"?api_key="+uAPI

    reader = codecs.getreader("utf-8")
    try:
        gameResponse = urllib.request.urlopen(apiURL)
        gameResponse = json.load(reader(gameResponse))
    except:
        return False
        
    return gameResponse

def displayCurrentGame(gameData, uRegion, uAPI):

	with open("data/mapType.json") as jsonFileRead:
			mapType = json.load(jsonFileRead)

	with open("data/queueType.json") as jsonFileRead:
			queueType = json.load(jsonFileRead)

	if gameData == False:
		print("Player currently not ingame.")
	else:
		mapStr = str(gameData["mapId"])
		queueStr = str(gameData["gameQueueConfigId"])
		print("Player currently ingame.\n\nMap: {}\nGame mode: {}\n".format(mapType[mapStr], queueType[queueStr]))
		if gameData["gameQueueConfigId"] == 14 or gameData["gameQueueConfigId"] == 4 or gameData["gameQueueConfigId"] == 41 or gameData["gameQueueConfigId"] == 42:
			print("Banned champions:")
			for championB in gameData["bannedChampions"]:
				print(getChampionName(championB["championId"], uRegion, uAPI))

		print("\nBlue side:")
		for summ in gameData["participants"]:
			if summ["teamId"] == 100:
				print(summ["summonerName"], "playing", getChampionName(summ["championId"], uRegion, uAPI))
		print("\nRed side:")
		for summ in gameData["participants"]:
			if summ["teamId"] == 200:
				print(summ["summonerName"], "playing", getChampionName(summ["championId"], uRegion, uAPI))
