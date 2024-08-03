def generate_password(n):
    result = ''
    for a in range(1, 21):
        for b in range(a + 1, 21):
            pair_sum = a + b
            if n % pair_sum == 0:
                result += str(a) + str(b)
    return result
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

