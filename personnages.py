class Personnage:

    nb_personnages = 0

    def __init__(self, nom, energie=100, humeur=50):
        self._nom = nom
        self.__energie = self.borner(energie)
        self._humeur = humeur
        Personnage.nb_personnages += 1

    @staticmethod
    def borner(valeur, mini=0, maxi=100):
        return max(mini, min(maxi, valeur))

    @property
    def nom(self):
        return self._nom

    @property
    def humeur(self):
        return self._humeur

    @property
    def energie(self):
        return self.__energie

    @energie.setter
    def energie(self, valeur):
        self.__energie = self.borner(valeur)

    @classmethod
    def nombre_total(cls):
        return cls.nb_personnages

    def modifier_energie(self, delta):
        self.energie = self.energie + delta
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

    def __str__(self):
        return f"{self._nom} (énergie={self.energie}, humeur={self.humeur})"

    def __repr__(self):
        return f"Personnage({self._nom!r}, energie={self.energie})"

    def __eq__(self, autre):
        return isinstance(autre, Personnage) and self._nom == autre._nom
