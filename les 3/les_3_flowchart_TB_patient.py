#flowchart TB patient
print('\nPatient exposed to TB')

#Vraag of de patient een kind of volwassene is.
age_str = input('\nIs the patient a adult or a child?\n')
age = age_str.upper()

#Als de patient volwassen is
if age == 'ADULT':
  #Vraag of de patient enige symptomen vertoond.
  answer_str = input('\nDoes the patient experience common TB symtoms? [yes/no]\n')
  answer = answer_str.upper()
  #als de patient symptomen vertoond
  if answer == 'YES':
    print('\nTreat as likely TB patient and perform full TB exam.')
  #als de patient geen symptomen vertoond
  elif answer == 'NO':
    print('\nHave patient report back if unwell; return in 1 month for checkup.')
  #als er geen 'Ja of Nee' is ingevoerd
  else:
    print('\nInvalid input, choose either \'yes\' or \'no\'')

#Als de patient een kind is.
elif age == 'CHILD':
  #Vraag of er een TB test gedaan kan worden
  tb_test_str = input('\nCan TB test be given? [yes/no]\n')
  tb_test = tb_test_str.upper()
  #Als er een TB test gegeven kan worden
  if tb_test == 'YES':
    print("""\nAdminister TB test.\nAsses TB test reslut and child's condition""")
  #Als er geen TB test gedaan kan worden
  elif tb_test == 'NO':
    child_condition_str = input('\nIs the child well? [yes/no]\n')
    child_condition = child_condition_str.upper()
    #Als het kind gezond is
    if child_condition == 'YES':
      print("""\n6 months preventive isoniazid\nhave Parent bring in if child shows any symptoms""")
    #Als het kind niet gezond is
    elif child_condition == 'NO':
      print("""\nTake fulle history.\nExamine for TB:\n\n- If TB likely diagnosis, treat for TB\n\n- If other diagnosis more likely, treat as needed and watch for TB symptoms""")
    #als er geen 'ja of nee' wordt ingevoerd
    else:
      print('Invalid input, choose [yes or no]')

#Als er geen keuze is gemaakt tussen (child/adult)
else:
  print('\nInvalid input, choose adult or child')