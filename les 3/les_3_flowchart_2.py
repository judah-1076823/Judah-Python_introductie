#Flowchart 2

print('\nShopping Cart\n')

#vraag voor de betaalmethode
payment_methode_str = input('Payment methode [online/offline]\n')
payment_methode = payment_methode_str.lower()


#als betaalmethode 'offline' is
if payment_methode == 'offline':
  print('\nPlace purchase order')

  #vraag of de gebruiker admin rechten heeft
  admin_user_str = input('Admin user? [yes/no]\n')
  admin_user = admin_user_str.lower()

  #als de gebruiker admin is
  if admin_user == 'yes':
    print('\nOrder Created Automatically')

  #als de gebruiker niet admin is
  elif admin_user == 'no':
    approval_rules_str = input('\n"Approval Rules" [rejected/approved]\n')
    approval_rules = approval_rules_str.upper()

    #vraag om de regels toe te staan
    if approval_rules == 'REJECTED':
      print('\nPurchase Order Rejected!')
    elif approval_rules == 'APPROVED':
      print('\nOrder Created Automatically')
    #als er geen gelidige input is
    else:
      print('Invalid input, choose \'rejected\' or \'approved\'')
  
  #als er geen gelidige input is
  else:
    print("Invalid input, choose 'yes' or 'no'")


#Als betaalmethode 'online' is
elif payment_methode == 'online':
  #vraag of de gebruiker admin rechten heeft
  admin_user_str = input('\nAdmin user? [yes/no]\n')
  admin_user = admin_user_str.lower()

  #als de gebruiker geen admin rechten heeft
  if admin_user == 'no':
    #vraag om regels toe te staan
    approval_rules_str = input('\n"Approval rules" [approved/rejected]\n')
    approval_rules = approval_rules_str.upper()

    #als de regels niet zijn toegestaan
    if approval_rules == 'REJECTED':
      print('Purchase Order Rejected!')
    #als de regels zijn toegestaan
    elif approval_rules == 'APPROVED':
      #vraag om de betaalgegevens van de klant
      print('\nPayment details:')
      payment_details_firs_and_last_name  = input('first and last name: ')
      payment_details_adress = input('Street name and house number: ')
      payment_details_zip = input('Zipcode and city: ')
      payment_details_iban = input('IBAN: ')

      #print een verzendlabel
      print(f"\nOrder placed\n{payment_details_firs_and_last_name}\n{payment_details_adress}\n{payment_details_zip}")
    
    #als er geen gelidige input is
    else:
      print('Invalid input, choose \'approved\' or \'rejected\'')

  elif admin_user == 'yes':
    print('\nPayment details:')
    payment_details_firs_and_last_name  = input('first and last name: ')
    payment_details_adress = input('Street name and house number: ')
    payment_details_zip = input('Zipcode and city: ')
    payment_details_iban = input('IBAN: ')

    print(f"\nOrder placed\n{payment_details_firs_and_last_name}\n{payment_details_adress}\n{payment_details_zip}")

  #als er geen gelidige input is
  else:
    print("Invalid input, type 'yes' or 'no'")

#als er geen gelidige input is
else:
  print('Invalid input, choose \'online\' or \'offline\'.')