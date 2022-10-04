import sqlite3

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

# creation de la table "utilateur" '(id, role, prenom, nom, mdp)
curseur.execute('''
                CREATE TABLE utilisateur
                (
                    id INTEGER PRIMARY KEY,
                    role INTEGER,
                    prenom TEXT,
                    nom TEXT,
                    mdp TEXT
                )
                '''
)

connexion.commit()
connexion.close()
