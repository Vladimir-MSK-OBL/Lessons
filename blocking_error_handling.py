import threading
from time import sleep
from random import randint

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.lock.locked()

    def deposit(self):
        num_transac = 100
        self.lock.acquire()
        for _ in range(num_transac):
            num = randint(50, 500)
            self.balance += num
            print(f'Пополнение: {num}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
        sleep(0.001)


    def take(self):
        num_transac = 100
        for _ in range(num_transac):
            num = randint(50, 500)
            print(f'Запрос на {num}.')
            if num >= self.balance:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            else:
                self.balance -= num
                print(f'Снятие: {num}. Баланс: {self.balance}')
            if self.lock.locked():    # Если не снимать блокировку
                self.lock.release()   # происходит бесконечное зацикливание.



bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')