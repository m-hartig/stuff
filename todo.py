from datetime import datetime, timedelta
from json import load, dump
from sys import argv


def schnell_aufgabe_erstellen(fach, thema):
    """Schnelles Erstellen einer Aufgabe via Terminal"""
    AUFGABEN[abkz_expand(fach)] = [
        # Termin morgen, da eigentlicher Termin unbekannt
        str(datetime.today() + timedelta(days=1)),
        thema,
        # Keine Benotung, da schnelle Aufgabe meist ohne Note
        False
    ]
    print "Aufgabe wurde erstellt."


def neue_aufgabe():
    """Eingabe einer neuen Aufgabe"""
    fach = raw_input("Fach: ")
    datum = raw_input("Datum: ")
    thema = raw_input("Thema: ")
    note = bool(raw_input("Note? "))

    AUFGABEN[abkz_expand(fach)] = [str(datum_auswerten(datum)), thema, note]


def aufgabe_entfernen():
    """Entfernen einer bestehenden Aufgabe"""
    fach = raw_input("Welches Fach: ")
    if raw_input("Sind Sie sich sicher? ") == "ja":
        del AUFGABEN[abkz_expand(fach)]
    else:
        return


def abkz_expand(fach):
    """Zuordnung der Abkuerzungen zu den Faechern"""
    abkuerzung_zu_fach = {"D": "Deutsch", "Ma": "Mathematik",
                          "Ru": "Russisch", "Eng": "Englisch"}
    return abkuerzung_zu_fach.get(fach, fach)


def datum_auswerten(datum):
    """Datum wird zur Weiterverabeitung bearbeitet"""
    try:
        tag, monat, jahr = map(int, datum.split("."))
    except:
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


def programm_beenden():
    """Beenden des Programmes"""
    print "Danke, dass du dieses Programm genutzt hast!"


def programm_steuern(menue):
    """Steuerung des Programmes ueber ein Menue"""
    while True:
        print "=== Aufgabenverwaltung ==="
        for index, item in enumerate(menue, 1):
            print "{}  {}".format(index, item[0])

        auswahl = raw_input("> ")
        if "end" in auswahl:
            break

        print
        auswahl = int(auswahl) - 1
        if 0 <= auswahl < len(menue):
            menue[auswahl][1]()
        else:
            print "Nur Zahlen im Bereich 1 - {} eingeben".format(len(menue))


menue = [
    ["Alle Aufgaben anzeigen", ausgabe_der_aufgaben],
    ["Neue Aufgabe anlegen", neue_aufgabe],
    ["Aufgabe entfernen", aufgabe_entfernen],
    ["Programm beenden", programm_beenden]
]

with open("aufgaben.txt", "w") as aufgaben_datei:
    try:
        AUFGABEN = load(aufgaben_datei)
    except:
        AUFGABEN = dict()

    if argv[1:]:
        # Wenn Paramter uebergeben wurden
        script, fach, thema = argv
        schnell_aufgabe_erstellen(fach, thema)
        dump(AUFGABEN, aufgaben_datei, "w")
    else:
        programm_steuern(menue)
        dump(AUFGABEN, aufgaben_datei)


# Was noch fehlt/zu tun ist
# ======
# Datei wird nicht gespeichert
# Datumseingabe, MenueEingabe ueberpruefen lassen
# Programm-Beenden ueberarbeiten
# Excpet in datum_auswerten praezisieren
# Schnellaufgabe funktioniert nicht
# Sortieren nach noch verbleibender Zeit + Note
