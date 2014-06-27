
def median_berechnen(daten):
    """Berechnet den Median einer Datenreihe"""
    daten = sorted(daten)
    lg = len(daten)

    if lg % 2 != 0:
        return daten[lg / 2]

    if lg % 2 == 0:
        # Index beginnt bei 0
        return (daten[lg / 2] + daten[lg / 2 - 1]) / 2.0


def main():
    daten = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    print median_berechnen(daten)

if __name__ == '__main__':
    main()
