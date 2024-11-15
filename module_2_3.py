my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length_list = len(my_list)

index = 0
while True:
    num = my_list[index]

    if num < 0 or index > length_list:
         break

    else:
        print(num)

    index += 1