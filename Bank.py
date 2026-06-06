import os
import time
from colorama import Fore, Style, init
init()
def clear():
    os.system('cls' if os.name == "nt" else 'clear')

# Database 
data_user = {
    "username1": "admin",
    "password1": "admin123",
    "pin1": 102007,
    "usersaldo1": 1500000,
    "norek1": 1118212855121
}
loopmenu = True
loop = True
while loop:
    print("╔══════════════════════════════════════╗")
    print("║        🏦 BANK DIGITAL CLI  🏦       ║")
    print("║     Sistem Perbankan Versi CLI       ║")
    print("╚══════════════════════════════════════╝")
    print("Selamat Datang, Nasabah!")
    print("[1] 👤 Login")
    print("[2] 🚪 Keluar")
    print()
    inputfirst = input("➜  Masukan Pilihan : ")
    clear()
    while loop:
        if inputfirst == "1":
            print("╔══════════════════════════════════════════════╗")
            print("║                 🔐 LOGIN 🔐                  ║")
            print("╚══════════════════════════════════════════════╝")
            print("Selamat Datang di BANK DIGITAL CLI")
            print("Silakan masuk ke akun Anda")
            inputlogin_username = input("👤 Username : ")
            inputlogin_password = input("🔑 Password : ")
            if inputlogin_username == data_user["username1"] and inputlogin_password == data_user["password1"]:
                while loopmenu:
                    time.sleep(3)
                    print(Fore.GREEN + "! Login Berhasil" + Style.RESET_ALL)
                    clear()
                    print("╔══════════════════════════════════════════════╗")
                    print("║            🏦 BANK DIGITAL CLI 🏦            ║")
                    print("╚══════════════════════════════════════════════╝")
                    print()
                    print("👋 Selamat Datang, " + Fore.GREEN + "AZHAR RAAFI PRADHITA!" + Style.RESET_ALL)
                    print("💙 Terima kasih telah menggunakan layanan kami.")
                    print("💰 Kelola keuangan dengan aman dan mudah.")
                    print()
                    print("╔═══════════════ MENU UTAMA ═══════════════════╗")
                    print("║                                              ║")
                    print("║  💳 [1] Cek Saldo                            ║")
                    print("║  💸 [2] Transfer Dana                        ║")
                    print("║  ➕ [3] Top Up Saldo                         ║")
                    print("║  📜 [4] Riwayat Transaksi                    ║")
                    print("║  🔐 [5] Ganti PIN                            ║")
                    print("║  🚪 [6] Logout                               ║")
                    print("║                                              ║")
                    print("╚══════════════════════════════════════════════╝")
                    print("")
                    pilihan = input("➜  Pilih menu : ")
                    inputmenu_utama = input("> Masukan Pilihan : ")
            elif inputlogin_username != data_user["username1"] and inputlogin_password == data_user["password1"]:
                print(Fore.RED + "! Username Salah" + Style.RESET_ALL)
            elif inputlogin_username == data_user["username1"] and inputlogin_password != data_user["password1"]:
                print(Fore.RED + "! Password Salah" + Style.RESET_ALL)
        elif inputfirst == "2":
            break
        else:
            print(Fore.RED + "! Masukan pilihan dengan valid" + Style.RESET_ALL)
            break