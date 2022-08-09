#create a list of integer between 5.5 and 20.5
my_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#odd numbers
odd_number_count = len(list(filter(lambda x: (x%2 != 0) , my_list)))
#even numbers
even_number_count = len(list(filter(lambda x: (x%2 == 0) , my_list)))
print("Even numbers in the list: ", even_number_count)
print("Odd numbers in the list: ", odd_number_count)

square = map(lambda n: n ** 2, my_list)
squared_list = list(square)

print(squared_list)

cube = map(lambda n: n ** 3, my_list)
cubic_list = list(cube)

print(cubic_list)