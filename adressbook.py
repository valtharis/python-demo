class Adres(object):
    def __init__(self,ulica = "ulica",miasto = "miasto"):
        self.ulica = ulica
        self.miasto = miasto
    def __str__(self):
        return "{} {}".format(self.ulica, self.miasto)
    def get(self):
        return {'ulica':self.ulica, 'miasto':self.miasto}

class Osoba(object):
    def __init__(self,imieNazwisko = "imie_nazwisko", adres = Adres()):
        self.adres = adres
        self.imieNazwisko = imieNazwisko
    def __str__(self):
        return "{} {}".format(self.imieNazwisko, self.adres)
    def get(self):
        return {'imieNazwisko':self.imieNazwisko,'adres':self.adres.get()}


class Kontakt(object):
    def __init__(self,osoba = Osoba(), email = "email"):
        self.osoba = osoba
        self.email = email
    def __str__(self):
        return "{} {}".format(self.osoba, self.email)
    def get(self):
        return {'osoba':self.osoba.get(),'email':self.email}

class Ksiazka(object):
    def __init__(self):
        self.list = {}
    def __str__(self):
        result = ''
        for kontakt in self.list:
            result += str(self.list[kontakt])+"\n"
        return result
            
    def dodaj(self, imieNazwisko = "imieNazwisko", email = "email", ulica = "ulica", miasto = "miasto"):
        adres = Adres(ulica, miasto)
        osoba = Osoba(imieNazwisko, adres)
        kontakt = Kontakt(osoba, email)
        self.list[imieNazwisko] = kontakt
        


#adr = Adres()
#print(adr)
#o = Osoba()
#print(o)
k = Kontakt()
#print(k.get())
#print(str(k))

ksiazka = Ksiazka()
ksiazka.dodaj("ala","email@wd")
ksiazka.dodaj("tomek")
ksiazka.dodaj("aga")
ksiazka.dodaj("marcin")

print(ksiazka)