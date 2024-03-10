seznam_cisel = [1, 2, 3]

# for cislo in seznam_cisel:
#     print(cislo)

# EAFP - Easier to Ask Forgiveness than Permission
#
# delka_listu = len(seznam_cisel)
# index_pristupu = 2
# if index_pristupu < delka_listu:
#     print(seznam_cisel[index_pristupu])
# else:
#     print("Pristupovany kod neexistuje v seznamu!")


prehled_zamestnancu = {
    'Petr Novak': {
        'vek': 35,
        'pozice': "udrzbar",
        'trvale bydliste': "Brno"
    },
    'Lucie Pokorna': {
        'vek': 25,
        'pozice': "pravnik",
        'trvale bydliste': "Breclav"
    },
}

hledany_index = 1
hledany_zamestnanec = "Petr Dvorak"
try:
    print(seznam_cisel[hledany_index])
    print(prehled_zamestnancu[hledany_zamestnanec])
except KeyError:
    print("Hledany zamestnanec neexistuje v databazi.")
except IndexError:
    print("Pristupovany index neexistuje v nasem seznamu!")

if hledany_index < len(seznam_cisel):
    print(seznam_cisel[hledany_index])
else:
    print("Pristupovany index neexistuje v nasem seznamu!")
if hledany_zamestnanec in prehled_zamestnancu:
    print(prehled_zamestnancu[hledany_zamestnanec])
else:
    print("Hledany zamestnanec neexistuje v databazi.")


print("Ukazka toho, ze program pokracuje dale!")