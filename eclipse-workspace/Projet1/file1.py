class Biblio:
    def __init__(self):
        self.collection = []
    def emprunter_livre(self, livre):
        if livre in self.collection:
            self.collection.remove(livre)
            return f"{livre.titre} a été emprunté"
        else:
            return "Le livre n'est pas disponible"

    def ajouter_livre(self, livre):
        self.collection.append(livre)

    def afficher_collection(self):
        print("Livres disponibles dans la bibliothèque :")
        for livre in self.collection:
            print(f"Titre : {livre.titre}, Auteur : {livre.auteur.nom}")

class Livre:
    def __init__(self,titre,auteur):
        self.titre=titre
        self.auteur=auteur
        
    
class Auteur:
    def __init__(self,nom):
        self.nom=nom

    
auteur1 = Auteur("REDA BELHAJ")
livre1 = Livre("2001", auteur1)
auteur2 = Auteur("George Orwell")
livre2 = Livre("1984", auteur2)

bibliotheque = Biblio()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

result = bibliotheque.emprunter_livre(livre1)
print(result)

bibliotheque.afficher_collection()
