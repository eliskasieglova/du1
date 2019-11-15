import math             #na používání radiánů,ln,sin,cos,tan
from turtle import forward,backward,right,left,exitonclick,speed,penup,pendown

#otázka na zobrazení
zobrazeni = input("Vyber zobrazení (A=Marinovo, B=Braunovo, M=Mercatorovo, L=Lambertovo): ")
while zobrazeni != "L" and zobrazeni != "A" and zobrazeni != "B" and zobrazeni != "M":
    zobrazeni = input("Zadali jste neplatné zobrazení. Zkuste to znovu: ")
#dotaz na měřítko
meritko = int(input("Zadej měřítko. 1 : "))
while meritko <= 0:
    meritko = input("Zadali jste neplatné měřítko. Zkuste to znovu. 1 : ")
#dotaz na poloměr Země:
R = (float(input("Zadejte poloměr Země: ")))*100000
while R < 0:
    R = (float(input("Zadejte poloměr Země: "))) * 100000
if R == 0 or not R:
    R=6371.11*100000

#vytvoření seznamů
poledniky = [ ]
rovnobezky = [ ]

def vypis(zobrazeni,meritko,poledniky,rovnobezky):
    """vypise zobrazeni, meritko, poledniky a rovnobezky"""
    print()
    if zobrazeni == "A":
        print("Marinovo zobrazení")
    elif zobrazeni == "B":
        print("Braunovo zobrazení")
    elif zobrazeni == "M":
        print("Mercatorovo zobrazení")
    elif zobrazeni == "L":
        print("Lambertovo zobrazení")
    print("1 :",meritko)
    print("Rovnoběžky:", end=" ")
    nahradit_velke_hodnoty(rovnobezky)
    print()
    print("Poledníky: ", end= " ")
    nahradit_velke_hodnoty(poledniky)

def spocti_delku(R,stupen_sirka,meritko):
    """vrati souradnice poledniku podle vzorecku x=R*v"""
    return ((R * math.radians(stupen_sirka)) / meritko)

def spocti_sirku(zobrazeni,stupen_sirka, meritko, R):
    """vrati souradnice rovnobezek podle zobrazeni"""
    if zobrazeni == "A":  # Marinovo:  x=R*v   y=R*u
        return (((R * math.radians(stupen_sirka)) / meritko))
    elif zobrazeni == "M":  # Mercatorovo:  x=R*v   y=R*ln(cotg(fi/2))
        return((R * math.log((1 / ((math.tan((math.radians(stupen_sirka)) / 2))))) / meritko))
    elif zobrazeni == "B":  # Braunovo:     x=R*v   y=2*R*tg(u/2)
        return(((2 * R * math.tan((math.radians(stupen_sirka)) / 2)) / meritko))
    elif zobrazeni == "L":  # Lambertovo:   x=R*v   y=R*sin(u)
        return((R * math.sin(math.radians(stupen_sirka)) / meritko))

def nahradit_velke_hodnoty(seznam):
    """nahradi hodnoty v seznamu vetsi nez 1 m pomlckou"""
    for i in seznam:
        if i  < -100 or i > 100:
            print("-", end=", ")
        else:
            print(i, end=", ")
#konec funkci pro vypocet a vypis rovnobezek a poledniku

#vypocet rovnobezek:
if zobrazeni == "M":
    #pokud si uzivatel vybere Mercatorovo zobrazeni, je potreba vyjimka (poly lezi v nekonecnu)
    for stupen_sirka in range(80, 9, -10):
        rovnobezka_bod = spocti_sirku(zobrazeni, stupen_sirka, meritko, R)
        rovnobezky.append(round(rovnobezka_bod, 1))
    #přidám 0 na první (nulté) místo v seznamu
    rovnobezky.insert(0, 0)
    #projedu seznam rovnobezky[], přidávám záporné hodnoty na první (nulté) místo v seznamu
    for x in list(rovnobezky):
        if x != 0:
            rovnobezky.insert(0,-x)
else:
    #pro ostatni zobrazeni plati:
    for stupen_sirka in range(-90, 91, 10):
        rovnobezka_bod = spocti_sirku(zobrazeni, stupen_sirka, meritko, R)
        rovnobezky.append(round(rovnobezka_bod, 1))

#vypocet poledniku - pro vsechny zobrazeni stejne
for stupen_delka in range(-180, 181, 10):
    polednik_bod = spocti_delku(R,stupen_delka, meritko)
    poledniky.append(round(polednik_bod, 1))

vypis(zobrazeni,meritko,poledniky,rovnobezky)
#konec casti programu, ktera pocita a vypisuje rovnobezky a poledniky

#####################zacatek zelvy

#užitečné zkratky pro kreslení mřížky:
rovnobezka_delka = poledniky[-1] * 10 #délka půlky rovnoběžky (*10 na cm) (dosadit za delku posunu, kdyz chci kreslit rovnobezky)
polednik_delka = rovnobezky[-1] * 10 #délka půlky poledníku (dosadit za delku posunu, kdyz chci kreslit poledniky)
polednik_delka_mercator = rovnobezky[-1] * 10 + 30 #výjimka pro Mercatorovo zobrazení (póly leží v nekonečnu)
#funkce pro zelvu
#pro kresleni rovnobezek dosadim rovnobezka_delka, pro kresleni poledniku polednik_delka
def kresli(delka_posunu):
    forward(delka_posunu)
    backward(2 * delka_posunu)
    forward(delka_posunu)

def posun_o_10_stupnu(seznam,index):
    """posouva zelvu o 10 stupnu
    dosadime rovnobezky v pripade, ze kreslime rovnobezky, poledniky kdyz kreslime poledniky
    """
    left(90)
    forward(seznam[index]  * 10 - seznam[index+1] * 10)
    right(90)

#zrychlime zelvu
speed(10)
#posune želvu nahoru
penup()
left(90)
forward(polednik_delka)
right(90)
pendown()


#kresli rovnobezky
for i in range(len(rovnobezky)-1):
    kresli(rovnobezka_delka)
    posun_o_10_stupnu(rovnobezky,i)
#nakresli posledni rovnobezku
kresli(rovnobezka_delka)
#vrati se zpatky do body 0,0=
left(90)
forward(polednik_delka)
#posune se úplně doprava:
right(90)
forward(rovnobezka_delka)
right(90)

#kresli poledníky:
if zobrazeni == "M":    #výjimka pro Mercatorovo zobrazení (póly leží v nekonečnu)
    for k in range(len(poledniky)-1):
        kresli(polednik_delka_mercator)
        posun_o_10_stupnu(poledniky,k)
    kresli(polednik_delka_mercator)
else:
    for k in range(len(poledniky)-1):
        kresli(polednik_delka)
        posun_o_10_stupnu(poledniky,k)
    kresli(polednik_delka)

exitonclick()

#####################konec zelvy

print()
print()

zadana_sirka = float(input("Zadejte zeměpisnou šířku: "))
zadana_delka = float(input("Zadejte zeměpisnou délku: "))
#ptani se na zemepisne souradnice
while zadana_sirka and zadana_delka != 0:
    print("Souřadnice zeměpisné šířky:", spocti_sirku(zobrazeni, zadana_sirka, meritko, R))
    print("Souřadnice zeměpisné délky:", spocti_delku(R, zadana_delka, meritko))
    zadana_sirka = float(input("Zadejte zeměpisnou šířku: "))
    zadana_delka = float(input("Zadejte zeměpisnou délku: "))
    #muzu pouzit funkce, ktere jsem si vytvorila na zacatku pro vypocet souradnic rovnobezek a poledniku po 10°

print("Konec")