# Задание №3
#  def pyramid(visota):
#     for i in range(visota):
#         for j in range(visota - i - 1):
#             print(' ', end='')
#         for k in range(2 * i + 1):
#             print('X', end='')
#         print()
# x = (int(input("Введите высоту пирамиды: ")))
# pyramid(x)

#Задание №4
# def glas_soglas():
#     glas = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    
#     user_vvod = input("Введите строку на русском языке: ")
#     user_vvod = user_vvod.lower()  # Приводим строку к нижнему регистру для удобства сравнения
    
#     vowel_count = 0
#     consonant_count = 0
    
#     for i in user_vvod:
#         if i in glas:
#             vowel_count += 1
#         elif i.isalpha():  # Проверяем, является ли символ буквой
#             consonant_count += 1
    
#     if vowel_count > consonant_count:
#         print("Гласная строка")
#     elif consonant_count > vowel_count:
#         print("Согласная строка")
#     else:
#         print("Строка содержит одинаковое количество гласных и согласных букв")

# # Вызов функции для проверки
# glas_soglas()

# Задание 5
# def format_rubles(rubley):
#     if rubley == 1 or rubley % 10 == 1 and rubley != 11:
#         return f"{rubley} рубль"
#     elif 2 <= rubley % 10 <= 4 and (rubley < 10 or rubley >= 20):
#         return f"{rubley} рубля"
#     else:
#         return f"{rubley} рублей"

# # Пример использования:
# rubley = int(input("Введите количество рублей (от 0 до 100): "))
# if 0 <= rubley <= 100:
#     result = format_rubles(rubley)
#     print(result)
# else:
#     print("Некорректное количество рублей")

