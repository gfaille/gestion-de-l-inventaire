import sqlite3
from datetime import datetime
# datetime.today().strftime('%Y-%m-%d')

"""Creation d'un ticket avec l'id, la date de cration du ticket, id du pret, son status ainsi que le message"""


def creer_ticket(date_de_creation, id_pret, status, message):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)", (None, date_de_creation, id_pret, status, message))
    connexion.commit()
    connexion.close()

date_du_jour = datetime.today().strftime('%Y-%m-%d')

creer_ticket(date_du_jour, 1, "Nouveau", "Bonjour")



def select_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM Ticket WHERE id =?", (id, ))
    resultat = curseur.fetchone()

    connexion.close()
    return resultat

print(select_ticket(1))



def supprimer_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM Ticket WHERE id=?", (id, ))
    connexion.commit()
    connexion.close()

supprimer_ticket(2)



def mise_a_jour(status):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("""UPDATE Ticket SET status =? WHERE id =?""", (status, ))
   
    connexion.commit()
    connexion.close()