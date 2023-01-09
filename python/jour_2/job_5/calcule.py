def calcule(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2

        case "-":
            return num1 - num2

        case "*":
            return num1 * num2

        case "/":
            return num1 / num2

        case "%":
            return num1 % num2


num1 = int(input('Entrez une valeur entière : '))
num2 = int(input('Entrez une seconde valeur entière : '))
operator = str(input("Entrez l'opération voulue : "))

print(calcule(num1, operator, num2))
