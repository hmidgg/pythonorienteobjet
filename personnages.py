class Personnage:

    nb_personnages = 0

    def __init__(self, nom, energie=100, humeur=50):
        self.nom = nom
        self.energie = self.borner(energie)
        self.humeur = humeur
        Personnage.nb_personnages += 1

    @staticmethod
    def borner(valeur, mini=0, maxi=100):
        return max(mini, min(maxi, valeur))

    @classmethod
    def nombre_total(cls):
        return cls.nb_personnages

    def afficher(self):
        print("nom est:", self.nom)
        print("energie:", self.energie)
        print("humeur est:", self.humeur)

    def modifier_energie(self, delta):
        self.energie = self.borner(self.energie + delta)
        return self.energie

    def est_epuise(self):
        return self.energie == 0

    def reagir(self, situation):
        return -(situation.chaos_de_base() // 6)

    def agir(self, situation):
        if self.est_epuise():
            return 0

        self.modifier_energie(-situation.cout_energie())
        return self.reagir(situation)
