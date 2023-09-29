#abort
def aborted():
    print('\nOngeldige invoer!')
    exit()

#print burger order
def print_burger_order():
    print(f'\n+ 1x {burger_keuze}')

#print welkom
print('\nWelkom bij Mc Donalds\nLaten we beginnen met uw bestelling:')

#hier eten of meenemen
waar_eten_str = input('\nWilt u de bestelling hier eten of meenemen? (hier/meenemen)\n')
waar_eten = waar_eten_str.upper()

#if hier
if waar_eten == 'HIER':
    hier_eten = True
# if meenemen
elif waar_eten == 'MEENEMEN':
    hier_eten = False
else:
    aborted()

#Burger ja/nee
vraag_burger_str = input('\nWilt u een burger bestellen? (ja/nee)\n')
vraag_burger = vraag_burger_str.upper()

# nee
if vraag_burger == 'NEE':
    geen_burger = True
    burger_keuze = 'GEEN BURGER'
    print(f'\nU hebt gekozen voor {burger_keuze}')

# ja
elif vraag_burger =='JA':
    geen_burger = False
    # Welke burger wilt u
    print('\nWelke burger wilt u?:\n- Hamburger\n- Cheese burger\n- Big Mac\n- Quarter Pounder')
    burger_keuze_str = input('\nUw keuze: ')
    burger_keuze = burger_keuze_str.upper()
    
    # QUARTER POUNDER met of zonder kaas
    if burger_keuze == 'QUARTER POUNDER':
        kaas_str = input('Wilt u kaas op de burger? (ja/nee)\n')
        kaas = kaas_str.lower()
        if kaas == 'ja':
            print_burger_order()
        elif kaas == 'nee':
            burger_keuze = 'QUARTER POUNDER (zonder kaas)'
            print(f'\n+ 1x {burger_keuze}')
    # geldige input
    elif burger_keuze == 'HAMBURGER' or 'CHEESE BURGER' or 'BIG MAC':
        print_burger_order()
    else:
        aborted()
    
else:
    aborted()

# Drankje ja/nee
vraag_drankje_str = input('\nWilt u een drankje bestellen? (ja/nee)\n')
vraag_drankje = vraag_drankje_str.upper()

# nee
if vraag_drankje == 'NEE':
    geen_drankje = True
    drank_keuze = 'GEEN DRANKJE'
    print(f'\nU hebt gekozen voor {drank_keuze}')

# ja
elif vraag_drankje == 'JA':
    geen_drankje = False
    
    def print_drank_order():
        print(f'\n+ 1x {drank_keuze}')
    
    #Warm of koud
    warm_koud_str = input('\nWilt u een warm of koud drankje? (warm/koud)\n')
    warm_koud = warm_koud_str.upper()
    
    #warm
    if warm_koud == 'WARM':
        print('\nWelke zou u willen bestellen?:\n- Koffie\n- Cappucino\n- Thee\n- Chocomelk')
        drank_keuze_str = input('\nUw keuze: ')
        drank_keuze = drank_keuze_str.upper()
        

        if drank_keuze == 'KOFFIE' or 'CAPPUCINO' or 'THEE' or 'CHOCOMELK':
            print_drank_order()
        else:
            aborted()
        
    #koud
    elif warm_koud == 'KOUD':
        print('Welke zou u willen bestellen?:\n- Coca Cola\n- Cola Zero\n- 7up\n- Fanta\n- Fristi')
        drank_keuze_str = input('\nUw keuze: ')
        drank_keuze = drank_keuze_str.upper()
        
        if drank_keuze == 'COLA':
            print(f'\n+ 1x COCA {drank_keuze}')
        elif drank_keuze == 'COCA COLA' or 'COLA ZERO' or 'FRISTI' or '7UP' or 'FANTA':
            print_drank_order()
        else:
            aborted()

        
    else:
        aborted()

else:
    aborted()

line_chr = '_'
line = line_chr * 40

if geen_burger == False or geen_drankje == False:
    print(line)
    print(f'Uw bestelling:\n1x {burger_keuze}\n1x {drank_keuze}')


if geen_burger == True and geen_drankje == True:
    print(line)
    print(f'\nU hebt gekozen voor {drank_keuze} en {burger_keuze}. Er is dus niets besteld!\nProbeer het opnieuw of vindt een medewerker voor hulp.')
    exit()
elif hier_eten == True:
    print('\nBedankt voor uw bestelling en eetsmakelijk in ons restaurant.')
    exit()
elif hier_eten == False:
    print('\nBedankt voor uw bestelling. Goede reis en eet smakelijk.')
    exit()