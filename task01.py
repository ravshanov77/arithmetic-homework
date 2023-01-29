def sum_odd(num: int):
    x1 = num % 10
    x2 = num // 10 % 10
    x3 = num // 100 % 10
    x4 = num // 1000

    sum = 0
    sum += (x1 % 2) * x1
    sum += (x2 % 2) * x2
    sum += (x3 % 2) * x3
    sum += (x4 % 2) * x4
    return sum


print(sum_odd(2347))