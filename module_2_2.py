first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))

# ввод 1 условия
if first == second == third:
    print(3)

# ввод 2 условия
elif first == second or first == third or second == third:
    print(2)

# ввод 3 условия
else:
    print(0)