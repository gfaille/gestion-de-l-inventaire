import sqlite3

def creer_user (prenom, nom, mdp) :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?)", (None, 0, prenom, nom, mdp))
    connexion.commit()
    connexion.close()

def creer_admin (prenom, nom, mdp) :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?)", (None, 1, prenom, nom, mdp))
    connexion.commit()
    connexion.close()

def suppr_user (prenom, nom) :

    connexion = sqlite3.Connection("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM user WHERE (?, ?)", (None, prenom, nom))
    connexion.commit()
    connexion.close()
    