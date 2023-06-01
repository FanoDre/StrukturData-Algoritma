import os

os.system('cls')

# ------------------------------------------------------------
print(60*'-')
print(f"NAMA \t: ALFANOEL AUDREY")
print(f"NIM \t: 411221162")
print(60*'-')
# ------------------------------------------------------------

data = [9, 22, 8, 20, 7]

dataSortedfrmLow = sorted(data)
dataSortedfrmHigh = sorted(data, reverse=True)

print("Terkecil > Terbesar")
print(f"\t{dataSortedfrmLow}")
print()
print("Terbesar > Terkecil ")
print(f"\t{dataSortedfrmHigh}")
print(60*'-')
