def creer_ticket(id_pret, message):
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO Ticket VALUES (?, ?, ?, ?, ?)", (None,datetime.today().strftime('%Y-%m-%d'), id_pret, "En cours", message))
    connexion.commit()
    connexion.close()

def user_total () :
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM user")
    resultat = curseur.fetchone()
    connexion.close
    return resultat

def ticket_en_cours () :
    connexion = sqlite3.connect("bdd.sql")
    curseur = connexion.cursor()

    curseur.execute(" SELECT COUNT() FROM Ticket")
    resultat = curseur.fetchone()
    connexion.close
    return resultat