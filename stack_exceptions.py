def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data



def  calculate_average(numbers):
    divider = 0
    try:
       for i in numbers:
            if isinstance(i, int):
                divider += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
       aver = personal_sum(*numbers)[0] / divider
    except ZeroDivisionError:
        return 0
    return aver


print(personal_sum(1, 'hi', 3, 'uhu', 8))
print(calculate_average(567))
print(calculate_average([1, 2, 3, 4, 5]))