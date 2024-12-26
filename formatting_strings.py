
male1 = 3
female1 = 2
team1_num = male1 + female1
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})

male2 = 3
female2 = 3
team2_num = male2 + female2
print('Итого в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})
print('#' * 50)

total2_tasks = 45
solved2_not_correctly = 3
score_2 = total2_tasks - solved2_not_correctly
total1_tasks = 43
solved1_not_correctly = 3
score_1 = total1_tasks - solved1_not_correctly
print('Команда Волшебники данных решила задач: {0}!'.format(score_2))
print('#' * 50)

team1_time = 18015.2
team2_time = 17780.5
print('Волшебники данных решили задачи за {0}c!'.format(team1_time))
print('#' * 50)

print(f'Команды решили {score_1} и {score_2} задачи.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}!')

tasks_total = (score_1 + score_2)
time_avg = round((team1_time + team2_time) / tasks_total, 1)


print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')

