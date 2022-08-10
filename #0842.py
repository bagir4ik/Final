def summing_numbers_as_strings(number_1: str, number_2: str):
    '''Суммирование чисел "столбиком". Числа представлены в виде str'''
    if len(number_1) != len(number_2):
        diff = abs(len(number_1) - len(number_2))
        if len(number_1) > len(number_2):
            number_2 = '0' * diff + number_2
        else:
            number_1 = '0' * diff + number_1
    
    final_number = ''
    over_nine = False
    for i in range(len(number_1)-1, -1, -1):
        sum_num = int(number_1[i]) + int(number_2[i])
        if over_nine:
            sum_num += 1
            over_nine = False
        if sum_num > 9:
            sum_num %= 10
            over_nine = True
        final_number = str(sum_num) + final_number
    if over_nine:
        final_number = '1' + final_number
    
    return final_number

print(summing_numbers_as_strings('9999999999999999', '999999999999999'))