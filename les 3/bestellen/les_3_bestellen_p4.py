#Bestellen:
def aborted():
    print('Ongeldige invoer!')

hier_eten = True


#Welkom
print('\nWelkom bij Mc Donalds\nLaten we gaan beginnen met de bestelling:')

#Hier eten of meenemen
waar_eten_str = input('\nWilt u de bestelling hier opeten of meenemen?\n')
waar_eten = waar_eten_str.upper()

if 'MEENEMEN' in waar_eten:
    hier_eten = False
    print(f'U gaat de bestelling hier opeten: {hier_eten}')
elif 'HIER ETEN' or 'HIER OPETEN' in waar_eten:
    print(f'U gaat de bestelling hier opeten: {hier_eten}')
else:
    aborted()


#Burger
burger_str = input('\nWilt u een burger bestellen? [ja/nee]\n')
burger = burger_str.upper()
geen_burger = True

if burger == 'JA':
    geen_burger = False
    print('\nWelke burger zou u willen?\n- Hamburger\n- Cheese burger\n- Big Mac\n- Quarter Pounder\n')
    burger_keuze_str = input('Uw keuze: ')
    burger_keuze = burger_keuze_str.upper()
    print(burger_keuze)

    if burger_keuze == 'QUARTER POUNDER':
        kaas_str = input('Wilt u kaas op de burger? (ja/nee)\n')
        kaas = kaas_str.upper()
        if kaas == 'JA':
            print(f'\n+ 1x {burger_keuze}')
        elif kaas == 'NEE':
            print(f'\n+ 1x {burger_keuze} (zonder kaas)')
        else:
            aborted()

    elif burger_keuze == 'HAMBURGER' or 'CHEESEBURGER' or 'CHEESE BURGER' or 'BIG MAC' or 'BIGMAC':
        print(f'\n+ 1x {burger_keuze}')

    else:
        aborted()

elif burger == 'NEE':
    print('U heeft gekozen voor geen burger.')
    burger_keuze = 'GEEN BURGER'
else:
    aborted()


#Drankjes
vraag1_str = input('\nWilt u een drankje bestellen? (ja/nee)\n')
vraag1 = vraag1_str.upper()

if vraag1 == 'JA':
    warm_koud_str = input('\nZou u een warme of koude drank willen? (warm/koud)\n')
    warm_koud = warm_koud_str.upper()
    
    if warm_koud == 'KOUD':
        print('\nKies een drank:\n- Coca Cola\n- Cola Zero\n- 7up\n- Fanta\n- Fristi')
        drank_str = input('\nUw keuze: ')
        drank = drank_str.upper()
        if drank == 'COCA COLA' or 'COCACOLA' or 'COLA ZERO' or 'COLAZERO' or '7UP' or '7 UP' or 'FANTA' or 'Fristi':
            print(f'\n+ 1x {drank}')
        else:
            aborted()

    elif warm_koud == 'WARM':
        print('\nKies een drankje:\n- Koffie\n- Cappucino\n- Chocomelk')
        drank_str = input('\nUw keuze: ')
        drank = drank_str.upper()
        if drank == 'KOFFIE' or 'CAPPUCINO' or 'CHOCOMELK' or 'CHOCO MELK':
            print(f'\n+ 1x {drank}')

    else:
        aborted()

elif vraag1 == 'NEE':
    print('\nU heeft gekozen voor geen drankje.')
    drank = 'GEEN DRANKJE'
else:
    aborted()

if burger == 'NEE' and vraag1 == 'NEE':
    print('\nU heeft niets besteld.\nProbeer het opnieuw of vind een medewerker bij de balie voor hulp.')
elif hier_eten == False:
    print(f'UW BESTELLING:\n- {burger_keuze}\n- {drank}')
    print('\nBedankt vopor uw bestelling, goede reis en eet smakelijk.')
elif hier_eten == True:
    print(f'UW BESTELLING:\n- {burger_keuze}\n- {drank}')
    print('Bedankt voor uw bestelling en eet smakelijk in ons restaurant.')
else:
    aborted()