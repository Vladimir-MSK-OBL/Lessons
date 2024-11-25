grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_lst = list(frozenset(students)) # converting a set to a list

students_lst.sort() # we arrange the names in alphabetical order

dict_res = {students_lst[0]: sum(grades[0]) / len(grades[0]),
            students_lst[1]: sum(grades[1]) / len(grades[1]),
            students_lst[2]: sum(grades[2]) / len(grades[2]),
            students_lst[3]: sum(grades[3]) / len(grades[3]),
            students_lst[4]: sum(grades[4]) / len(grades[4])
            }

print("Average student score:", dict_res)
