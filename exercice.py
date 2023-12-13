from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number -= number*2
    return int(number)


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for i in prefixes:
        liste.append(i+suffixe)
    return liste


def prime_integer_summation() -> int:
    def is_prime(nombre):
        if nombre == 1:
            return False
        for i in range(2,nombre):
            if nombre % i == 0:
                return False
        return True
    compteur = 0
    nombre = 0
    for i in range(1, 1000):
        if is_prime(i):
            nombre += i
            compteur += 1
            if compteur == 100:
                return nombre

def factorial(number: int) -> int:
    nombre = 1
    for i in range(1,number+1):
        nombre *= i
    return nombre


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    def contient_25(liste):
        for i in liste:
            if i == 25:
                return True
        return False
    def contient_50(liste):
        for i in liste:
            if i == 50:
                return True
        return False
    liste = []
    for i in range(len(groups)):
        if 10 < len(groups[i]) or len(groups[i]) <= 3:
            liste.append(False)
        else:
            for j in groups[i]:
                groups[i].sort()
                print(groups[i])
                if groups[i][-1] > 70 and contient_50(groups[i])==True and contient_25(groups[i]) == False:
                    liste.append(False)
                    break
                elif j < 18 and contient_25(groups[i]) == False:
                    liste.append(False)
                    break
                else:
                    liste.append(True)
                    break
    return liste


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
