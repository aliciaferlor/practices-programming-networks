N = 11

n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, N):
    number = n1 + n2
    print(number, end=" ")
    n1 = n2
    n2 = number