games = int(input("How many games did they play"))
ofe = int(input("of how many"))
minpg = float(input("How many minutes per game"))
wsper48 = float(input("How many wins per 48"))
teamsrsabs = float(input("What is the absolute value of team srs"))
teamsrsabs2 = teamsrsabs
if teamsrsabs < 1:
    teamsrsabs2 = 1

playervalue = ((((minpg/48) * wsper48) * teamsrsabs2)/(games/ofe))
print(playervalue)
print("if team srs is negative:")
print(-(playervalue + teamsrsabs))
print("if team srs is positive:")
print(teamsrsabs - playervalue)
