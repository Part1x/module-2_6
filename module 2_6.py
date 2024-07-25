def password(n):
    result = ""
    s = [i for i in range(1, n + 1)]
    for i in range(len(s)):
        for j in range(i, len(s)):
            num1 = s[i]
            num2 = s[j]
            sum = num1 + num2
            if n % sum == 0:
                result += str(num1) + str(num2)

    return result
print(password(9))
print(password(8))