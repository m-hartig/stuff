
"""
Das Zoomobjektiv eines Fotoapparates hat eine maximale Brennweite von 300 m. Die Entfernung wird so eingestellt, dass ein 50 m entferner Gegenstand scharf auf dem Film abbgebildet wird. Bei einer Blendeneinstellung von 11 erscheinen die Bilder auch dann noch scharf, wenn das bild 0,2 mm vor oder hinter der Flmebene entsteht. 
Welches Entfernungsintervall wird dann auf dem Bild scharf sein?
"""


class Entfernungsintervall(object):

    def __init__(self, brennweite, gegenstandsweite):

        self.__brennweite = brennweite
        self.__gegenstandsweite = gegenstandsweite

    def bildweite_berechnen(self):
        self.bildweite =  float((self.__brennweite * self.__gegenstandsweite * 1000)) / \
            float((self.__gegenstandsweite * 1000 - self.__brennweite))
        return self.bildweite

    def bildweite1_berechnen(self):
        self.bildweite1 = self.bildweite + 0.2
        return self.bildweite1

    def bildweite2_berechnen(self):
        self.bildweite2 = self.bildweite - 0.1
        return self.bildweite2

    def entfernung1_berechnen(self):
        self.entfernung1 = (self.__brennweite * self.bildweite1) / \
            (self.bildweite1 - self.__brennweite)
        self.entfernung1 /= 1000
        return self.entfernung1

    def entfernung2_berechnen(self):
        self.entfernung2 = (self.__brennweite * self.bildweite2) / \
            (self.bildweite2 - self.__brennweite)
        self.entfernung2 /= 1000
        return self.entfernung2

    def intervall_berechnen(self):
        self.__bildweite = self.bildweite_berechnen()
        self.__bildweite1 = self.bildweite1_berechnen()
        self.__bildweite2 = self.bildweite2_berechnen()
        self.__entfernung1 = self.entfernung1_berechnen()
        self.__entfernung2 = self.entfernung2_berechnen()
        self.__intervall = self.entfernung2 - self.entfernung1
        return self.__intervall

intervall = Entfernungsintervall(300, 50)
print 'Intervall: %f m' % intervall.intervall_berechnen()
