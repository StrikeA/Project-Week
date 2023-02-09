from bs4 import BeautifulSoup
import requests

url = "https://www.basketball-reference.com/boxscores/202202030TOR.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

Inactive_Players = doc.find_all(text="Inactive: ")

parent = Inactive_Players[0].parent
parents = parent.parent
# print(parents)

players = parents.find_all("a")
teams = parents.find_all("span")
'''
team1 = teams[0].contents
team2 = teams[1].contents
team1_text = team1[0]
team2_text = team2[0]
strT1 = str(team1_text)
strT2 = str(team2_text)
team1_text_text = strT1[8:11]
team2_text_text = strT2[8:11]
'''


print(players)
for i in range(len(players)):
    print(i)
    STRplayer = str(players[i])
    link = STRplayer.split(sep='"')
    link = link[1]
    players_names = STRplayer.split(sep=">")
    players_names = players_names[1]
    '''
    print(link[1])
    print(players_names[:-3])
    print(STRplayer)
    '''
    player_url = f"https://www.basketball-reference.com{link}"

    result1 = requests.get(player_url)
    doc1 = BeautifulSoup(result1.text, "html.parser")

    
