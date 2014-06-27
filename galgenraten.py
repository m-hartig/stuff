
def eingabe_auswerten(eingabe, aufgabe, lg):
    for x in range(0, len(aufgabe)):
        if eingabe == aufgabe[x]:
            lg[x] = eingabe

    return lg


def eingabe_pruefen(eingabe):
    if len(eingabe) > 1 or len(eingabe) == 0 or ord(eingabe) < 65 or ord(eingabe) > 122:
        return True

    return False


def frage_stellen():
    from random import choice
    aufgaben = ["SCANNER", "MAUS", "TASTATUR", "MAC", "LINUX"]
    return choice(aufgaben)


def main():
    aufgabe = list(frage_stellen())
    lg = ["_"] * len(aufgabe)

    print lg

    for x in range(0, 11):
        eingabe = raw_input("Buchstaben eingeben: ")

        while eingabe_pruefen(eingabe):
            print "Eingabe ungueltig"
            eingabe = raw_input("Buchstaben eingeben: ")

        eingabe = eingabe.upper()

        lg = eingabe_auswerten(eingabe, aufgabe, lg)
        print lg

        if lg == aufgabe:
            print "Gewonnen!"
            break

    else:
        print "Verloren!"


if __name__ == '__main__':
    main()
