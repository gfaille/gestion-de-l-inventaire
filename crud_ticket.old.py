import sqlite3
from datetime import datetime
# datetime.today().strftime('%Y-%m-%d')

"""Creation d'un ticket avec l'id, la date de cration du ticket, id du pret, son status ainsi que le message"""


"""def creer_ticket(id_pret, message):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)", (None, datetime.today().strftime('%Y-%m-%d'), id_pret, "En cours", message))
    connexion.commit()
    connexion.close()

creer_ticket(66, "Bonjour")"""


"""
def select_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM Ticket WHERE id =?", (id, ))
    resultat = curseur.fetchone()

    connexion.close()
    return resultat

print(select_ticket(1))
"""

"""
def supprimer_ticket(id):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM Ticket WHERE id=?", (id, ))
    connexion.commit()
    connexion.close()

supprimer_ticket(2)
"""


#def mise_a_jour(status):
#    connexion = sqlite3.connect("bdd.sql")
#    curseur = connexion.cursor()

#    curseur.execute("""UPDATE FROM Ticket SET status =? WHERE id =?""", (status, ))
   
#    connexion.commit()
#    connexion.close()


#def statistique_ticket(status):
#    connexion = sqlite3.connect("bdd.sql")
#    curseur = connexion.cursor()

#    curseur.execute("SELECT COUNT FROM Ticket WHERE status =?", (status, ))
#    resultat = curseur.fetchone

def stat_ticket(status):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("""SELECT COUNT (*) FROM Ticket WHERE status =?""", (status, ))
    resultat = curseur.fetchall()

    connexion.close()
    return resultat

print(stat_ticket("En cours"))

def stat_user(role):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("""SELECT COUNT (*) FROM user WHERE role =?""", (role, ))
    resultat = curseur.fetchall()

    connexion.close()
    return resultat

print(stat_user(0))