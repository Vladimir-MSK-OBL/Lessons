def is_prime(func):
    def simp_or_comp(*number):

        original_result = func(*number)
        number = original_result

        result_dec = ''
        for divider in range(2, number):
            if number % divider == 0:
                result_dec = f'Число {number} составное.'
                break
            else:
                result_dec = f'Число {number} простое.'
                break
        return result_dec
    return simp_or_comp


@is_prime
def sum_three(*numbers):
    result_sum = sum(numbers)
    return result_sum



result = sum_three(7, 4, 79)
print(result)

