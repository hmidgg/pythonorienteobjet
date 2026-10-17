from personnages import Personnage
from situations import Situation
def main():
    print(Personnage.nombre_total())
    a=Personnage("A")
    b=Personnage("B")
    print(Personnage.nombre_total())
    print(Personnage("Test").reagir(Situation.incendie(4)))
if __name__ == "__main__":
    main()

