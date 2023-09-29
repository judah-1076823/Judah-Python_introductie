# create a tuple 
print('\ncreate a tuple:')
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# opdrachten
leveranciers = ('Apple',
'Asus',
'Dell',
'Lenovo',
'Acer',
'Samsung',
'MSI',
'Hewlett-Packard (HP)',
'Toshiba',
'Microsoft',
'Chuwi',
'Sony')

# a 
print('\nA:')
aantal_leveranciers = len(leveranciers)
print(f'De tuple bevat {aantal_leveranciers} computer leveranciers')

# b 
print('\nB:')
characters_8 = len(leveranciers[7])
print(f'De naam van {leveranciers[7]} bestaat uit {characters_8} karakters')

# c 
print('\nC:')
print(leveranciers[9])