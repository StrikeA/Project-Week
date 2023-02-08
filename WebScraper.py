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

team1 = teams[0].contents
team2 = teams[1].contents
team1_text = team1[0]
team2_text = team2[0]
strT1 = str(team1_text)
strT2 = str(team2_text)
team1_text_text = strT1[8:11]
team2_text_text = strT2[8:11]

# print(team1_text_text)
# print(team2_text_text)

print(players)
for i in range(len(players)):
    print(i)
    STRplayer = str(players[i])
    player_name = STRplayer.
    link = STRplayer[9:34]
    print(link)
    print()
    print(STRplayer)

