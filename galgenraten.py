
def eingabe_auswerten(eingabe, aufgabe, lg):
    """Einsetzen der Eingabe in die Loesung"""
    for x in range(0, len(aufgabe)):
        # Wenn die Eingabe ein Buchstabe der Lsg ist ...
        if eingabe == aufgabe[x]:
            # ... wird an der entsprechenden Position die Eingabe eingesetzt
            lg[x] = eingabe
    return lg


def eingabe_pruefen(eingabe):
    """Pruefen der Eingabe auf Laenge und Zeichen"""
    if len(eingabe) > 1 or len(eingabe) == 0 or ord(eingabe) < 65 or ord(eingabe) > 122:
            return True
    return False


def frage_stellen():
    """Eine zufaellige Aufgabe stellen"""
    from random import choice
    aufgaben = ["SCANNER", "MAUS", "TASTATUR", "MAC", "LINUX"]
    return choice(aufgaben)


def main():
    """Hauptfunktion"""
    aufgabe = list(frage_stellen())
    lg = ["_"] * len(aufgabe)

    print " ".join(lg)

    # Der Spieler hat 10 Versuche
    for x in range(0, 11):
        eingabe = raw_input("> ")

        # Solange die Eingabe ungueltig ist
        while eingabe_pruefen(eingabe):
            print "Eingabe ungueltig"
            eingabe = raw_input("Buchstaben eingeben: ")

        lg = eingabe_auswerten(eingabe.upper(), aufgabe, lg)
        print "\n", " ".join(lg)

        if lg == aufgabe:
            print "\nGewonnen!"
            break

    else:
        print "Verloren!"


if __name__ == '__main__':
    main()
