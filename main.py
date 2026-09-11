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

def mainmenu():
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

mainmenu()

def megyeadatok(telepulesek):
    bekeres_megyekód = input("Kérem a megye kódját: ")
    print

def megyetelepulesek(telepulesek, bekeres_megyekod):
    
    for i in telepulesek:
        if i["megyekod"] = bekeres_megyekod:
            

