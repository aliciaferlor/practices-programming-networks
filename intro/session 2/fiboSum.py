def fiboSum(n):
    n1 = 0
    n2 = 1
    suma = n1 + n2
    for i in range(2, n):
        number = n1 + n2
        suma = suma + number
        n1 = n2
        n2 = number
    return suma

a = 5
b = 10
print("The sum of the",a,"th fibonacci number is: ", fiboSum(a))
print("The sum of the",b,"th fibonacci number is: ", fiboSum(b))