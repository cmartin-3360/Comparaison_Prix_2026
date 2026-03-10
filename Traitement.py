def compare_products(A, B, C):
    if A == B == C:
        return "Les trois produits sont équivalents en prix"
    elif A > B > C:
        return "Produit A > Produit B > Produit C"
    elif A < B < C:
        return "Produit A < Produit B < Produit C"
    elif B > A > C:
        return "Produit B > Produit A > Produit C"
    elif B < A < C:
        return "Produit B < Produit A < Produit C"
    elif C > A > B:
        return "Produit C > Produit A > Produit B"
    elif A < C < B:
        return "Produit A < Produit C < Produit B"
    elif C > B > A:
        return "Produit C > Produit B > Produit A"
    else:
        return "Ordre non déterminé (peut-être égalités partielles)"

print ("Comparaison des prix de trois produits:")

result = compare_products(
        float(input("Prix de A: ")),
        float(input("Prix de B: ")),
        float(input("Prix de C: ")))
print(result)
   
  