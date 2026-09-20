import os
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
    os.system("cls" if os.name == "nt" else "clear")
    
    print("-" * 60)    
    print("Népesség 2025".center(60))
    print()
    print("[1] Megye adatai")
    print("[2] Település típusai")
    print("[x] Kilépés")
    print()
    print("-" * 60)
    print()

    mainmenu_valasztas = input("> ")
    return mainmenu_valasztas

#1. valaszas
def megyeadatok_ui(telepulesek):
    os.system("cls" if os.name == "nt" else "clear")


    bekeres_megyekód = input("Kérem a megye kódját: ")
    print()

    bekert_megyekod_letezik = False

    for i in telepulesek:
        if i["megyekod"] == bekeres_megyekód:
            bekert_megyekod_letezik = True
            break
    print("-"*60)

    if bekert_megyekod_letezik:
        megye_telepules_adatok = megyetelepulesek(telepulesek,bekeres_megyekód)
        print(f"Települések száma: {megye_telepules_adatok[0]} db")
        print(f"Összes lakos: {megye_telepules_adatok[1]} fő")
        print(f"Városok lakosai összesen: {megye_telepules_adatok[2]} fő")
    else:
        print("Hiba, nincs ilyen megye!".center(60))
        
    print("-"*60)
    print()
    print("[Enter] Vissza a menübe ")
    input("> ")
    

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
    os.system("cls" if os.name == "nt" else "clear")

    print("-"*60)
    print("Települések Típusai")
    print()
    print("[a] Község")
    print("[b] Város")
    print()
    print("-"*60)
    print()
    print("[x] Vissza")
    tipus_bekeres = input("> ")

    if tipus_bekeres == "x":
        return
    elif tipus_bekeres == "a" or tipus_bekeres == "b":
        telepules_tipus_listazasa(telepulesek,tipus_bekeres)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("-" * 60)
        print("Hiba, nincs ilyen típus".center(60))
        print("-" * 60)
        print()
        print("[Enter] Vissza a menübe ")
        input("> ")
        return


def telepules_tipus_listazasa(telepulesek, tipus_bekeres):
    kivalasztott_telepulesek = telepules_kivalasztas(telepulesek, tipus_bekeres)
    osszes_oldal = (len(kivalasztott_telepulesek) + 20 -1) // 20
    aktualis_oldal = 0


    while True:
        os.system("cls" if os.name == "nt" else "clear")

        oldal_elemek_start = (aktualis_oldal * 20)
        oldal_elemek_end = min(oldal_elemek_start + 20, len(kivalasztott_telepulesek))
        oldal_elemek = kivalasztott_telepulesek[oldal_elemek_start:oldal_elemek_end]

        print("-" * 60)

        print(f"{"Település neve":<30}{"Népesség":>30}")
        print()

        for telepules in oldal_elemek:
            print(f"{telepules["nev"]:<50}{(telepules["ferfi_szam"]+telepules["no_szam"]):>10}")

        print("-" * 60)

        if aktualis_oldal == osszes_oldal -1:
            print(f"[a] <--- {aktualis_oldal+1}/{osszes_oldal}")
        elif aktualis_oldal == 0:
            print(f"{aktualis_oldal+1}/{osszes_oldal} ---> [d]")
        else:
            print(f"[a] <--- {aktualis_oldal+1}/{osszes_oldal} ---> [d]")
        print("[x] Kilépés")

        lista_iranyitas_bekeres = input("> ")

        print()
        if lista_iranyitas_bekeres == "d":
            if aktualis_oldal < osszes_oldal -1:
                aktualis_oldal += 1
            else:
                print("Ez az utolsó oldal!")
                input("[Enter] továbblépés ")
        elif lista_iranyitas_bekeres == "a":
            if aktualis_oldal > 0:
                aktualis_oldal -=1
            else:
                print("Ez az első oldal!")
                input("[Enter] továbblépés ")
        elif lista_iranyitas_bekeres == "x":
            break
        else:
            print("Érvénytelen bevitel!")
            input("[Enter] továbblépés ")


def telepules_kivalasztas(telepulesek, valasztas):
    kivalasztott_telepulesek = []
    if valasztas == "a":
        for i in telepulesek:
            if i["telepules_tipus"] == "község" or i["telepules_tipus"] == "nagyközség":
                kivalasztott_telepulesek.append(i)
    elif valasztas == "b":
        for i in telepulesek:
            if i["telepules_tipus"] == "város" or i["telepules_tipus"] == "fővárosi kerület" or i["telepules_tipus"] == "vármegye székhely" or i["telepules_tipus"] == "vármegyei jogú város":
                kivalasztott_telepulesek.append(i)
    return kivalasztott_telepulesek


def main():
    while True:
        menu_valasztas = menu_ui()
        if menu_valasztas == "1":
            megyeadatok_ui(telepulesek)
        elif menu_valasztas == "2":
            telepules_tipusok_ui(telepulesek)
        elif menu_valasztas == "x":
            print("Kilépés...")
            print()
            break
main()


