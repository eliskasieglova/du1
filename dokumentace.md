### Dokumentace

Importovala jsem math (potřebovala jsem funkce sin,cos,tan,log,radian) pro výpočet bodů na rovnoběžkách a polednících pomocí funkcí pro jednotlivá zobrazení.

Z balíčku turtle jsem importovala funkce forward,backward,right,left a exitonclick (pro základní ovládání želvy), funkci speed (abych jí mohla zrychlit, protože želva byla docela pomalá) a funkce penup a pendown (abych želvu mohla přesouvat, aniž by u toho kreslila).

Prvně jsem se uživatele dotázala na zobrazení. Případ, že by uživatel zadal nekorektní vstup jsem ošetřila while cyklem - program se bude uživatele ptát tak dlouho, dokud nezadá písmeno A, B, M nebo L.

Dále se program uživatele ptá na měřítko (a doufá, že uživatel zadá číslo) a na poloměr Země (pokud uživatel zadá číslo, počítá s ním, pokud uživatel zadá 0, počítá to s poloměrem 6371.11 km).

Další část programu počítá souřadnice podle zobrazení, které si uživatel dříve zvolil a sice podle těchto vzorců:
Pro všechny souřadnice poledníků platí stejný vzorec: *x=R\*v*
Pro souřadnice rovnoběžek máme 4 různé vzorce:
Marinovo zobrazení: *y=R\*u*
Mercatorovo zobrazení: *y=R\*ln(cotg(u/2))*
Braunovo zobrazení: *y=2\*R\*tg(u/2)*
Lambertovo zobrazení: *y=R\*sin(u)*
Souřadnice počítám pomocí for-cyklu po 10°. Uložím je do seznamů rovnobezky[] a poledniky[].
Mercatorovo zobrazení trochu zlobí kvůli přirozenému logaritmu ve vzorečku (není možné počítat se zápornými hodnotami nebo dělit nulou) - proto vytvořím seznam pouze pro pozizivní hodnoty (range(80,9,-10)) a poté pomocí for-cyklu přidám záporné hodnoty.

Zadané parametry (zobrazení, měřítko) zobrazím pomocí funkce print. Souřadnice rovnoběžek a poledníků ještě upravím pomocí for-cyklu, který říká, že všechny hodnoty větší než 100 nebo menší než -100 (výsledky vychází v cm - podle toho, kde je pak želva na papíře bude kreslit) mají být nahrazeny "-". Poté tyto výsledky také zobrazím pomocí funkce print.

Jako další bod jsem řešila, aby želva pomocí seznamů rovnobezky[] a poledniky[] vykreslila mřížky k zadanému zobrazení. Proto jsem si vytvořila proměnné rovnobezka_delka a polednik_delka. Proměnná rovnobezka_delka je rovna poslední hodnotě v seznamu poledniky[] (největší hodnota - potud má být vykreslena rovnoběžka) a vynásobena 10 (1 mm = 1px) a rovná se tedy polovině délky rovnoběžky. Proměnná polednik_delka vypadá obdobně.

Pak želvu zrychlím, ušetří mi to čas při zkouškách, jestli můj program funguje, a přesunu pomocí funkcí penup() a pendown() na stránku dolů (aby mi pak neodjížděla mimo obrazovku).

Pak postupně vykresluju rovnoběžky a poledníky. Mercatorovo zobrazení musí být ošetřeno individuálně, protože póly na něm leží v nekonečnu.

Poté se uživatele zeptám na zeměpisné souřadnice, udělám z nich čísla (float) a převedu je na stupně, minuty a vteřiny.
