def giai_thua(n):
    while n < 0:
        print("Error!")
        n = int(input("Nhap n: "))
    if n == 0:
        return 1
    return n * giai_thua(n-1)

def tu_so(n):
    tu_so = pow(y, 2*n-1) * pow(-1, n+1)
    return tu_so

def so_hang(n):
    result = tu_so(n)/giai_thua(2*n-1)
    return result

y = -0.3
sum = 0
import itertools
for i in itertools.count(start=1):
    print(so_hang(i))
    if abs(so_hang(i)) < 10**(-6):
        break
    else:
        sum += so_hang(i)

print(sum)
        