# Split a String into a List of Integers using a list comprehension

my_str = '2 4 6 8 10'

list_of_strings = my_str.split(' ')
print(list_of_strings)  # 👉️ ['2', '4', '6', '8', '10']

list_of_integers = [int(x) for x in list_of_strings]
print(list_of_integers)  # 👉️ [2, 4, 6, 8, 10]