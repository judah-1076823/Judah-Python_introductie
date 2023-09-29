#Bestellen
def aborted():
    print('\nOngeldige invoer!')
    exit()

def welkom():
    print('\nWelkom bij Mc Donalds\nLaten we beginnen met uw bestelling:')

def vraag1(): #Hier eten of meenemen
    waar_eten_str = input('\nWilt u de bestelling hier eten of meenemen? (hier/meenemen)\n')
    waar_eten = waar_eten_str.upper()

    if waar_eten == 'HIER':
        hier_eten = True
        print(f'U wilt de bestelling hier eten: {hier_eten}')
    elif waar_eten == 'MEENEMEN':
        hier_eten = False
        print(f'U wilt de bestelling hier eten: {hier_eten}')
    else:
        aborted()

def vraag2(): #Burger ja/nee
    vraag_burger_str = input('\nWilt u een burger bestellen? (ja/nee)\n')
    vraag_burger = vraag_burger_str.upper()

    if vraag_burger == 'NEE':
        geen_burger = True
        burger_keuze = 'GEEN BURGER'
        print(f'\nU hebt gekozen voor {burger_keuze}')
    elif vraag_burger =='JA':
        geen_burger = False
        vraag2_1()
    else:
        aborted()
        
def vraag2_1(): #if 'ja' welke burger 
    def print_burger_order():
        print(f'\n+ 1x {burger_keuze}')

    print('\nWelke burger wilt u?:\n- Hamburger\n- Cheese burger\n- Big Mac\n- Quarter Pounder')
    burger_keuze_str = input('\nUw keuze: ')
    burger_keuze = burger_keuze_str.upper()
    
    #QUARTER POUNDER met of zonder kaas
    if burger_keuze == 'QUARTER POUNDER':
        kaas_str = input('Wilt u kaas op de burger? (ja/nee)\n')
        kaas = kaas_str.lower()
        if kaas == 'ja':
            print_burger_order()
        elif kaas == 'nee':
            print(f'\n+ 1x {burger_keuze} (zonder kaas)')

    elif burger_keuze == 'HAMBURGER' or 'CHEESE BURGER' or 'BIG MAC':
        print_burger_order()
    else:
        aborted()

def vraag3(): #Drankje ja/nee
    vraag_drankje_str = input('\nWilt u een drankje bestellen? (ja/nee)\n')
    vraag_drankje = vraag_drankje_str.upper()

    if vraag_drankje == 'NEE':
        geen_drankje = True
        drank_keuze = 'GEEN DRANKJE'
        print(f'\nU hebt gekozen voor {drank_keuze}')
    elif vraag_drankje == 'JA':
        geen_drankje = False
        vraag3_1()
    else:
        aborted()
    
def vraag3_1(): #if 'ja' welk warm of koud
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
        print(drank_keuze)

    else:
        aborted()

# def order_check():
#     if geen_burger == True and geen_drankje == True:
#     print(f'U hebt gekozen voor {burger_keuze} en {drank_keuze}. U hebt dus niets betseld!\nProbeer het opnieuw of vind een medewerker aan de balie voor hulp.')

#code
welkom()
vraag1() 
vraag2()
vraag3()
# order_check()
