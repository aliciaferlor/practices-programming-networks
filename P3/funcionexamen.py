seq = "ACGTACGT"
n = 0
for i in seq:
    if i == "A":
        n = n + 2
    elif i == "C":
        n = n - 1
    elif i == "G":
        n = n + 4
    elif i == "T":
        n = n + 6
print(n)


