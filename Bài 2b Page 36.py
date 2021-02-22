def giai_thua(n):
    while n < 0:
        print("Loi gia tri! Nhap lai: ")
        n = int(input("Nhap gia tri n: "))
    if n == 0:
        return 1
    return n * giai_thua(n-1)

x = float(input("Nhap gia tri x: "))
item = 1
sum = 1
while (pow(x, item))/(giai_thua(item)) < pow(10, -6):
    sum = sum + (pow(x, item))/(giai_thua(item))
    item += 1

print(sum)