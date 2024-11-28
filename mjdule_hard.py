

first_stoune = 0
pairs = set()
result = []

first_stoune = int(input("Введите число от 3 до 20:"))

for j in range(1, first_stoune):
    
    for k in range(j + 1, first_stoune):

        if first_stoune % (j + k) == 0:

            if (j,k) not in pairs and (k, j) not in pairs:
                pairs.add((j, k))
                result.append(j)
                result.append(k)

print("Первый камень:", first_stoune)
print("Пары:", *result)
