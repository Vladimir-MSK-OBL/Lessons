grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_lst = list(frozenset(students)) # converting a set to a list

students_lst.sort() # we arrange the names in alphabetical order

dict_res = {}
average_scoresum = 0

while True:
    stds = str
    grds = 0
    grds_l = []
    stds = input("Введите имя студента(0 - закончить ввод):")

    while True:
        grds = int(input("Введите оценки студента(0 - закончить ввод):"))

        if grds == 0:
            break

        grds_l.append(int(grds))

    if stds == "0":
        break

    average_scoresum = sum(grds_l) / len(grds_l)

    dict_res[stds] = average_scoresum


print("Average student score:", dict_res)