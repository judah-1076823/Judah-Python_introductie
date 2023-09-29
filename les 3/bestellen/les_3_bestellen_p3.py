#Bestellen
hier_eten = False
aborted = False

#Welkom bij Mc Donalds
print('\nWelkom bij Mc Donlads\nLaten we beginnen met uw bestelling:')
#hier eten of meenemen
vraag1_str = input('\nWilt u de bestelling hier opeten of meenemen?\n')
vraag1 = vraag1_str.upper()

if vraag1 == 'MEENEMEN':
    hier_eten = False
elif vraag1 == 'HIER ETEN' or 'HIER OPETEN':
    hier_eten = True
else:
    aborted = True

print(f'Hier eten: {hier_eten}')


vraag2_str = input('\nWilt u een burger bestellen? [ja/nee]\n')
vraag2 = vraag2_str.upper()

if vraag2 == 'JA':
    print('Welke burger wilt u?\n- Hamburger\n- Cheese burger\n- Big Mac\n- Quarter Pounder')
    vraag3_str = input('')
    vraag3 = vraag3_str.upper()

    if vraag3 == 'QUARTER POUNDER':
        kaas_str = input('Wilt u kaas op de bureger? [ja/nee]\n')
        kaas = kaas_str.upper()

        if kaas == 'NEE':
            print(f'+ 1x {vraag3}[zonder kaas]')
        elif kaas == 'JA':
            print(f'+ 1x {vraag3}')
        else:
            aborted = True

    elif vraag3 == 'HAMBURGER' or 'CHEESE BURGER' or 'BIG MAC':
        print(f'+ 1x {vraag3}')

    else:
        aborted = True

elif vraag2 != 'NEE':
    aborted = True


if aborted:
    print('Ongeldige invoer, begin opnieuw.')