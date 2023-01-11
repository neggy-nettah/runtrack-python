L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1
i = 0
while i < len(L):
    if L[i] <= 25 or L[i] >= 90:
        pass
    else:
     produit = produit * L[i]
    i = i + 1
print(produit)