import mysql.connector
import re
from tabulate import tabulate
#-------------------------------
#CONNEXION À LA BASE DE DONNÉES
#-------------------------------

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
    print("\n============ Choisissez une catégorie =============")
    print("1.Laitier")
    print("2.Charcuterie")
    print("3.Boissons")
    print("4.Hygiène")
    print("5.Cereale")
    print("6.Légumes")
    print("7.Fruits exotiques")


    choix = int(input("Choisir une categorie:..."))

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
        case "6":
            return "Légumes"
        case "7":
            return "Fruits exotiques"
        case _:
            print("Choix invalide")
            return None
        
        
        

#FONCTION AFFICHER LISTE PRODUIT
def Lister_inventaire():
    query = "SELECT * FROM Produits"    
    moncurseur.execute(query)
    Resultat = moncurseur.fetchall()
    
    colonnes = [desc[0] for desc in moncurseur.description]
    
    print(tabulate(Resultat, headers=colonnes, tablefmt="grid"))



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
def supprimer_produit():
    id_produit = input("Entrez l'Id du produit:")  
    query = "DELETE FROM Produits WHERE id = %s"
    moncurseur.execute(query,(id_produit),)
    connexion.commit()
    print(f"Le produit avec l'id {id_produit} à été supprimé avec succès.")

#FONCTION DASHBOARD COMMENCE ICI
def dashboard():
    print("\nBienvenu dans le dashboard du programme")
    afficher_produit_lpc()
    afficher_somme_produit()
    afficher_produit_par_categorie()

def afficher_produit_lpc():
    query = "SELECT Designation,Prix_unitaire FROM Produits ORDER BY Prix_unitaire DESC LIMIT 1"
    moncurseur.execute(query)
    resultat = moncurseur.fetchone()
    print(f"1.Le produit le plus cher est: {resultat[0]}:{resultat[1]} FCFA ")

def afficher_somme_produit():
    query = "SELECT SUM(Prix_unitaire * Stock) FROM Produits "
    moncurseur.execute(query)
    resultat = moncurseur.fetchone()
    print(f"2.Le montant totale du stock est de {resultat[0]} FCFA.")

def afficher_produit_par_categorie():
    query = "SELECT Categorie, COUNT(*) FROM Produits GROUP BY Categorie"
    moncurseur.execute(query)
    resultat = moncurseur.fetchall()
    for Categorie, nombre in resultat:
     print(f"Categorie:{Categorie}: {nombre} produit(s)")

#FONCTION DASHBOARD TERMINE ICI



#------------------------------------------------------------------------
#                                MENU PRINCIPALE
#------------------------------------------------------------------------
while True:
  print("\n=============== Bienvenue ================") 
  print("\n1.Ajouter un produit")
  print("2.Lister inventaire")
  print("3.Mise à jour du stock de produit")
  print("4.Recherchez un produit")
  print("5.Supprimez un produit")
  print("6.Dashboard")
  print("0.Quitter")

  choix = input("Entrez une option:...")

  match choix:

    case "1":
        Designation = input("Entrez nom du produit:").strip()
        if not re.match(r"^(?=(?:.*[A-Za-z]){3,})[A-Za-z0-9\s\-]+$", Designation):
         print("Nom de produit invalide")

        Categorie = choisir_categorie()
        print("Categorie:",Categorie)

        prix = input("Entrez le prix du produit:").strip()
        if not prix.alnum():
            print("Saisie invalide.")

        stock = input("Entrez le stock du produit").strip()
        if not stock.isnumeric():
            print("saisie invalide.")
        Ajouter_produit(Designation,Categorie,prix,stock)

    case "2": 
          Lister_inventaire()

    case "3":
          Mettre_à_jour()

    case "4": 
          Designation = input("Entrez nom du produuit:").strip() 
          Recherche_produit(Designation)  

    case "5": 
           supprimer_produit()

    case "6":
          dashboard()

    case "0":
          print("Merci d'avoir utilisé notre boutique!") 
          break     
    case _: 
          print("Saisi invalide !")              
   
            
