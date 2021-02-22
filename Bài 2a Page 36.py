# Bài 2.a Page 36.
# Tạo hàm tính giai thừa 
def giai_thua(n):

    while n < 0:
        print("Loi gia tri. Nhap lai.")
        n = int(input("Nhap gia tri n: "))
    if n == 0:
        return 1
    return n * giai_thua (n -1)

k1 = 1
x1 = 1
while giai_thua(k1 - 1) < pow(10, 6):
    x1 = x1 + 1/(giai_thua(k1))
    k1 += 1
print(x1)
print("-"*100)

