with open(r'Path') as file:                                         #вместо r'Path' нужно прописать путь к файлу, в который входят значения
    numbers = [num for num in file]
    number_of_students = numbers.pop(0)
    number_of_messages = [int(num) for num in numbers[0].split(',')]

k = 0
history = []
students_index = 1
for i in range(number_of_students):
    if students_index < number_of_students:
        count = number_of_messages[i]
        while count > 0:
            count -= 1
            k += 1
            students_index += 1
            history.append((i, students_index))
            if students_index == number_of_students:
                break
    else:
        break

if students_index < number_of_students:
    print(-1)
else:
    print(k)
    for f, t in history:
        print(f, t)
