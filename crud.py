import sqlite3
import hashlib

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

def creer_admin (prenom, nom, mdp, mail) :
    """ la fonction pour créer un admin (prenom, nom, mdp) :
        - connexion a la base de donner
        - salage + hashage de mot de passe
        - executer la requette pour inserer les valeur dans la bdd
        - enregistre dans la bdd
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

def changer_mdp (mdp) :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("UPDATE user SET mdp = ? WHERE mdp <> ?", (mdp))
    connexion.commit()
    connexion.close()
    
#crer un ordinateur( id, marque, processeur, carte_graphique, ram, disque)
def creer_ordinateur ( marque, processeur, carte_graphique, ram, disque):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO ordinateur VALUES (?, ?, ?, ?, ?, ?)" , (None, marque, processeur, carte_graphique, ram, disque))
    connexion.commit()
    connexion.close()


#supprimer un ordinateur par son id
def delete_ordinateur ( id):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute(("DELETE FROM ordinateur WHERE id=?"), (id,))
    connexion.commit()
    connexion.close()


#creer un pret sur carnet_carnet(reference_pc, id_user, id_ordinateur)
def creer_carnet(reference_pc, id_user, id_ordinateur):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO carnet_pret VALUES (?, ?, ?)" , (reference_pc, id_user, id_ordinateur))
    connexion.commit()
    connexion.close()


##supprimer un pret  par sa refrence_pc
def delete_carnet(reference_pc):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute (("DELETE FROM carnet_pret WHERE reference_pc=?"), (reference_pc,))
    connexion.commit()
    connexion.close()


#sortir les infos d'une fiche de pret avec id
def select_carnet(reference_pc):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute ("SELECT * FROM carnet_pret WHERE reference_pc=? ", (reference_pc,))
    print (curseur.fetchone())
    reponse=curseur.fetchone()
    connexion.commit()
    connexion.close() 
    return reponse


#sortir les infos d'un ordinateur avec id
def select_ordinateur(id):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute ("SELECT * FROM ordinateur WHERE id=? ", (id,))
    print (curseur.fetchone())
    reponse=curseur.fetchone()
    connexion.commit()
    connexion.close() 
    return reponse

"""Creation d'un ticket avec l'id, la date de cration du ticket, id du pret, son status ainsi que le message"""
def creer_ticket(date_de_creation, id_pret, status, message):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)", (None, date_de_creation, id_pret, status, message))
    connexion.commit()
    connexion.close()

def select_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM Ticket WHERE id =?", (id, ))
    resultat = curseur.fetchone()

    connexion.close()
    return resultat

def supprimer_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM Ticket WHERE id=?", (id, ))
    connexion.commit()
    connexion.close()

def mise_a_jour(status):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("""UPDATE Ticket SET status =? WHERE id =?""", (status, ))
   
    connexion.commit()
    connexion.close()