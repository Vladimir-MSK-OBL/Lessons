class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers
        self.get_vin(vin_number)
        self.get_nums(numbers)


    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            pass
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if 1000000 <= vin_number <= 9999999:
            pass
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True


    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            pass
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) == 6:
            pass
        else:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


    def get_vin(self, vin_number):
        return self.__is_valid_vin(vin_number)


    def get_nums(self, numbers):
        return self.__is_valid_numbers(numbers)



class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message



class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')