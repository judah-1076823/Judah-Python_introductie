#Lijn om het begin aan te duiden
line_character = '_'
line = line_character * 80
print(line + '\n')

#vraag de user voor het netwerktype & convert naar caps
netwerk_keuze = input('Hoe wil je verbinden met het internet? [via 4G, 5G of open Wifi]\n')
netwerk = netwerk_keuze.upper()

#Laat zien dat de verbing is gemakt
if netwerk == '4G':
  print(f'U bent verbonden met het internet via {netwerk}.')
elif netwerk == '5G':
  print(f'U bent verbonden met het internet via {netwerk}.')
#wijs de user op dat het een open netwerk is en vraag om door teb gaan
elif netwerk == 'OPEN WIFI':
  print('U hebt voor de open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.')
  antwoord_str = input('Wilt u nog steeds verbinden via "open wifi"? [ja/nee]')
  antwoord = antwoord_str.upper()
  
  if antwoord == 'JA':
    print(f'U bent verbonden met het internet via {netwerk_keuze}.')
  elif antwoord == 'NEE':
    print('U bent niet verbonden!')

#Als de input niet wordt herkend
else:
  print('Onbekende invoer, er wordt geen verbinding tot stand gebracht.')