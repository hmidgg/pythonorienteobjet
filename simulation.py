class Equipe:
    

    def __init__(self, membres=None):
        self._membres = list(membres) if membres else []

    def ajouter(self, personnage):
        self._membres.append(personnage)

    def retirer(self, personnage):
        self._membres.remove(personnage)

    @property
    def membres(self):
        # Renvoie une copie de la liste.
        return self._membres.copy()

    def __str__(self):
        return ", ".join(personnage.nom for personnage in self._membres)


class Journal:
    

    def __init__(self):
        self._entrees = []

    def enregistrer(self, nom, chaos):
        self._entrees.append((nom, chaos))

    def entrees(self):
        return list(self._entrees)  # Renvoie une copie de la liste

    def total(self):
        return sum(chaos for _, chaos in self._entrees)


class Simulation:

    SEUIL_CHAOS = 100

    def __init__(self, equipe):
        # Agrégation : l'équipe est créée à l'extérieur.
        self._equipe = equipe

        # Composition : le journal est créé par la simulation.
        self._journal = Journal()

    @property
    def chaos(self):
        return self._journal.total()

    @property
    def historique(self):
        return self._journal.entrees()

    def est_perdue(self):
        return self.chaos >= self.SEUIL_CHAOS

    def jouer_tour(self, situation):
        somme_reactions = sum(
            personnage.agir(situation) for personnage in self._equipe.membres
        )
        chaos_tour = max(0, situation.chaos_de_base() + somme_reactions)
        self._journal.enregistrer(situation.nom, chaos_tour)
        return chaos_tour

    def lancer(self, situations):
        for situation in situations:
            if self.est_perdue():
                break

            self.jouer_tour(situation)

        if self.est_perdue():
            return "DÉFAITE : trop de chaos"

        return "VICTOIRE : Elmore est sauvée"
