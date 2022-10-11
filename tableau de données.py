import sqlite3

connexion = sqlite3.Connection("bdd.sql")
curseur = connexion.cursor()

""" fonction pour crée les tableau dans la base de donner 
        les tableau crée sont :
            - Ticket
            - Chat_Ticket
            - ordinateur
            - carnet_pret
            - user
"""

# creation de table "Ticket" (id, date_de_création, id_pret, status, message, foreign key)
curseur.execute ('''CREATE TABLE Ticket
                    (
                        id INT PRIMARY KEY,
                        date_de_création DATE,
                        id_pret INT,
                        status INT,
                        message VARCHAR (255), 
                        FOREIGN KEY (id_pret)
                            REFERENCES Chat_Ticket(id)
                    )
    ''')
# creation de la table "Chat_Ticket" (id, id_ticket, auteur, message, 2 foreign key)
curseur.execute ('''CREATE TABLE Chat_Ticket
                    (
                        id INTEGER PRIMARY KEY,
                        id_ticket INT,
                        auteur VARCHAR (50),
                        message VARCHAR (255),
                        FOREIGN KEY (id_ticket)
                            REFERENCES Ticket(id),
                        FOREIGN KEY (auteur)
                            REFERENCES user(prenom)  
                    )
    ''')



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
                        reference_pc INT PRIMARY KEY,
                        id_user INT,
                        id_ordinateur INT,
                        FOREIGN KEY (id_user)
                            REFERENCES user(id),
                        FOREIGN KEY (id_ordinateur)
                            REFERENCES ordinateur(id)   
                    )
    ''')

     # creation de la table "user" '(id, role, prenom, nom, mdp)
curseur.execute('''
                    CREATE TABLE user
                    (
                        id INTEGER PRIMARY KEY,
                        role INTEGER,
                        prenom VARCHAR (50),
                        nom VARCHAR (50),
                        mdp VARCHAR (255),
                        mail VARCHAR (255)
                    )
    '''
    )


connexion.commit()
connexion.close()

