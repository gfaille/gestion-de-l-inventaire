import crud 

def creation_compte (choix) :
    """ fonction pour crée un compte pour l'utilisateur ou administrateur
        si c'est l'utilisateur :
            - on lui défini son rôle
            - on lui demande c'est information confidenciel (prenom, nom, mail, mot de passe)
            - on verifie si les deux mot de passe corresponde :
                alors on l'enregistre dans la base de données 
            - sinon on demande de rentrez de nouveaux les information 
        et si c'est l'admin :
            - on defini son rôle
            - on lui demande c'est information confidenciel (prenom, nom, mail, mot de passe)
            - on verifie si les deux mot de passe corresponde :
                alors on l'enregistre dans la base de données 
            - sinon on demande de rentrez de nouveaux les information      
    """
    if choix == 1 :
        

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

    elif choix == 2 :
        
        role = 1

        prenom = input("entrez vôtre prenom : ")
        nom = input("entrez vôtre nom : ")
        mail = input("entrez vôtre mail : ")
        mdp = input("entrez vôtre mot de passe : ")
        mdp2 = input("confirmer vôtre mot de passe : ")

        if mdp == mdp2 :
            crud.creer_user(role, prenom, nom, mdp, mail)
            return
        else :
            return print("Veuillez avoir les deux mot de passe identique")
    else :
        print("Veuillez choisir un chiffre correct")

def connexion_user () :
    """ fonction pour la connexion utilisateur
        on demande le mail et le mot de passe 
        si crud.verif_user renvoi none 
            retourne connexion echouée
        sinon renvoi la ligne de la base de donnée 
    """

    mail = input("entrez vôtre mail : ")
    mdp = input("entrez vôtre mot de passe : ")

    if  crud.verif_user(mail, mdp) == None :
        return print("connexion echouée")
    else :
        return crud.verif_user(mail, mdp)

def connexion_admin () :
    """ fonction pour la connexion administrateur
        on demande le mail et le mot de passe 
        si crud.verif_user renvoi none 
            retourne connexion echouée
        sinon renvoi la ligne de la base de donnée 
    """

    mail = input("entrez vôtre mail : ")
    mdp = input("entrez vôtre mot de passe : ")

    if crud.verif_user(mail, mdp) == None :
        return print("connexion echouée")
    else :
        return crud.verif_user(mail, mdp)


def nb_pc () :
    """ fonction qui permet d'avoir le nombre total de pc"""

def nb_tickets () :
    """ fonction qui permet de calculer le nombre de ticket total en cours"""

def nb_tickets_terminer () :
    """ fonction qui permet de calculer le nombre de ticket total terminer"""