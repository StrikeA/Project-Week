minpg = float(input("How many minutes per game"))
wsper48 = float(input("How many wins per 48"))
teamsrsabs = float(input("WHat is the absolute value of team srs"))
if teamsrsabs < 1:
    teamsrsabs = 1

playervalue = (((minpg/48) * wsper48) * teamsrsabs)
print(playervalue)
print("if team srs is negative:")
print(playervalue + teamsrsabs)
print("if team srs is positive:")
print(teamsrsabs - playervalue)
