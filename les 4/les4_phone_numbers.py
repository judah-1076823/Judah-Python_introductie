# Phone numbers 
phone_numbers = {'The Simpsons': '636-555-3226',
                 'Vegas Vacation': '555-0100',
                 'Ghostbusters (OLD)': '555-23678',
                 'Billy Madison': '555-0840',
                 'Swingers': '213-555-4679',
                 'Bruce Almighty': '555-0123',
                 'Seinfield': '555-FILK',
                 'Arrested Development': '555-0113',
                 'Die Hard With a Vengeance': '555-0001',
                 'The A-Team': '555-6162'}

print(phone_numbers)

# A 
print('\nA:')
print(f'Het telefoonnummer van Bruce Almighty is {phone_numbers["Bruce Almighty"]}.')

# B
print('\nB:')
phone_numbers['Harry Potter'] = '605-475-6961'
print(phone_numbers)

# C 
print('\nC:')
phone_numbers['Ghostbusters'] = '555-2368'
print(f'Het telefoonnummer {phone_numbers["Ghostbusters (OLD)"]} van de Ghostbusters is gewijzigd naar {phone_numbers["Ghostbusters"]}')

# D 
print('\nD:')
print(f'Telefoonnummer {phone_numbers["Seinfield"]} van Seinfeld is verwijderd.')
del phone_numbers['Seinfield']

# E 
print('\nE:')
print(f'In de dictonary zitten {len(phone_numbers)} telefoonnummers.')