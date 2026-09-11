telepulesek = []

with open('lakossag_2025.csv', "r" ,encoding='UTF-8') as fajl:
    fajl.readline()
    for sor in fajl:
        adat = sor.split(';')
        telepules = {
            "megyekod":adat[0],
            "nev":adat[1],
            "telepules_tipus":adat[2],
            "ferfi_szam":int(adat[3].replace(" ","")),
            "no_szam":int(adat[4].replace(" ","")),
        }
        telepulesek.append(telepules)

def menu_ui():
    print("--------------------------------------------------------------")    
    print()
    print("Népesség 2025".center(60))
    print("[1] Megye adatai")
    print("[2] Település típusai")
    print("[x] Kilépés")
    print()
    print("--------------------------------------------------------------")    
    print()
    mainmenu_valasztas = input("Válassz a továbblépéshez: ")
    return mainmenu_valasztas

#1. valaszas
def megyeadatok_ui(telepulesek):
    bekeres_megyekód = input("Kérem a megye kódját: ")

    megye_telepules_adatok = megyetelepulesek(telepulesek,bekeres_megyekód)
    print()
    print(f"Települések száma: {megye_telepules_adatok[0]} db")
    print(f"Összes lakos: {megye_telepules_adatok[1]} fő")
    print(f"Városok lakosai összesen: {megye_telepules_adatok[2]} fő")
    print()
    print("[Enter] Vissza")
    print()
    input()

    

def megyetelepulesek(telepulesek, bekeres_megyekod):
    telepulesszamok = 0
    osszlakos = 0
    varoslakos = 0
    for i in telepulesek:
        if i["megyekod"] == bekeres_megyekod:
            telepulesszamok += 1
            osszlakos += i["ferfi_szam"] + i["no_szam"]
            if i["telepules_tipus"] == "város" or i["telepules_tipus"] == "fővárosi kerület" or i["telepules_tipus"] == "vármegye székhely" or i["telepules_tipus"] == "vármegyei jogú város":
                varoslakos += i["ferfi_szam"] + i["no_szam"]
    return [telepulesszamok, osszlakos,varoslakos]

#2. valasztas
def telepules_tipusok_ui(telepulesek):
    print("Települések Típusai")
    print()
    print("[a] Község")
    print("[b] Város")
    print()
    print("[x] Vissza")
    valasztas = input("")
    if valasztas == "a":
        print("kozseg")
    elif valasztas == "b":
        print("varos")

def telepules_tipus_listazas(telepulesek, valasztas):
    kivalasztott_telepulesek = []
    sor_szamlalo = 0
    pass


def main():
    #menu_ui()
    #megyeadatok_ui(telepulesek)
    telepules_tipusok_ui(telepulesek)

main()


