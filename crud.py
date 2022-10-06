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

    mdp += """
                What's new Scooby-Doo?1
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                What's new Scooby-Doo?
                We're gonna follow you
                You're gonna solve that mystery
                We see you Scooby-Doo
                We're coming after you
                What's new Scooby-Doo?
                
                Don't look back, you may find another clue
                The Scooby snacks will be waiting here for you
                
                What's new Scooby-Doo?
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                Na na na na na
                Na na na na na
                Na na na na na na na
                Na na na na na
                Na na na na na
                What's new Scooby-Doo?!
            """
    mdp_crypter = hashlib.sha256(mdp.encode()).hexdigest()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", (None, 0, prenom, nom, mdp_crypter, mail))
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

    mdp += """
                What's new Scooby-Doo?1
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                What's new Scooby-Doo?
                We're gonna follow you
                You're gonna solve that mystery
                We see you Scooby-Doo
                We're coming after you
                What's new Scooby-Doo?
                
                Don't look back, you may find another clue
                The Scooby snacks will be waiting here for you
                
                What's new Scooby-Doo?
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                Na na na na na
                Na na na na na
                Na na na na na na na
                Na na na na na
                Na na na na na
                What's new Scooby-Doo?!
            """
    mdp_crypter = hashlib.sha256(mdp.encode()).hexdigest()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", (None, 1, prenom, nom, mdp_crypter, mail))
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

    mdp += """
                What's new Scooby-Doo?1
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                What's new Scooby-Doo?
                We're gonna follow you
                You're gonna solve that mystery
                We see you Scooby-Doo
                We're coming after you
                What's new Scooby-Doo?
                
                Don't look back, you may find another clue
                The Scooby snacks will be waiting here for you
                
                What's new Scooby-Doo?
                We're coming after you
                You're gonna solve that mystery
                I see you Scooby-Doo
                The trail leads back to you
                What's new Scooby-Doo?
                
                Na na na na na
                Na na na na na
                Na na na na na na na
                Na na na na na
                Na na na na na
                What's new Scooby-Doo?!
            """
    mdp_crypter = hashlib.sha256(mdp.encode()).hexdigest()

    curseur.execute("SELECT * FROM user WHERE mail = ? AND mdp = ?", (mail, mdp_crypter, ))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse
