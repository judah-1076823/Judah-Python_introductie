# LIST OF GAMES

# 'Player’s Unkno'wn Battle Ground (PUBG) 50 Million 2018'
# 'Snake',
# 'Fortnite Battle Royale 39 Million 2017'
# 'Apex Legends 50 Million (1 Month) 2019'
# 'Leauge of Legends (LOL) 27 Million 2009'
# 'Counter Strike; Global Offensive 32 Million 2014'
# 'Heartstone 29 Million 20120'
# 'Minecraft 91 Million 2011'
# 'DOTA 2 5 million 2015'
# 'The Division 2 N/A 2019'

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

# A
print('\nA:')
print(f'5] {game_list[4]}')

# B
print('\nB:')
lengte_dota = len(game_list[7])
print(f'De lengte van de tekst van de achtse game (DOTA) is {lengte_dota} characters.')

# C
print('\nC:')
lengte_game_list = len(game_list)
print(f'Er zitten {lengte_game_list} games in de lijst.')

# D
print('\nD:')
game_list.insert(1, 'Snake')
print(game_list)

# E
print('\nE:')
print(f'Helaas heeft de game {game_list[10]} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van de game {game_list[10]}.')
game_list.pop(10)

# F
print('\nF:')
game_list.pop(6)
game_list.insert(6, 'Heartstone 29 Million 2012')
print(game_list)