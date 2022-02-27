import http.client
import json

def getMatches(date):
    connection = http.client.HTTPConnection('api.football-data.org')
    #TODO put token in separate local file
    headers = {'X-Auth-Token': '6b273e17d1f343a4b4d6ceb63d27775d'}
    # connection.request('GET', '/v2/competitions/PL/dateFrom?2021-02-26&dateTo?2021-02-27', None, headers )
    getstring = '/v2/matches/?dateFrom=' + date + '&dateTo=' + date + '&competitions=2021'
    connection.request('GET', getstring, None, headers)
    # connection.request('GET', '/v2/competitions/PL', None, headers)
    response = json.loads(connection.getresponse().read().decode())

    # print (response)
    matchlist = response['matches']
    for x in matchlist:
        print("Home : " + x['homeTeam']['name'] + " and Away: " + x['awayTeam']['name'] + " at: " + x['utcDate'])

def getTeams():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '6b273e17d1f343a4b4d6ceb63d27775d'}
    # connection.request('GET', '/v2/competitions/PL/dateFrom?2021-02-26&dateTo?2021-02-27', None, headers )
    getstring = '/v2/competitions/PL/teams'
    connection.request('GET', getstring, None, headers)
    response = json.loads(connection.getresponse().read().decode())

    teamlist = response['teams']
    # teams = {}
    for x in teamlist:
        print(x['name'])

if __name__ == '__main__':
    getTeams()
    getMatches('2022-02-26')