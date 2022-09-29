odd=1111
x1 = odd % 10
x2 = odd // 10 % 10
x3 = odd // 100 % 10
x4 = odd // 1000

n = x1 % 2 + x2 % 2 + x3 % 2 + x4 % 2
print(n)