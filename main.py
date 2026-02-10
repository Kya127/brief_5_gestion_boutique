import mysql.connector
#CONNEXION À LA BASE DE DONNÉES
connexion = mysql.connector.connect(
    host="localhost",
    user="KyaDev",
    password="Boutique@1234",
    database="Gestion_boutique"
)
print("Connexion réussie")

moncurseur = connexion.cursor()
#FONTION AJOUT DE PRODUIT
def Ajouter_produit(Designation,Categorie,Prix_unitaire,Stock):
    query = "INSERT INTO Produits (Designation,Categorie,Prix_unitaire,Stock) VALUES (%s,%s,%s,%s)"
    moncurseur.execute(query,(Designation,Categorie,Prix_unitaire,Stock))
    connexion.commit()
    print("Produit ajouté.")

#FONCTION CHOISIR CATEGORIE
def choisir_categorie():
    print("\nChoisissez une catégorie :")
    print("1.Laitier")
    print("2.Charcuterie")
    print("3.Boissons")
    print("4.Hygiène")
    print("1.Cereale")

    choix = input("Choisir une categorie:...")

    match choix:
        case "1":
            return "Laitier"
        case "2":
            return "Charcuterie"
        case "3":
            return "Boissons"
        case "4":
            return "Hygiène"
        case "5":
            return "Cereale"
        case _:
            print("Choix invalide")
            return None
        
        
        

#FONCTION AFFICHER LISTE PRODUIT
def Lister_inventaire():
    query = "SELECT * FROM Produits"    
    moncurseur.execute(query)
    for Resulat in moncurseur.fetchall():
        print(Resulat)


# FONCTION MISE À JOUR 
def Mettre_à_jour():
    id_produit = input("Entrez l'id du produit:")
    nouveau_stock = input("Entrez le nouveau stock:")
    query = "UPDATE Produits SET Stock = %s WHERE id = %s" 
    moncurseur.execute(query,(nouveau_stock,id_produit))
    connexion.commit()
    print("Stockage à été mise à jour.")  


#FONCTION RECHERCHER UN PRODUIT

def Recherche_produit(Designation):
    query = "SELECT Designation, Categorie, Prix_unitaire,Stock FROM Produits WHERE Designation LIKE %s "
    moncurseur.execute(query,('%'+Designation+'%',))
    Resultat = moncurseur.fetchone()
    if Resultat:
        print("\nProduit trouvé :")
        print("Designation :", Resultat[0])
        print("Categorie :", Resultat[1])
        print("Prix :", Resultat[2])
        print("Stock :", Resultat[3])
    else:
        print("Aucun produit de ce nom trouvé.")
       #print(f"{Designation} de {Categorie} trouvé(e) disponible reste {stock} en stock")

#FONCTION SUPPRIMER UN PRODUIT
#def supprimer_produit():



# MENU PRINCIPALE

while True:
  print("Bienvenue !") 
  print("\n1.Ajouter un produit")
  print("2.Lister inventaire")
  print("3.Mise à jour du stock de produit")
  print("4.Recherchez un produit")
  print("5.Supprimez un produit")
  print("6.Dashboard")
  print("7.Quitter")

  choix = input("Entrez une option:...")

  match choix:

    case "1":
        Designation = input("Entrez nom du produit:")
        Categorie = choisir_categorie()
        print("Categorie:",Categorie)
        prix = input("Entrez le prix du produit:")
        stock = input("Entrez le stock du produit")
        Ajouter_produit(Designation,Categorie,prix,stock)

    case "2": 
          Lister_inventaire()

    case "3":
          Mettre_à_jour()

    case "4": 
          Designation = input("Entrez nom du produuit:") 
          Recherche_produit(Designation)    

     
                 
            
