#Importtaa laskin.py:stä Laskin classin.
from Laskin import Laskin
lasku = Laskin()
# kuusi eri funktiota jotka testaavat Laskin classin funktiot läpi.
def test_plus():
    lasku._plus(1,2)
def test_minus():
    lasku._miinus(1,2)
def test_kerto():
    lasku._kertolasku(1,2)
def test_jako():
    lasku._jakolasku(1,2)
#Testataan myös nollalla, jakamisen errorin löytäminen.
def test_jakonollalla():
    try:
        lasku._jakolasku(1,0)
    except ValueError:
        print("Errorin testaus onnistui")
def test_valimuisti():
    print(lasku.valimuisti)

    