#Bestellen:

#welkom bij Mc Donlads
print('\nWelkom bij Mc Donalds\nLaten we beginnen met uw bestelling:')

#Hier opeten of meenemen?

correct_input = False

while correct_input == False:
  eet_locatie_str = input('\nWilt u de bestellking meenemen of hier opeten?\n')
  eet_locatie = eet_locatie_str.upper()

  print(eet_locatie)

  if 'MEENEMEN' in eet_locatie:
    meenemen = True
    print(f'U wilt de bestelling meenemen: {eet_locatie}')