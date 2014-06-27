
from urllib2 import urlopen
import wolframalpha


def molare_masse_abrufen(stoff_name):
    """ Verbindung zu wolframalpha herstellen und molare Masse abfragen """
    try:
        client = wolframalpha.Client('888685-EEAL3LYL9H')
        res = client.query(
            'molar mass of %s' % stoff_name)
        molare_masse = str(next(res.results).text)
        return float(molare_masse[:7])

    except:
        print "Verbindung konnte nicht hergestellt werden. M = 0"
        return 0


def auswertung(base_name, base_liter, saeure_name, saeure_c, saeure_liter):
    """Ergebnisse berechnen"""
    base_c = saeure_c * saeure_liter / base_liter
    base_n = base_c * base_liter
    base_masse = base_n * molare_masse_abrufen(base_name)
    saeure_n = saeure_c * saeure_liter
    saeure_masse = saeure_n * molare_masse_abrufen(saeure_name)

    return [["S1 c", base_c], ["S1 n", base_n], ["S1 m", base_masse], ["S2 n", saeure_n], ["S2 m", saeure_masse]]


def eingabe_abfragen():
    """Abfrage der Werte"""
    base_name = "KOH"
    base_liter = 0.034
    saeure_name = "HNO3"
    saeure_c = 0.05
    saeure_liter = 0.028

    return [base_name, base_liter, saeure_name, saeure_c, saeure_liter]


def main():
    """Hauptfunktion"""
    eing = eingabe_abfragen()
    ergebnisse = auswertung(eing[0], eing[1], eing[2], eing[3], eing[4])

    for name in ergebnisse:
        for wert in name:
            print wert
        print

if __name__ == '__main__':
    main()
