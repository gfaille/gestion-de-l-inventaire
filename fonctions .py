
import sqlite3
from types import NoneType


connexion = sqlite3.Connection("bdd.db")
curseur = connexion.cursor()

#crer un ordinateur( id, marque, processeur, carte_graphique, ram, disque)
def creer_ordinateur (marque, processeur, carte_graphique, ram, disque):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO ordinateur VALUES (?, ?, ?, ?, ?, ?)" , (None, marque, processeur, carte_graphique, ram, disque))
    connexion.commit()
    connexion.close()

'''
creer_ordinateur("Apple", "M1", "M1", 8, 512 )
creer_ordinateur("Apple", "M2", "M2", 8, 512 )
creer_ordinateur("ASUS", "A12", "RTX2035", 16, 512 )
creer_ordinateur("ASUS", "A15", "RTX2045", 32, 512 )
creer_ordinateur("HP", "H55", "ABC100", 16, 512 )
creer_ordinateur("HP", "H65", "ABC500", 8, 1000 )


creer_ordinateur("Apple", "M2", "M2", 8, 512 )
creer_ordinateur("DENFER", "696", "FEU", 9, 969 )
creer_ordinateur("DENFER", "812", "FIRE", 9, 218)
creer_ordinateur("Apple", "M4", "M4", 128, 4000 )
'''


def delete_ordinateur ( id):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute(("DELETE FROM ordinateur WHERE id=?"), (id,))
    connexion.commit()
    connexion.close()

#delete_ordinateur (2) 



def lire_données_ordinateur ( id):
    connexion = sqlite3.Connection ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("SELECTALL * FROM ordinateur WHERE  id = ? ") , (id)
    connexion.close()
    reponse=curseur.fetchall()
    print(reponse) 
    return reponse 
   


#lire_données_ordinateur(5)







"""
marque=input ("Entrez la marque de l'ordinateur")
processeur= input("Entrez le type de processeur")
carte_graphique=input ("Entrez la reference de la carte graphique")
ram=input ("Entrez la capacité de la ram")
disque=input ("Entrez la capacite du disque dur")
crud.creer_ordinateur(marque, processeur, carte_graphique, ram, disque)
"""

def creer_carnet(reference_pc, id_user, id_ordinateur):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute("INSERT INTO carnet_pret VALUES (?, ?, ?)" , (reference_pc, id_user, id_ordinateur))
    connexion.commit()
    connexion.close()



    
creer_carnet("pccompta", None, 5)
creer_carnet("pcgame", None, None)
creer_carnet("pcpaie", None, 3)


def delete_carnet(reference_pc):
    connexion = sqlite3.connect ('bdd.db')
    curseur = connexion.cursor()   
    curseur.execute ("DELETE FROM carnet_pret WHERE reference_pc=?"), (reference_pc)
    connexion.commit()
    connexion.close()

#delete_carnet("pcpaie")