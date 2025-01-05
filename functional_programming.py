def apply_all_func(int_list, *functions):

    result = {}

    for function in functions:
        volume = function(int_list)
        result[function.__name__] = volume

    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
