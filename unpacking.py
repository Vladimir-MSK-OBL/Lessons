def print_params(a=1, b="bububu", c=True):

    print(a, b, c)


print_params()

print_params(a=1, b="bububu", c=True)

print_params(a=1, b="bububu")

print_params(a=1)

print_params(a=1, b="bububu", c=False)

print_params(c=False)

print_params(a=[1, 2, 3, 4], b=8, c="bobobob")

print_params(b=25)

print_params(c=[1, 2, 3])

print("#" * 50)

values_list = [8, "bobob", True]
values_dict = {"a": 1, "b": "tutu", "c": False}

print_params(*values_list)

print_params(**values_dict)

print("#" * 50)

values_list2 = ["gotuda", 45.9]

print_params(*values_list2, 56)