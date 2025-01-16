import threading
from time import sleep


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.number_days = 0

    def battle(self, name, power):
        while self.enemies:
            self.enemies -= power
            self.number_days += 1
            print(f'{name}, сражается {self.number_days} дней, осталось {self.enemies} воинов.\n')
            sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.number_days} дней(дня)!\n')



first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()