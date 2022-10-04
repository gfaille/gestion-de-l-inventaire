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


#creation de la base de données carnet de pret (reference du pret, > id user, id ordinateur)
curseur.execute ('''CREATE TABLE carnet_pret
                (
                reference TEXT,
                id_user TEXT,
                id_ordinateur TEXT,
                FOREIGN KEY (user_id)
                    references user(id)
                 FOREIGN KEY (ordinateur_id)
                    references ordinateur(id)   
                    ON DELETE CASCADE
                )
''')


connexion.commit()
connexion.close()

#def get_admin():