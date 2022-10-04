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

# creation d'une fonction pour creer un utilisateur (role, prenom, nom, mdp)
def create_user(role, prenom, nom, mdp):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO utilisateur VALUES (?, ?, ?, ?, ?)", (None, role, prenom, nom, mdp))
    connexion.commit()
    connexion.close()