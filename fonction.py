import re
from unittest import result
from urllib import response
import crud 
import os
import time

def creation_user () :
    """ fonction pour crée un compte pour l'utilisateur ou administrateur
        si c'est l'utilisateur :
            - on lui défini son rôle
            - on lui demande c'est information confidenciel (prenom, nom, mail, mot de passe)
            - on verifie si les deux mot de passe corresponde :
                alors on l'enregistre dans la base de données 
            - sinon on demande de rentrez de nouveaux les information      
    """
        
    prenom = input("entrez vôtre prenom : ")
    nom = input("entrez vôtre nom : ")
    mail = input("entrez vôtre mail : ")
    mdp = input("entrez vôtre mot de passe : ")
    mdp2 = input("confirmer vôtre mot de passe : ")

    if mdp == mdp2 :
        crud.creer_user(prenom, nom, mdp, mail)
        return print("inscription reussi")
    else :
        return print("Veuillez avoir les deux mot de passe identique")

def connexion_user () :
    """ fonction pour la connexion utilisateur
        on demande le mail et le mot de passe 
        si crud.verif_user renvoi none 
            retourne connexion echouée
        sinon renvoi la ligne de la base de donnée 
    """

    mail = input("entrez vôtre mail : ")
    mdp = input("entrez vôtre mot de passe : ")

    return crud.verif_user(mail, mdp)

def afficher_erreur () :
    os.system("cls")
    print("veuillez entrez une commande valide !")

def creer_admin () :
    """ fonction qui creer un admin """
    crud.creer_admin()

def ajout_ordinnateur() :
    """ ajouter un ordinnateur dans la base de données (seulement l'admin)"""

    marque = input ("Entrez la marque de l'ordinateur : ")
    processeur = input("Entrez le type de processeur : ")
    carte_graphique = input ("Entrez la reference de la carte graphique : ")
    ram = input ("Entrez la capacité de la ram : ")
    disque = input ("Entrez la capacite du disque dur : ")

    return crud.creer_ordinateur(marque, processeur, carte_graphique, ram, disque)

def ajout_pc_user () :
    """ fonction pour ajouter un pc a un utilisateur"""

    ref = input("entrez la référence du pc : ")
    id_user = input("entrez l'id de l'utilisateur : ")
    id_pc = input("entrez l'id du pc : ")

    return crud.creer_carnet(ref, id_user, id_pc)

def ticket () :
    """crée un ticket

    Returns:
        string: ajout de la référence du pc et le message
    """
    ref_pc = crud.select_ticket_ref_pc ()

    ref = input("reference pc : ")
    message = input("ecrire message : ")

    id_ticket = ref_pc
    liste_id = [str(id[0]) for id in id_ticket]
    print(liste_id)
    if ref in liste_id :
        return print("trop de ticket en cours")
    else :
        return crud.creer_ticket(ref, message)


def tickets_en_cours () :

    """fonction pour afficher les ticket en cours a l'admin

    Returns:
        variable: retourn la variable
    """

    resultat = crud.select_ticket()
    resultat_pc = crud.select_carnet()

    for i in range(len(resultat)):
        print("Numéro PC :", resultat_pc[i][0])
        print("Marque PC : ", resultat_pc[i][1])

        for j in range(len(resultat_pc[0])):
            print(resultat[i][j])
            print("------------------------")
    return resultat

def select_id_user (command) :

    """fonction pour selectionner l'id de l'utilisateur

    Returns:
        variable: retourn l'id de lutilisateur
    """

    resultat_user = crud.select_user_admin()
    return resultat_user[command][2]
        
def ticket_user (id_user) :

    """fonction pour afficher les ticket de l'utilisateur

    Returns:
        variable: renvoi la variable 
    """
    
    resultat_pc = crud.select_carnet_user(id_user)

    for i in range(len(resultat_pc)) :
        print(resultat_pc[i][0])
        print(resultat_pc[i][2])

        for j in range(len(resultat_pc)):
            ref_pc = resultat_pc[i][0]
            print(crud.select_ticket_user(ref_pc)[0][j])
            print("--------------------------------------")

    return resultat_pc         
