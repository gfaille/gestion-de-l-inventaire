def ticket_en_cours (status) :
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM Ticket WHERE status =?", (status, )
    resultat = curseur.fetchone()
    connexion.close
    return resultat

def ticket_terminé (status) :
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM Ticket WHERE status =?", (status, )
    resultat = curseur.fetchone()
    connexion.close
    return resultat

def nb_ticket():
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM Ticket")
    resultat = curseur.fetchone()
    connexion.close
    return resultat