

#Personnage = {
 ##   "nom" : "Kara",
  #  "arme" : "épée",
   ## "hp" : 10,
#"force" : 5,
    
    
#"points": 5,
#}

#print(f"{Personnage['nom']} attaque avec son arme {Personnage['arme']} !")

#Personnage["hp"] -= 5

#Personnage["vivant"] = True

#print(Personnage)


paquet = ["1" , "2" , "3" , "3"]

paquet_valide = set(paquet)


if len(paquet) != len(paquet_valide):
    print("Triche détectée ! Cartes en double.")
else:
    print("Paquet valide.")

