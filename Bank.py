# Database 
data_user = {
    "username1": "admin",
    "password1": "admin123",
    "pin1": 102007,
    "usersaldo1": 1500000,
    "norek1": 1118212855121
}

loop = True
while loop:
    print("╔══════════════════════════════════════╗")
    print("║        🏦 BANK DIGITAL CLI  🏦       ║")
    print("║     Sistem Perbankan Versi CLI       ║")
    print("╚══════════════════════════════════════╝")
    print()
    print("Selamat Datang, Nasabah!")
    print("[1] Login")
    print("[2] Exit")
    print()
    inputfirst = input("> Masukan Pilihan : ")
    if inputfirst == "1":
        print("")
    elif inputfirst == "2":
        break