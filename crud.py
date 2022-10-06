
import sqlite3
from types import NoneType


connexion = sqlite3.Connection("bdd.db")
curseur = connexion.cursor()
'''
#crer un ordinateur( id, marque, processeur, carte_graphique, ram, disque)
def creer_ordinateur ( marque, processeur, carte_graphique, ram, disque):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO ordinateur VALUES (?, ?, ?, ?, ?, ?)" , (None, marque, processeur, carte_graphique, ram, disque))
    connexion.commit()
    connexion.close()


#supprimer un ordinateur par son id
def delete_ordinateur ( id):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute(("DELETE FROM ordinateur WHERE id=?"), (id,))
    connexion.commit()
    connexion.close()


#creer un pret sur carnet_carnet(reference_pc, id_user, id_ordinateur)
def creer_carnet(reference_pc, id_user, id_ordinateur):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO carnet_pret VALUES (?, ?, ?)" , (reference_pc, id_user, id_ordinateur))
    connexion.commit()
    connexion.close()


##supprimer un pret  par sa refrence_pc
def delete_carnet(reference_pc):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute (("DELETE FROM carnet_pret WHERE reference_pc=?"), (reference_pc,))
    connexion.commit()
    connexion.close()
'''

#sortir les infos d'une fiche de pret avec id
def select_carnet(reference_pc):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute ("SELECT * FROM carnet_pret WHERE reference_pc=? ", (reference_pc,))
    print (curseur.fetchone())
    reponse=curseur.fetchone()
    connexion.commit()
    connexion.close() 
    return reponse


#sortir les infos d'un ordinateur avec id
def select_ordinateur(id):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute ("SELECT * FROM ordinateur WHERE id=? ", (id,))
    print (curseur.fetchone())
    reponse=curseur.fetchone()
    connexion.commit()
    connexion.close() 
    return reponse

select_ordinateur(4)