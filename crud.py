from distutils.util import execute
import sqlite3
connexion = sqlite3.connect ('bdd.db')
curseur = connexion.cursor()


#creation de la table "ordinateur" ( id, marque, processeur, carte graphique, ram, disque)
curseur.execute ('''CREATE TABLE ordinateur
                (
                id INTEGER PRIMARY KEY,
                marque TEXT,
                processeur TEXT,
                carte graphique TEXT,
                ram TEXT,
                disque TEXT
               
                )
''')




connexion.commit()
connexion.close()

#def get_admin():