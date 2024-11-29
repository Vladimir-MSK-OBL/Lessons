
call = 0

def count_calls():
    global call
    call += 1
    return call



def string_info(str_):

    count_calls()

    tup = ()
    len_str = len(str_)
    tup += (len_str,)

    up_str = ""
    for j in str_:
        up_str += j.upper()
    tup += (up_str,)

    low_str = ""
    for k in str_:
        low_str += k.lower()
    tup += (low_str,)
    return tup



def is_contains(str_, lst):

    count_calls()

    str_low = ""
    for j in str_:
        str_low += j.lower()

    lst_low = []
    for k in lst:
        lst_low.append(k.lower())

    if str_low in lst_low:
        return True

    else:
        return False





a = string_info("KarabasBarabas")
print(a)
a = string_info("BuRatInkoandMalvinka")
print(a)

a = is_contains("DooM", ["DOom", "dOm", "kiNo"])
print(a)
b = is_contains("TraSh", ["ogo", "content", "kIno"])
print(b)

print(f'Колличество вызванных функций: {call}')