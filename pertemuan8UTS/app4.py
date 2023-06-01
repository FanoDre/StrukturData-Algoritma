import os

os.system('cls')

# ------------------------------------------------------------
print(60*'-')
print(f"NAMA \t: ALFANOEL AUDREY")
print(f"NIM \t: 411221162")
print(60*'-')
# ------------------------------------------------------------


def pangkat():
    print(60*'-')
    print(f"{'APLIKASI HITUNG PERKALIAN':>44}")
    print(60*'-')
    angka1 = int(input("Mulai dari angka\t: "))
    angka2 = int(input("Sampai angka\t\t: "))
    angka3 = int(input("Nilai pangkat\t\t: "))
    print(60*'-')

    for x in range(angka1, angka2 + 1):
        print(f"\t({x} ^{angka3} = {x**angka3})")
    print(60*'-')


pangkat()
