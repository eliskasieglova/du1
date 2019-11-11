import math             #na používání radiánů,ln,sin,cos,tan
from turtle import forward,backward,right,left,exitonclick,speed,penup,pendown

#otázka na zobrazení
zobrazeni = input("Vyber zobrazení (A=Marinovo, B=Braunovo, M=Mercatorovo, L=Lambertovo): ")
while zobrazeni != "L" and zobrazeni != "A" and zobrazeni != "B" and zobrazeni != "M":
    zobrazeni = input("Zadali jste neplatné zobrazení. Zkuste to znovu: ")
#dotaz na měřítko
meritko = int(input("Zadej měřítko: "))
#dotaz na poloměr Země:
R=(float(input("Zadejte poloměr Země: ")))*100000
if R == 0 or not R:
    R=6371.11

#vytvoření seznamů
poledniky = [ ]
rovnobezky = [ ]

if zobrazeni == "A":                        # Marinovo:  x=R*v   y=R*u
    for stupen_delka in range(-90, 91, 10):
        rovnobezky_body = ((R * math.radians(stupen_delka)) / meritko)
        rovnobezky.append(round(rovnobezky_body, 1))
    for stupen_sirka in range(-180, 181, 10):
        poledniky_body = ((R * math.radians(stupen_sirka)) / meritko)
        poledniky.append(round(poledniky_body, 1))
    zadane_zobrazeni = "Marinovo zobrazení"
elif zobrazeni == "M":                      # Mercatorovo:  x=R*v   y=R*ln(cotg(fi/2))
    for stupen_delka in range(80, 9, -10):
        rovnobezky_body = (R * math.log((1 / ((math.tan((math.radians(stupen_delka)) / 2))))) / meritko) #nefunguje
        rovnobezky.append(round(rovnobezky_body, 1))
    #přidám 0 na první (nulté) místo v seznamu
    rovnobezky.insert(0, 0)
    #projedu seznam rovnobezky[], přidávám záporné hodnoty na první (nulté) místo v seznamu
    for x in list(rovnobezky):
        if x != 0:
            rovnobezky.insert(0,-x)
    for stupen_sirka in range(-180, 181, 10):
        poledniky_body = ((R * math.radians(stupen_sirka)) / meritko)
        poledniky.append(round(poledniky_body, 1))
    zadane_zobrazeni = "Mercatorovo zobrazení"
elif zobrazeni == "B":                      # Braunovo:     x=R*v   y=2*R*tg(u/2)
    # meritko = int(input("Zadej měřítko: "))
    for stupen_delka in range(-90, 91, 10):
        rovnobezky_body = ((2 * R * math.tan((math.radians(stupen_delka)) / 2)) / meritko)
        rovnobezky.append(round(rovnobezky_body, 1))
    for stupen_sirka in range(-180, 181, 10):
        poledniky_body = ((R * math.radians(stupen_sirka)) / meritko)
        poledniky.append(round(poledniky_body, 1))
    zadane_zobrazeni = "Braunovo zobrazení"
elif zobrazeni == "L":                      # Lambertovo:   x=R*v   y=R*sin(u)
    # meritko = int(input("Zadej měřítko: "))
    for stupen_delka in range(-90, 91, 10):
        rovnobezky_body = (R * math.sin(math.radians(stupen_delka)) / meritko)
        rovnobezky.append(round(rovnobezky_body, 1))
    for stupen_sirka in range(-180, 181, 10):
        poledniky_body = ((R * math.radians(stupen_sirka)) / meritko)
        poledniky.append(round(poledniky_body, 1))
    zadane_zobrazeni = "Lambertovo zobrazení"

print(zadane_zobrazeni)
print("1 :",meritko)
print("Rovnoběžky:",end=" ")
for i in rovnobezky:
    if i  < -100 or i > 100:
        print("-", end=", ")
    else:
        print(i, end=", ")
print()
print("Poledníky:", end=" ")
for i in poledniky:
    if i  < -100 or i > 100:
        print("-", end=", ")
    else:
        print(i, end=", ")


#užitečné zkratky pro kreslení mřížky:
rovnobezka_delka = poledniky[-1] * 10 #délka půlky rovnoběžky (*10 na cm)
polednik_delka = rovnobezky[-1] * 10 #délka půlky poledníku

#zrychlime zelvu
speed(10)

#posune želvu dolů
penup()
right(90)
forward(polednik_delka)
left(90)
pendown()

#kresli rovnobezky
for i in range(len(rovnobezky)-1):
    forward(rovnobezka_delka)
    backward(2*rovnobezka_delka)
    forward(rovnobezka_delka)
    left(90)
    forward(rovnobezky[i+1]*10-rovnobezky[i]*10)
    right(90)
forward(rovnobezka_delka)
backward(2 * rovnobezka_delka)
forward(rovnobezka_delka)
#vrati se zpatky do body 0,0
right(90)
forward(polednik_delka)
#posune se úplně doleva:
right(90)
forward(rovnobezka_delka)
right(90)
#kresli poledníky:
if zobrazeni == "M":    #výjimka pro Mercatorovo zobrazení (póly leží v nekonečnu)
    for k in range(len(poledniky)):
        forward(polednik_delka+30)
        backward(2 * polednik_delka+60)
        forward(polednik_delka+30)
        left(90)
        forward(poledniky[k] * 10 - poledniky[k-1] * 10)
        right(90)
else:
    for k in range(len(poledniky)):
        forward(polednik_delka)
        backward(2 * polednik_delka)
        forward(polednik_delka)
        left(90)
        forward(poledniky[k] * 10 - poledniky[k-1] * 10)
        right(90)
exitonclick()

#ptani se na zemepisne souradnice
x = float(input("Zadejte zeměpisnou šířku: "))
y = float(input("Zadejte zeměpisnou délku: "))

#prevod zemepisne sirky
d1 = int(x)
m1 = (x - int(x))*60
s1 = (m1 - int(m1))*60
m1 = int(m1)

print("Zeměpisná šířka:",end=' ')
print(d1,"stupnů",m1,"minut a ",s1,"vteřin")

#prevod zemepisne delky
d2 = int(y)
m2 = (y - int(y))*60
s2 = (m2 - int(m2))*60
m2 = int(m2)

print("Zeměpisná délka:",end=' ')
print(d2,"stupnů",m2,"minut a ",s2,"vteřin")