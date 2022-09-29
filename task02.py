even = 2548
x1 = even % 10
x2 = even // 10 % 10
x3 = even //100 % 10
x4 = even // 1000

n = ( x1 + 1 ) % 2 + ( x2 + 1 ) % 2 + ( x3 + 1 ) % 2 + ( x4 + 1 ) % 2
print(n)