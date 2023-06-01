import os

os.system('cls')

# ------------------------------------------------------------
print(60*'-')
print(f"NAMA \t: ALFANOEL AUDREY")
print(f"NIM \t: 411221162")
print(60*'-')
# ------------------------------------------------------------


def perkalian():
    print(60*'-')
    print(f"{'APLIKASI HITUNG PERKALIAN':>44}")
    print(60*'-')
    angka1 = int(input("Kalikan dengan angka?: "))
    angka2 = int(input("Mulai dari? : "))
    angka3 = int(input("Sampai dengan? : "))
    print(60*'-')

    for x in range(angka2, angka3 + 1):
        print(f"\t{x} x {angka1} = {x*angka1}")

    print(60*'-')


def pembagian():
    print(60*'-')
    print(f"{'APLIKASI HITUNG PEMBAGIAN':>44}")
    print(60*'-')
    angka1 = int(input("Bagi dengan angka?: "))
    angka2 = int(input("Mulai dari? : "))
    angka3 = int(input("Sampai dengan? : "))
    print(60*'-')

    for x in range(angka2, angka3 + 1):
        print(f"\t{x} x {angka1} = {x/angka1}")

    print(60*'-')


def pertambahan():
    print(60*'-')
    print(f"{'APLIKASI HITUNG PERTAMBAHAN':>44}")
    print(60*'-')
    angka1 = int(input("Tambah dengan angka?: "))
    angka2 = int(input("Mulai dari? : "))
    angka3 = int(input("Sampai dengan? : "))
    print(60*'-')

    for x in range(angka2, angka3 + 1):
        print(f"\t{x} x {angka1} = {x+angka1}")

    print(60*'-')


def pengurangan():
    print(60*'-')
    print(f"{'APLIKASI HITUNG PENGURANGAN':>44}")
    print(60*'-')
    angka1 = int(input("Tambah dengan angka?: "))
    angka2 = int(input("Mulai dari? : "))
    angka3 = int(input("Sampai dengan? : "))
    print(60*'-')

    for x in range(angka2, angka3 + 1):
        print(f"\t{x} x {angka1} = {x-angka1}")

    print(60*'-')


def selectOp():
    inp = input("Pilih Operator? [ + | - | x | / ]: ")
    if inp == "+":
        pertambahan()
        selectOp()
    elif inp == "-":
        pengurangan()
        selectOp()
    elif inp == "x":
        perkalian()
        selectOp()
    elif inp == "/":
        pembagian()
        selectOp()
    else:
        print("Operator tidak ditemukan.")
        print()


selectOp()
