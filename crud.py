import sqlite3
import hashlib

def creer_user (prenom, nom, mdp, mail) :
    """ la fonction pour un créer utilisateur (prenom, nom, mdp) : 
        - connexion a la base de donner, 
        - executer la requette pour inserer les valeur dans la bdd
        - enregistre dans bdd
        - ferme la connexion a la bdd
        """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", (None, 0, prenom, nom, mdp, mail))
    connexion.commit()
    connexion.close()

def creer_admin (prenom, nom, mdp, mail) :
    """ la fonction pour créer un admin (prenom, nom, mdp) :
        - connexion a la base de donner
        - executer la requette pour inserer les valeur dans la bdd
        - enregistre dans la bdd
        - ferme la connexion a la bdd
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", (None, 1, prenom, nom, mdp, mail))
    connexion.commit()
    connexion.close()

def suppr_user (id) :
    """ la fonction supprimer un utilisateur (prenom, nom) 
        - connexion a la base de donner
        - executer la requette pour supprimer les valeur de la bdd
        - enregistre les modification
        - ferme la connexion
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM user WHERE id = ?", (id, ))
    connexion.commit()
    connexion.close()


def verif_user (mail, mdp) :
    """ la fonction pour verifier l'utilisateur (mail, mdp)
        - connexion a la base de données 
        - executer la requette pour selectionner dans le tableau user et verifier que l'adresse mail, mot de passe corresponde bien
        - enregistre dans une variable les données recuperer 
        - ferme la connexion a la bdd
        - retourne les données 
    """
    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM user WHERE mail = ? AND mdp = ?", (mail, mdp, ))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse
