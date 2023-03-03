print('Введите коэффициент A')
a = int(input())
print('Введите коэффициент B')
b = int(input())
print('Введите коэффициент C')
c = int(input())
x1 = 0
x2 = 0
d = 0
d = b**2 - 4*a*c
if d > 0:
    x1 = int((-b) - d**(0.5))/(2*a)
    x2 = int((-b) + d**(0.5))/(2*a)
    print('Корни уравнения:  ', x1, x2)
else:
    if d < 0:
        print('Корней нет')
    else:
        print('Корень уравнения: ', int((-b)/2*a))
