import os

os.system('cls')

# ------------------------------------------------------------
print(60*'-')
print(f"NAMA \t: ALFANOEL AUDREY")
print(f"NIM \t: 411221162")
print(60*'-')
# ------------------------------------------------------------

jurusanSI = ['Sistem Informasi',
             'Software Engineer']

jurusanTI = ['Teknik Informatika',
             'Network Engineer']


def selectJurusan():

    fakultas = ['SI',
                'TI']

    print("[+] Data Fakultas")
    for x in range(len(fakultas)):
        print(f"\t{x+1}. {fakultas[x]}")
    pilihFakultas = int(input("Pilih Fakultas: "))
    print(60*'-')

    print("[+] Data Jurusan")
    if pilihFakultas > 2:
        print("Data Tidak Ditemukan.")
        print(60*'-')

        selectJurusan()

    elif pilihFakultas == 1:
        for x in range(len(jurusanSI)):
            print(f"\t{x+1}. {jurusanSI[x]}")

        pilihJurusan = int(input("Pilih Jurusan: "))
        items = {'jurusan': jurusanSI[pilihJurusan - 1]}
        if pilihJurusan > 2:
            print("Data Tidak Ditemukan.")
            print(60*'-')
            selectJurusan()

        elif pilihJurusan == 1:
            priceJurusan = 5000000
            print(60*'-')
            print("[=] Data Jurusan ")
            print(f"\tJurusan : {items['jurusan']}")
            print(f"\tHarga   : Rp. {priceJurusan:,.2f}")
        elif pilihJurusan == 2:
            priceJurusan = 5100000
            print(60*'-')
            print("[=] Data Jurusan ")
            print(f"\tJurusan : {items['jurusan']}")
            print(f"\tHarga   : Rp. {priceJurusan:,.2f}")

    elif pilihFakultas == 2:
        for x in range(len(jurusanTI)):
            print(f"\t{x+1}. {jurusanTI[x]}")
        pilihJurusan = int(input("Pilih Jurusan: "))

        items = {'jurusan': jurusanTI[pilihJurusan - 1]}
        if pilihJurusan > 2:
            print("Data Tidak Ditemukan.")
            print(60*'-')
            selectJurusan()

        elif pilihJurusan == 1:
            priceJurusan = 5200000
            print(60*'-')
            print("[=] Data Jurusan ")
            print(f"\tJurusan : {items['jurusan']}")
            print(f"\tHarga   : Rp. {priceJurusan:,.2f}")
        elif pilihJurusan == 2:
            priceJurusan = 5300000
            print(60*'-')
            print("[=] Data Jurusan ")
            print(f"\tJurusan : {items['jurusan']}")
            print(f"\tHarga   : Rp. {priceJurusan:,.2f}")

    print(60*'-')


selectJurusan()
