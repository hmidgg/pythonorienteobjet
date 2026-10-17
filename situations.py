class Situation:
    """Situation chaotique."""

    TYPES = ("feu", "eau", "betise")
    COUTS = {"feu": 3, "eau": 2, "betise": 2}

    def __init__(self, nom, gravite, type_danger):
        if not 1 <= gravite <= 10:
            raise ValueError("La gravité doit être comprise entre 1 et 10")

        if not Situation.type_valide(type_danger):
            raise ValueError("Type de danger inconnu")

        self._nom = nom
        self._gravite = gravite
        self._type_danger = type_danger

    @property
    def nom(self):
        return self._nom

    @property
    def gravite(self):
        return self._gravite

    @property
    def type_danger(self):
        return self._type_danger

    @staticmethod
    def type_valide(type_danger):
        return type_danger in Situation.TYPES

    @classmethod
    def incendie(cls, gravite):
        return cls("Incendie", gravite, "feu")

    @classmethod
    def inondation(cls, gravite):
        return cls("Inondation", gravite, "eau")

    @classmethod
    def betise(cls, gravite):
        return cls("Bêtise de Gumball", gravite, "betise")

    def chaos_de_base(self):
        return self._gravite * 10

    def cout_energie(self):
        return self._gravite * Situation.COUTS[self._type_danger]

    def __str__(self):
        return f"{self._nom} (gravité {self._gravite})"

    def __repr__(self):
        return (
            f"Situation({self._nom!r}, {self._gravite}, "
            f"{self._type_danger!r})"
        )