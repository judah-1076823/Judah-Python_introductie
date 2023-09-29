# 'Player’s Unknown Battle Ground (PUBG) 50 Million 2018', 
# 'snake'
# 'Fortnite Battle Royale 39 Million 2017', 
# 'Apex Legends 50 Million (1 Month) 2019', 
# 'Leauge of Legends (LOL) 27 Million 2009', 
# 'Counter Strike; Global Offensive 32 Million 2014', 
# 'Heartstone 29 Million 20120', 
# 'Minecraft 91 Million 2011', 
# 'DOTA 2 5 million 2015', 
# 'The Division 2 N/A 2019', 
# 'The Splatoon 2'


game_list = ['Player’s Unknown Battle Ground (PUBG) 50 Million 2018', 
'Fortnite Battle Royale 39 Million 2017', 
'Apex Legends 50 Million (1 Month) 2019', 
'Leauge of Legends (LOL) 27 Million 2009', 
'Counter Strike; Global Offensive 32 Million 2014', 
'Heartstone 29 Million 20120', 
'Minecraft 91 Million 2011', 
'DOTA 2 5 million 2015', 
'The Division 2 N/A 2019', 
'The Splatoon 2']


# a Geef de 5de game (Counter Strike) uit de lijst op het scherm weer met 5] ervoor.
print('\nA:')
print(f'5 {game_list[4]}')

# b Geef de lengte van de tekst van de 8ste game (DOTA) uit de lijst weer.
print('\nB:')
size_eight = len(game_list[7])
print(f'De lengte van de tekst van de 8e game (8: {game_list[7]}) is {size_eight} characters.')

#c Geef op het scherm weer met een volzin: "Er zitten [aantal games] games in 
print('\nC:')
game_amount = len(game_list)
print(f'Er zitten {game_amount} games in de lijst.')

#d De ranking moet worden aangepast want de game Snake blijkt een instant hit en komt binnen op de 2de plaats. Voeg de game Snake toe aan de lijst op de tweede plaats.
print('\nD:')
game_list.insert(1, 'Snake')
print(game_list)

#e Verwijder de game "The Splatoon" uit de lijst en geef de naam op het scherm weer zoals deze uit de lijst is gekomen in een volzin: "Helaas heeft de game [naam van de game] het niet gered om in de top 10 te blijven. We nemen waardig afscheid van [naam van de game]."
print('\nE:')
game_list.pop(10)
print(game_list)

# f Nadat de redactie de lijst had gezien, hebben ze de opmerking geplaatst dat er een fout zit in de tekst van de game "Heartstone". Het jaartal moet 2012 zin. Pas de tekst in de lijst aan met Python code.
print('\nF:')
game_list.pop(4)
print(game_list)