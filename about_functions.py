data_structure = [
                  [1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                 ]

def calculate_structure_sum(lst):
    result = 0
    if isinstance(lst, list):
        for i in lst:
            result += calculate_structure_sum(i)
    if isinstance(lst, tuple):
        for i in lst:
            result += calculate_structure_sum(i)
    if isinstance(lst, set):
        for i in lst:
            result += calculate_structure_sum(i)
    if isinstance(lst, dict):
        for k, v in lst.items():
            result += calculate_structure_sum(k)
            result += calculate_structure_sum(v)
    if isinstance(lst, int):
        result += lst
    if isinstance(lst, str):
        result += len(lst)
    return result


print(calculate_structure_sum(data_structure))