a = int(input()) #левая граница отрезка
b = int(input()) #правая граница отрезка

numbers = []

k = 1
while True:
    user_input = input()
    if user_input == "":
        break  #

    try:
        number = int(user_input)
        numbers.append(number)  # Добавляем число в список
    except ValueError:
        print("Ошибка: введено не число. Попробуйте снова.")
for i in numbers:
    if (i >= a) and (i <= b):
        l = 1
    else:
        k = 2
if k == 2:
    print("False")
else:
    print("True")