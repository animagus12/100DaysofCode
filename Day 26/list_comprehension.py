numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Animagus"
new_list = [print(letter) for letter in name]

range_list = [print(n+n) for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_name_list = [name for name in names if len(name) <= 4]
print(new_name_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_name_list = [name.upper() for name in names if len(name) >= 5]
print(new_name_list)