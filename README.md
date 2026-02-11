Dans le cadre d'un projet de gestion de stock ce programme est une petite application réalisée en python pour gérer les produits d’une boutique.
Il permet d’ajouter des produits, consulter l’inventaire, modifier le stock, rechercher un produit, supprimer un produit et voir un petit tableau de bord (dashboard).
L’objectif est de faciliter la gestion quotidienne d’un magasin en centralisant les informations dans une base de données MySQL.

Les outils utilisés lors de ce projets sont:
Python
MySQL
mysql.connector (connexion à la base de données)
tabulate (affichage des tableaux)
re (contrôle des saisies utilisateur)

I.Connexion à la base de données

Au lancement du programme, une connexion est faite à la base de données Gestion_boutique.
Cette base contient une table Produits avec les informations suivantes :
id
Designation (nom du produit)
Categorie
Prix_unitaire
Stock
Si la connexion fonctionne, le message “Connexion réussie” s’affiche.

II.Fonctionnalités principales

1.Ajout de produit
L’utilisateur saisit :
le nom du produit,
la catégorie,
le prix,
le stock,
Le produit est ensuite enregistré dans la base de données.

2.Inventaire
Affiche tous les produits enregistrés sous forme de tableau affichant le nom du produit, sa categorie, son prix et le stock disponible pour ce produit.

3.Mise à jour du stock
Permet de modifier la quantité disponible d’un produit en utilisant son identifiant.

4.Rechercher un produit
L’utilisateur saisit un nom de produit.
Le programme affiche :
la désignation
la catégorie
le prix
le stock
Si le produit n’existe pas, un message s’affiche.

5.Supprimer un produit
Supprime un produit de la base de données à partir de son identifiant.

6.Dashboard (tableau de bord)
Affiche des informations importantes :
le produit le plus cher
la valeur totale du stock
le nombre de produits par catégorie

7.Le menu principale
Au lancement du programme, le menu suivant s'affiche et propose differente option :

Ajouter un produit
Lister inventaire
Mise à jour du stock
Rechercher un produit
Supprimer un produit
Dashboard
Quitter

L’utilisateur choisit simplement un numéro pour effectuer une action.

III.Contrôle des saisies

Le programme vérifie :
le nom du produit doit contenir au moins 3 lettres, peut contenir des chiffres, et des symboles comme (-) exemple: Coca-cola ou Lait 1L etc
le prix doit être valide 
le stock doit être un nombre 
Cela évite les erreurs dans la base de données.

Ce projet a pour objectif l'apprentissage de la connexion entre python et mysql, la manipulation des requete sql avec les fonctions d'aggregations mais aussi à pratiquer la logique de la programmation.
