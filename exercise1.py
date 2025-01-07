my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
for number in my_list:
    if number >= 10:
        print(number)

my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_new_list = []
for number in my_list:
    if number >= 10:
        my_new_list.append(number)
print(my_new_list)

user_input = input("Enter a number: ")
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_new_list = []
for number in my_list:
    if number > int(user_input):
        my_new_list.append(number)
print(my_new_list)
