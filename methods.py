## Arquivo com todos os método utilizados para extração de dados e criação em banco
import requests
## Get summoner puuid and encrypted_puuid from a summoner_name (BR1)
def get_puuid(api_key, summoner_name):
    
    url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
    'X-Riot-Token':api_key
    }
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['puuid'], data['id']  # 'id' is the encrypted PUUID
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None

## List of matchs 20 matchs the summoner have played
def get_matches(api_key, puuid):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None

## retorna apenas partidas ranked 5x5
def get_ranked_matches(api_key, puuid):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&type=ranked&start=0&count=20"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None    
    
## Get match info from a specific matchId    
def get_match_info(api_key, matchid):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchid}"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None
    
## Get patch fromgameVersion
def get_game_patch(gameVersion):
    patch = float(gameVersion.split('.',2)[0] + '.' + gameVersion.split('.',2)[1])
    return patch

## List of Challenger player in Ranked SoloQ
def get_challengers_solo(api_key):
    url = f"https://br1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None

    
    
## List of all league entries - Ranked Solo
def get_master_solo(api_key, division, tier):
    url = f"https://br1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{division}/{tier}?page=1"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None

## Return the list of match related infos, from a match_info file. To populate matchs_df.
def matchs_df_populate(match):
    match_info =[]
    
    matchid = match['metadata']['matchId']
    dataVersion = match['metadata']['dataVersion']
    participantpuuid0 = match['metadata']['participants'][0]
    participantpuuid1 = match['metadata']['participants'][1]
    participantpuuid2 = match['metadata']['participants'][2]
    participantpuuid3 = match['metadata']['participants'][3]
    participantpuuid4 = match['metadata']['participants'][4]
    participantpuuid5 = match['metadata']['participants'][5]
    participantpuuid6 = match['metadata']['participants'][6]
    participantpuuid7 = match['metadata']['participants'][7]
    participantpuuid8 = match['metadata']['participants'][8]
    participantpuuid9 = match['metadata']['participants'][9]
    gameDuration = match['info']['gameDuration']
    gameCreation = match['info']['gameCreation']
    gameVersion = get_game_patch(match['info']['gameVersion'])
    mapId = match['info']['mapId']
    gameMode = match['info']['gameMode']
    gameType = match['info']['gameType']
    
    match_info.extend([matchid, dataVersion, participantpuuid0, participantpuuid1,participantpuuid2, participantpuuid3,
                       participantpuuid4, participantpuuid5, participantpuuid6,participantpuuid7, participantpuuid8,
                       participantpuuid9,gameDuration,gameCreation,gameVersion,mapId,gameMode,gameType])
     
    
    return match_info


## Return the list of player related infos, from a match_info file. To populate player_stats_df.
def player_stats_populate(match,participant,items_dict):
    player_stats = []
    
    matchid = match['metadata']['matchId']
    puuid = participant['puuid']
    participantId = participant['participantId']
    teamId = participant['teamId']
    championId = participant['championId']

    
    # Extract additional player stats
    lane = participant['lane']
    role = participant['role']
    individualPosition = participant['individualPosition']
    teamPosition = participant['teamPosition']
    timePlayed = participant['timePlayed']
    championName = participant['championName']
    championTransform = participant['championTransform']
    champExperience = participant['champExperience']
    champLevel = participant['champLevel']
    win = participant['win']
    kills = participant['kills']
    firstBloodKill = participant['firstBloodKill']
    firstBloodAssist = participant['firstBloodAssist']
    deaths = participant['deaths']
    totalTimeSpentDead = participant['totalTimeSpentDead']
    longestTimeSpentLiving = participant['longestTimeSpentLiving']
    assists = participant['assists']
    killingSprees = participant['killingSprees']
    largestKillingSpree = participant['largestKillingSpree']
    doubleKills = participant['doubleKills']
    tripleKills = participant['tripleKills']
    quadraKills = participant['quadraKills']
    pentaKills = participant['pentaKills']
    largestMultiKill = participant['largestMultiKill']
    unrealKills = participant['unrealKills']
    baronKills = participant['baronKills']
    dragonKills = participant['dragonKills']
    turretKills = participant['turretKills']

    # Extract additional player stats (continued)
    firstTowerKill = participant['firstTowerKill']
    firstTowerAssist = participant['firstTowerAssist']
    turretTakedowns = participant['turretTakedowns']
    turretsLost = participant['turretsLost']
    inhibitorKills = participant['inhibitorKills']
    inhibitorTakedowns = participant['inhibitorTakedowns']
    inhibitorsLost = participant['inhibitorsLost']
    nexusKills = participant['nexusKills']
    nexusTakedowns = participant['nexusTakedowns']
    nexusLost = participant['nexusLost']
    objectivesStolen = participant['objectivesStolen']
    objectivesStolenAssists = participant['objectivesStolenAssists']
    totalMinionsKilled = participant['totalMinionsKilled']
    neutralMinionsKilled = participant['neutralMinionsKilled']
    totalAllyJungleMinionsKilled = participant['totalAllyJungleMinionsKilled']
    totalEnemyJungleMinionsKilled = participant['totalEnemyJungleMinionsKilled']
    goldEarned = participant['goldEarned']
    goldSpent = participant['goldSpent']
    bountyLevel = participant['bountyLevel']
    item0 = participant['item0']
    item0Name = items_dict.get(participant['item0'])
    item1 = participant['item1']
    item1Name = items_dict.get(participant['item1'])                                                
    item2 = participant['item2']
    item2Name = items_dict.get(participant['item2'])                                                
    item3 = participant['item3']
    item3Name = items_dict.get(participant['item3'])                                                
    item4 = participant['item4']
    item4Name = items_dict.get(participant['item4'])                                                
    item5 = participant['item5']
    item5Name = items_dict.get(participant['item5'])                                                
    item6 = participant['item6']
    item6Name = items_dict.get(participant['item6'])                                                
    itemsPurchased = participant['itemsPurchased']
    consumablesPurchased = participant['consumablesPurchased']
    spell1Casts = participant['spell1Casts']
    spell2Casts = participant['spell2Casts']
    spell3Casts = participant['spell3Casts']
    spell4Casts = participant['spell4Casts']
    summoner1Casts = participant['summoner1Casts']
    summoner1Id = participant['summoner1Id']
    summoner2Casts = participant['summoner2Casts']
    summoner2Id = participant['summoner2Id']
    damageDealtToBuildings = participant['damageDealtToBuildings']
    damageDealtToObjectives = participant['damageDealtToObjectives']
    damageDealtToTurrets = participant['damageDealtToTurrets']

    # Extracting additional player stats (continued)
    damageSelfMitigated = participant['damageSelfMitigated']
    magicDamageDealt = participant['magicDamageDealt']
    magicDamageDealtToChampions = participant['magicDamageDealtToChampions']
    magicDamageTaken = participant['magicDamageTaken']
    physicalDamageDealt = participant['physicalDamageDealt']
    physicalDamageDealtToChampions = participant['physicalDamageDealtToChampions']
    physicalDamageTaken = participant['physicalDamageTaken']
    trueDamageDealt = participant['trueDamageDealt']
    trueDamageDealtToChampions = participant['trueDamageDealtToChampions']
    trueDamageTaken = participant['trueDamageTaken']
    totalDamageDealt = participant['totalDamageDealt']
    totalDamageDealtToChampions = participant['totalDamageDealtToChampions']
    largestCriticalStrike = participant['largestCriticalStrike']
    totalDamageShieldedOnTeammates = participant['totalDamageShieldedOnTeammates']
    totalDamageTaken = participant['totalDamageTaken']
    totalHeal = participant['totalHeal']
    totalHealsOnTeammates = participant['totalHealsOnTeammates']
    totalUnitsHealed = participant['totalUnitsHealed']
    timeCCingOthers = participant['timeCCingOthers']
    totalTimeCCDealt = participant['totalTimeCCDealt']
    detectorWardsPlaced = participant['detectorWardsPlaced']
    sightWardsBoughtInGame = participant['sightWardsBoughtInGame']
    visionScore = participant['visionScore']
    visionWardsBoughtInGame = participant['visionWardsBoughtInGame']
    wardsKilled = participant['wardsKilled']
    wardsPlaced = participant['wardsPlaced']
    gameEndedInEarlySurrender = participant['gameEndedInEarlySurrender']
    gameEndedInSurrender = participant['gameEndedInSurrender']
    teamEarlySurrendered = participant['teamEarlySurrendered']
    placement = participant['placement']
    eligibleForProgression = participant['eligibleForProgression']
    subteamPlacement = participant['subteamPlacement']
    playerSubteamId = participant['playerSubteamId']

    # Append the extracted information to the player_stats list
    player_stats.extend([matchid,puuid,participantId,teamId,championId, lane, role, individualPosition, teamPosition, timePlayed, 
                       championName, championTransform, champExperience, champLevel,win, kills, firstBloodKill, firstBloodAssist,
                       deaths, totalTimeSpentDead,longestTimeSpentLiving, assists,killingSprees, largestKillingSpree, doubleKills,
                       tripleKills, quadraKills, pentaKills, largestMultiKill,unrealKills, baronKills, dragonKills, turretKills,
                       firstTowerKill, firstTowerAssist, turretTakedowns, turretsLost, inhibitorKills, inhibitorTakedowns,
                        inhibitorsLost, nexusKills, nexusTakedowns, nexusLost, objectivesStolen, objectivesStolenAssists,
                        totalMinionsKilled, neutralMinionsKilled, totalAllyJungleMinionsKilled, totalEnemyJungleMinionsKilled,
                        goldEarned, goldSpent, bountyLevel, item0,item0Name, item1,item1Name, item2,item2Name, item3, item3Name,
                       item4,item4Name, item5,item5Name, item6,item6Name, itemsPurchased,
                        consumablesPurchased, spell1Casts, spell2Casts, spell3Casts, spell4Casts, summoner1Casts, summoner1Id,
                        summoner2Casts, summoner2Id, damageDealtToBuildings, damageDealtToObjectives, damageDealtToTurrets,
                       damageSelfMitigated, magicDamageDealt, magicDamageDealtToChampions, magicDamageTaken,
                        physicalDamageDealt, physicalDamageDealtToChampions, physicalDamageTaken, trueDamageDealt,
                        trueDamageDealtToChampions, trueDamageTaken, totalDamageDealt, totalDamageDealtToChampions,
                        largestCriticalStrike, totalDamageShieldedOnTeammates, totalDamageTaken, totalHeal,
                        totalHealsOnTeammates, totalUnitsHealed, timeCCingOthers, totalTimeCCDealt, detectorWardsPlaced,
                        sightWardsBoughtInGame, visionScore, visionWardsBoughtInGame, wardsKilled, wardsPlaced,
                        gameEndedInEarlySurrender, gameEndedInSurrender, teamEarlySurrendered, placement,
                        eligibleForProgression, subteamPlacement, playerSubteamId])

    # Now, the player_stats list contains the extracted information for the additional items
    return player_stats

## Return a list o team data from a match info
def team_data_populate(match,team):
        team_info =[]
        
        matchid = match['metadata']['matchId']
        teamId = team['teamId']
        if teamId ==100:
            side = 'blue'
        else:
            side = 'red'
        win = team['win']
        firstBlood = team['objectives']['champion']['first']
        firstTower = team['objectives']['tower']['first']
        firstInhibitor = team['objectives']['inhibitor']['first']
        firstBaron = team['objectives']['baron']['first']
        firstDragon = team['objectives']['dragon']['first']
        firstHerald = team['objectives']['riftHerald']['first']
        championKills = team['objectives']['champion']['kills']
        towerKills = team['objectives']['tower']['kills']
        inhibitorKills = team['objectives']['inhibitor']['kills']
        baronKills =team['objectives']['baron']['kills']
        dragonKills = team['objectives']['dragon']['kills']
        riftHeraldKils = team['objectives']['riftHerald']['kills']
        
        team_info.extend([matchid, teamId, side, win, firstBlood,firstTower, firstInhibitor,firstBaron,firstDragon,
                         firstHerald,championKills,towerKills,inhibitorKills,baronKills,dragonKills,riftHeraldKils])
        return team_info
    