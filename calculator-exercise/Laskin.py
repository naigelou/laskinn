#Laskin luokka, joka sisältää funktiot(Pluslasku,miinuslasku,kertolasku,jakolasku)
class Laskin:
    def __init__(self):
        """Tallennus paikka laskujen tuloksille."""
        self.valimuisti = 0
    #Pluslasku funktio, joka ottaa kaksi numeroa ja suorittaa plus tehtävän
    def _plus(self,numero1:float,numero2:float):
        """Pluslasku funktio, joka ottaa kaksi numeroa ja suorittaa plus tehtävän
            Examples:
                >>> Laskin()._plus(1,1)
                2
                >>> Laskin()._plus(1,2)
                3
        """
        self.valimuisti = numero1 + numero2
        return numero1 + numero2
    #Miinuslasku funktio, joka ottaa kaksi numeroa ja suorittaa miinus tehtävän
    def _miinus(self,numero1:float,numero2:float):
        """Miinuslasku funktio, joka ottaa kaksi numeroa ja suorittaa miinus tehtävän
            Examples:
                >>> Laskin()._miinus(1,1)
                0
                >>> Laskin()._miinus(5,2)
                3
        """
        self.valimuisti = numero1 - numero2
        return numero1 - numero2
    #Kertolasku funktio, joka ottaa kaksi numeroa ja suorittaa kertolasku tehtävän
    def _kertolasku(self,numero1:float,numero2:float):
        """Kertolasku funktio, joka ottaa kaksi numeroa ja suorittaa kertolasku tehtävän
        Examples:
            >>> Laskin()._kertolasku(1,1)
            1
            >>> Laskin()._kertolasku(2,2)
            4
        """
        self.valimuisti = numero1 * numero2
        return numero1 * numero2
    #jakolasku funktio, joka ottaa kaksi numeroa ja suorittaa kertolasku tehtävän
    def _jakolasku(self,numero1:float,numero2:float):
        """jakolasku funktio, joka ottaa kaksi numeroa ja suorittaa kertolasku tehtävän
        Examples:
            >>> Laskin()._jakolasku(1,1)
            1.0
            >>> Laskin()._jakolasku(2,2)
            1.0
        """
        #Jos käyttäjä koittaa jakaa nollalla, nostaa ohjelma ValueErrorin.
        if numero2 == 0:
            raise ValueError("Nollalla ei voi jakaa")
        self.valimuisti = numero1 / numero2
        return numero1 / numero2


#Koodinsuoritus
if __name__ == "__main__":
    #Esimerkki koodinsuoritusta.
    print(Laskin()._plus(1,2))
    print(Laskin()._miinus(1,2))
    print(Laskin()._kertolasku(1,2))
    print(Laskin()._jakolasku(1,2))