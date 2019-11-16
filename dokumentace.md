### Dokumentace

Prvně se program dotáže uživatele  na zobrazení. Dokud uživatel nezadá jedno z písmen A, B, M nebo L, ptá se program znovu.

Dále se program uživatele ptá na měřítko a poloměr Země, dokud nezadá kladné číslo. Pokud uživatel do poloměru Země zadá 0, počítá program s číslem 6371.11.

Další část programu počítá souřadnice podle zobrazení, které si uživatel dříve zvolil a sice podle těchto vzorců:
Pro všechny souřadnice poledníků platí stejný vzorec: *x=R\*v*
Pro souřadnice rovnoběžek máme 4 různé vzorce:
Marinovo zobrazení: *y=R\*u*
Mercatorovo zobrazení: *y=R\*ln(cotg(u/2))*
Braunovo zobrazení: *y=2\*R\*tg(u/2)*
Lambertovo zobrazení: *y=R\*sin(u)*
Souřadnice počítám pomocí cyklu po 10°. Uložím je do seznamů rovnobezky[] a poledniky[].
Mercatorovo zobrazení  (není možné počítat se zápornými hodnotami nebo dělit nulou) - proto vytvořím seznam pouze pro pozizivní hodnoty (range(80,9,-10)) a poté pomocí for-cyklu přidám záporné hodnoty.

Další část programu je vykreslování mřížky k zadanému zobrazení.

Mercatorovo zobrazení musí být ošetřeno individuálně, protože póly na něm leží v nekonečnu.

Po vykreslení mřížky se program uživatele zeptá na zeměpisné souřadnice. Výsledkem jsou souřadnice přepočítané do daného zobrazení.
