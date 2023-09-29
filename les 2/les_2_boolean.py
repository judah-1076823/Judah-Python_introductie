#Boolean

logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

user_name = "John Doe"
size_user_name = len(user_name)

entered_username = input("Username, please: ")
size_entered_user_name = len(entered_username)

user_name_is_bigger = size_user_name > size_entered_user_name
entered_username_is_bigger = size_entered_user_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_username} is: {user_name_is_bigger}")
print(f"The entered name {entered_username} has more characters then the user name {user_name} is: {entered_username_is_bigger}")

lights_on = False
lock_closed = True

alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")
print (f"The lights are turned on is: {lights_on}")
print(f"The lock is closed is: {lock_closed}")
