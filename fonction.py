import crud 
import os

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
    os.system("clear")
    print("veuillez entrez une commande valide !")

def ajout_ordinnateur():
   
    marque=input ("Entrez la marque de l'ordinateur")
    processeur= input("Entrez le type de processeur")
    carte_graphique=input ("Entrez la reference de la carte graphique")
    ram=input ("Entrez la capacité de la ram")
    disque=input ("Entrez la capacite du disque dur")

    return crud.creer_ordinateur(marque, processeur, carte_graphique, ram, disque)