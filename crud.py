import sqlite3
import hashlib
from datetime import datetime
from unittest import result
from urllib import response

def creer_user (prenom, nom, mdp, mail) :
    """ la fonction pour un créer utilisateur (prenom, nom, mdp) : 
        - connexion a la base de donner, 
        - salage + hashage de mot de passe
        - executer la requette pour inserer les valeur dans la bdd
        - enregistre dans bdd
        - ferme la connexion a la bdd
        """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    mdp += """
                What's new Scooby-Doo?
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

def creer_admin () :
    """ la fonction pour créer un admin (prenom, nom, mdp) :
        - connexion a la base de donner
        - salage + hashage de mot de passe
        - executer la requette pour inserer les valeur dans la bdd
        - enregistre dans la bdd
        - ferme la connexion a la bdd
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()
    
    mdp = "root"
    mdp += """
                What's new Scooby-Doo?
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

    curseur.execute(" INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)", (None, 1, "root", "root", mdp_crypter, "root@admin.fr"))
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
        - salage + hashage de mot de passe
        - executer la requette pour selectionner dans le tableau user et verifier que l'adresse mail, mot de passe corresponde bien
        - enregistre dans une variable les données recuperer 
        - ferme la connexion a la bdd
        - retourne les données 
    """
    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    mdp += """
                What's new Scooby-Doo?
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

def select_user_admin () :
    """ selectionner les utilisateur pour l'admin """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor()  

    curseur.execute("SELECT * FROM user")

    reponse = curseur.fetchall()
    connexion.close()
    return reponse

def creer_ordinateur (marque, processeur, carte_graphique, ram, disque) :
    """créer un ordinnateur dans la base de données

    Args:
        marque (string): ajout de la marque
        processeur (string): ajout du processeur
        carte_graphique (string): ajout de la carte graphique (si en possède une)
        ram (string): ajout du nombre de ram (Go)
        disque (string): ajout de l'espace du disque dur (Go ou To)
    """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor()   

    curseur.execute("INSERT INTO ordinateur VALUES (?, ?, ?, ?, ?, ?)" , (None, marque, processeur, carte_graphique, ram, disque))

    connexion.commit()
    connexion.close()



def delete_ordinateur (id) :
    """fonction pour supprimer un ordinnateur de la base de données

    Args:
        id (int): recupére l'id de l'ordinnateur
    """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor() 

    curseur.execute("DELETE FROM ordinateur WHERE id = ?", (id,))

    connexion.commit()
    connexion.close()


def select_ordinateur() :
    """selectionne tout les ordinnateur et retourne le tableau conplet

    Returns:
        variable: renvoi reponse qui contient le tableau conplet des ordinnateur
    """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor() 

    curseur.execute ("SELECT id, marque FROM ordinateur")

    reponse = curseur.fetchall()
    connexion.close() 
    return reponse


def creer_carnet(reference_pc, id_user, id_ordinateur) :
    """fonction pour créer le carnet de prêt pour les ordinnateur

    Args:
        reference_pc (int): ajout la référence du pc
        id_user (int): ajout de l'id de l'utilisateur 
        id_ordinateur (int): ajout de l'id de l'ordinnateur
    """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor()   

    curseur.execute("INSERT INTO carnet_pret VALUES (?, ?, ?)", (reference_pc, id_user, id_ordinateur))

    connexion.commit()
    connexion.close()


def delete_carnet(reference_pc) :
    """fonction pour supprimer un carnet de prêt

    Args:
        reference_pc (int): reprend la référence du pc 
    """

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor()  

    curseur.execute ("DELETE FROM carnet_pret WHERE reference_pc = ?", (reference_pc, ))

    connexion.commit()
    connexion.close()


def select_carnet() :

    connexion = sqlite3.Connection ('bdd.sql')
    curseur = connexion.cursor()   

    curseur.execute ("SELECT id_ordinateur, marque FROM carnet_pret INNER JOIN ordinateur ON carnet_pret.id_ordinateur = ordinateur.id")

    reponse = curseur.fetchall()
    connexion.close() 
    return reponse

def creer_ticket(id_pret, message) :
    """crée un ticket 

    Args:
        id_pret (int): ajout de l'id du carnet prêt
        message (string): ajout du message entrez par l'utilisateur
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)", (None,datetime.today().strftime('%Y-%m-%d'), id_pret, "En cours", message))

    connexion.commit()
    connexion.close()

# id de l'utilisateur
def select_ticket() :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT id, message FROM Ticket WHERE status = ?", ("En cours", ))
    resultat = curseur.fetchall()

    connexion.close()
    return resultat

def chat_ticket(id_ticket, utilisateur, chat_bot) :
    """ crée un chat entre l'utilisateur et admin

    Args:
        id_ticket (int): ajout de l'id du ticket en cours
        utilisateur (string): ajout du nom de la personne
        chat_bot (string): ajout du message de la personne (utilisateur, admin)
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()


    curseur.execute("INSERT INTO Chat_Ticket VALUES (?, ?, ?, ?)", (None, id_ticket, utilisateur, chat_bot))

    connexion.commit()
    connexion.close()

def supprimer_ticket(id_ticket) :
    """fonction pour supprimer le ticket

    Args:
        id (int): l'id du ticket
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM Ticket WHERE id = ?", (id_ticket, ))

    connexion.commit()
    connexion.close()

def mise_a_jour(id_status) :
    """mise a jour du ticker

    Args:
        status (string): change le status
    """

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("UPDATE Ticket SET status = 'terminé' WHERE id = ?", (id_status, ))
   
    connexion.commit()
    connexion.close()

def calcul_pc () :
    """ fonction pour avoir le nombre total de pc préter"""

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM carnet_pret")
    resultat = curseur.fetchone()
    connexion.close()
    return resultat

def tickets (status) :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM Ticket WHERE status = ?", (status, ))
    resultat = curseur.fetchone()
    connexion.close()
    return resultat


def select_id_user () :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("SELECT id FROM user")
    resultat = curseur.fetchall()
    connexion.close()
    return resultat