def fiboN():
    n = int(input("chose number: "))
    n1 = 0
    n2 = 1
    for i in range(2, n):
        number = n1 + n2
        print(number, end= " ")
        n1 = n2
        n2 = number

    return number, n

number, n = fiboN()
print("is the fibonacci sequence")
print("The",n,"th fibonacci number is: ", number)
