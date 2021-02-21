# Hàm tính sigma
def sigma(low, high):
    
    sum = 0 
    for x in range(low, high + 1):
        sum = sum + pow(abs(x), j)
    result = pow(sum, 1/j)
    return result

from fractions import Fraction as F

j_raw = input("Nhập giá trị j: ")

# Xử lí trường hợp nhập phân số.
j = F(j_raw)

print(sigma(2, 6))      
