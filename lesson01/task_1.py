
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
user_input = int(input('Введите трёхзначное число: '))

a = user_input // 10 // 10
b = user_input // 10 % 10
c = user_input % 10

x = a + b + c
y = a * b * c

print(f'{x=} {y=}')