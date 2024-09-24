number_one=float(input("Введите первое число для проверки , какое из двух окажется меньше: "))
number_two=float(input("Введите втрое число для проверки , какое из двух окажется меньше: "))
if number_one > number_two:
    print(f"Второе число: {number_two} меньше первого")
elif number_two > number_one:
    print(f"Первое число: {number_one} меньше второго")
else:
     print(f"Первое число {number_one} равно Второму числу {number_two}")

