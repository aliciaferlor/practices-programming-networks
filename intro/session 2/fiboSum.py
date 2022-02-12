def fiboN():
    n = int(input("chose number: "))
    n1 = 0
    n2 = 1
    for i in range(2, n):
        number = n1 + n2
        n1 = n2
        n2 = number

    return number, n

def fiboSum(n, number):
    suma = 0
    for n in range(n):
        suma = suma + n
        number += n
    return suma

n, number= fiboN()
suma = fiboSum(n)
print("The sum of the",n,"th fibonacci number is: ", suma)