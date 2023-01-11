def diagonal(n):
    print("+", (n+3)*"-", "+")
    for i in range(0,n+1):
        print("|", (n - i) * "#", " ", i * "#", "|")
    print("+", (n+3)*"-", "+")

diagonal(20)

