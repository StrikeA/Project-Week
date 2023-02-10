from bs4 import BeautifulSoup
import requests

# Away_team = input("Input team abbreviation: ")
Away_team = "TOR"
url = "https://www.basketball-reference.com/boxscores/202202030TOR.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

Inactive_Players = doc.find_all(text="Inactive: ")

parent = Inactive_Players[0].parent
parents = parent.parent
players = parents.find_all("a")
parents = str(parents)

teams = parents.split(sep=Away_team)
T1_players = teams[0]
T2_players = teams[1]

T1_link = T1_players.split(sep='"')

print(T1_link)
print(T2_players)

for i in range(len(players)):
    print(i)

    '''
    STRplayer = str(players[i])
    link = STRplayer.split(sep='"')
    link = link[1]
    players_names = STRplayer.split(sep=">")
    players_names = players_names[1]
    players_names = players_names[:-3]

    player_url = f"https://www.basketball-reference.com{link}"

    result1 = requests.get(player_url)
    doc1 = BeautifulSoup(result1.text, "html.parser")
    '''
