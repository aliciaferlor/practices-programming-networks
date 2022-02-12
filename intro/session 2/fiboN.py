def fiboN():
    N = int(input("chose number: "))
    n1 = 0
    n2 = 1
    for i in range(2, N):
        number = n1 + n2
        print(number, end= " ")
        n1 = n2
        n2 = number

    return number, N

number, N = fiboN()
print("is the fibonacci sequence")
print("The", N, "fibonacci number is: ", number)
