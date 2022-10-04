import sqlite3

connexion = sqlite3.Connection("bdd.sql")
curseur = connexion.cursor()

def crée_tableaux () :

    curseur.execute ('''CREATE TABLE Ticket
                    (
                        id INTEGER PRIMARY KEY,
                        date_de_création DATE,
                        id_pret INT,
                        status INT,
                        message VARCHAR (255) 
                    )
    ''')

    curseur.execute ('''CREATE TABLE Chat_Ticket
                    (
                        id INTEGER PRIMARY KEY,
                        id_ticket INT,
                        auteur VARCHAR (50),  
                        message VARCHAR (255)
                    )
    ''')