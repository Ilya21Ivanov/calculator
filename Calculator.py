num1 = int(input("Введите 1-е число: "))
num2 = input("Выберите действие (+,-,*,/): ")
num3 = int(input("Введите 2-е число: "))

if num2 == "+":
    print(num1 + num3)
elif num2 == "-":
    print(num1 - num3)
elif num2 == "*":
    print(num1 * num3)
elif num2 == "/":
    if num3 == 0:
        print("Нельзя делить на 0")
else:
    print(num1 / num3)

