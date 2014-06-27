# -*- coding: utf-8 -*-
from math import sqrt


def sieb(x, y):
    """Sieb des Eratosthenes anwenden"""
    # Ausgangssituation
    prim = ['none', 2]

    # Primzahlfeld aus ungeraden Zahlen wird aufgebaut
    for i in range(3, x + 1, 2):
        prim.append(i)

    for k in range(2, (len(prim) - 1)):
        if k in range(2, (len(prim) - 1)):
            # gehe jeweils zur nächsten sicheren Primzahl im primay
            b = prim[k]
            # Alle Vielfachen von b suchen
            for j in range(b * b, prim[-1], b):
                if j in prim:
                    # Vielfache b in prim suchen und löschen
                    prim.remove(j)

    # y-te Primzahl zurückgeben
    return prim[y]


def main():
    print sieb(3000, 100)

if __name__ == '__main__':
    main()
