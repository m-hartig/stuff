from datetime import datetime, timedelta
from json import load, dump
from sys import argv, exit

ABKUERZUNG_ZU_FACH = {"D": "Deutsch", "Ma": "Mathematik",
                      "Ru": "Russisch", "Eng": "Englisch"}

try:
    with open("aufgaben.txt") as aufgaben_datei:
        AUFGABEN = load(aufgaben_datei)

except FileNotFoundError:
    # Wenn die Datei leer ist ...
    with open("aufgaben.txt", "w") as aufgaben_datei:
        # ... soll ein leeres Dict eingefuegt werden
        dump(dict(), aufgaben_datei)
        AUFGABEN = load(aufgaben_datei)


def schnell_aufgabe_erstellen(fach, thema):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    AUFGABEN[abkz_expandieren(fach)] = [
        str(datetime.today() + timedelta(days=1)), thema, False]


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))

    AUFGABEN[abkz_expandieren(fach)] = [
        str(datum_auswerten(datum)), thema, note]


def aufgabe_entfernen():
    """Entfernen einer bestehenden Aufgabe"""
    fach = raw_input("Welches Fach: ")
    del AUFGABEN[abkz_expandieren(fach)]


def abkz_expandieren(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    return ABKUERZUNG_ZU_FACH.get(fach, fach)


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    try:
        # Deutsches Datum
        tag, monat, jahr = map(int, datum.split("."))
    except:
        # Internationales Datum
        jahr, monat, tag = map(int, datum.split("-"))

    return datetime(jahr, monat, tag)


def countdown_berechnen(datum):
    """Berechnen der noch verbleibenden Zeit"""
    # Addieren mit 1, da heutiger Tag mitgerechnet werden soll
    return (datum_auswerten(datum) - datetime.now()).days + 1


def ausgabe_der_aufgaben():
    """Ausgabe aller Aufgaben"""
    for key, value in sorted(AUFGABEN.iteritems()):
        print "%s - noch %d Tag(e)" % (key, countdown_berechnen(value[0][:10]))
        for eintrag in value:
            print eintrag
        print


def hauptmenue_ausgeben(menue):
    while True:
        print "=== Aufgabenverwaltung ==="

        for index, item in enumerate(menue, 1):
            print "{}  {}".format(index, item[0])
        auswahl = input("> ") - 1
        print

        if 0 <= auswahl < len(menue):
            menue[auswahl][1]()
        else:
            print "Nur Zahlen im Bereich 1 - {} eingeben".format(len(menue))


def programm_beenden():
    print "Danke, dass du dieses Programm genutzt hast!"
    exit()


def main():
    """Hauptfunktion"""

    menue = [
        ["Alle Aufgaben anzeigen", ausgabe_der_aufgaben],
        ["Neue Aufgabe anlegen", neue_aufgabe],
        ["Aufgabe entfernen", aufgabe_entfernen],
        ["Programm beenden", programm_beenden]
    ]

    if argv[1:]:
        script, fach, thema = argv
        schnell_aufgabe_erstellen(fach, thema)
        with open("aufgaben.txt") as aufgaben_datei:
            dump(AUFGABEN, aufgaben_datei, "w")
    else:
        hauptmenue_ausgeben(menue)
        with open("aufgaben.txt") as aufgaben_datei:
            AUFGABEN = load(aufgaben_datei)
            dump(AUFGABEN, aufgaben_datei, "w")


if __name__ == '__main__':
    main()



# Was noch fehlt/zu tun ist
# ======
# Schnellaufgabe funktioniert nicht
# Sortieren nach noch verbleibender Zeit + Note
