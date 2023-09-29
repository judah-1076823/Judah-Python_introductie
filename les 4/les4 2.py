# create a list
print('\nMy list:')
my_list = [1,2,3,4,5]
print(my_list)

# elementen mogen van elk data type zijn
print('\nString data type')
my_list = [1, 2, 3, 'four', 5]
print(my_list)

# elementen hebben een 'index' nummer om hun locatie in de lijst aan te geven. Begint bij 0
print('\nprint index 0 drom my list')
print(my_list[0])

# elementen toeveogen achteraan een lijst
print('\neentje toevoegen')
my_list.append(6)
print(my_list)

# of op een specifieke locatie
print('\nop een specifieke plek')
my_list.pop(2)
my_list.insert(2, 'three')
print(my_list)
