
def type_saison(type, saison):

    if (type == "fruits" and saison == "hiver"):
        return("Orange, mandarine et kiwi")
    elif (type == "fruits" and saison =="ete"):
        return("Poire, fraise et cassis")
    elif (type == "legumes" and saison =="hiver"):
        return("Carotte, topinambour et endive")
    elif (type == "legumes" and saison =="ete"):
        return("Artichaud, aubergine et navet")


type = input("Entrez fruits ou legumes : ")
saison = input("Entrez hiver ou ete: ")

print(type_saison(type, saison))
