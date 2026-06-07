import os
import time
from colorama import Fore, Style, init
init (autoreset=True)
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

data_nomer_ewallet = {
    "6282128553267": "AZHAR RAAFI PRADHITA",
    "6285749776203": "IRA AULIA",
}

data_no_rekening = {
     "111212855121": "AZHAR RAAFI PRADHITA",
     "111549776121": "IRA AULIA",
}


loopmenu = True
looplogin = True
looplogin2 = True


def menu_antarrekening():
    clear()
    loopwallet = True
    while loopwallet:
        print("╔══════════════════════════════════════════════╗")
        print("║         💸 TRANSFER ANTAR REKENING          ║")
        print("╚══════════════════════════════════════════════╝")
        print()
        print("> Masukkan data rekening tujuan")
        print()
        rekening_tujuan = input("💳 Nomor Rekening : ")
        if rekening_tujuan in data_no_rekening:
            nama_tujuan = data_no_rekening[rekening_tujuan]
            time.sleep(1)
            print()
            print(Fore.GREEN +"> NOMER DITEMUKAN")
            print("💡 Ketentuan Tranfer Minimal Rp 50.000")
            nominal_dana = int(input("➜ Masukan Nominal Transfer :"))                                                 
            if nominal_dana >= 50000:
                time.sleep(1)
                clear()
                print("╔══════════════════════════════════════════════╗")
                print("║             📋 KONFIRMASI TOP UP             ║")
                print("╚══════════════════════════════════════════════╝")
                print()
                print(f"👤 Nama Tujuan   : {nama_tujuan}")
                print(f"📱 Nomor Tujuan  : {rekening_tujuan}")
                print(f"💰 Nominal Top Up: Rp {nominal_dana:,}")
                print()
                print("══════════════════════════════════════════════")
                print("! Pastikan data tujuan sudah benar.")
                print("! Transaksi yang berhasil tidak dapat dibatalkan.")
                print("══════════════════════════════════════════════")
                print()
                print("[1] ✅ Konfirmasi")
                print("[2] ❌ Batal")
                print()
                konfirmasi = input("➜ Masukan Pilihan : ")
                if konfirmasi == "1":
                    time.sleep(3)
                    clear()
                    data_user["usersaldo1"] -= nominal_dana
                    print("")
                    print("==========================================")
                    print("TRANSAKSI BERHASIL".center(40))
                    print("==========================================")
                    print("")
                    print(f"Kirim Ke    : {nama_tujuan}")
                    print(f"No. Tujuan  : {rekening_tujuan}")
                    print(f"Nominal     : Rp{nominal_dana:,}")
                    print("")
                    print("------------------------------------------")
                    print(f"Sisa Saldo Anda: Rp {data_user['usersaldo1']:,}".center(40))
                    print("==========================================")
                    print("> Ketik apapun Untuk Kembali ke Menu Utama")
                    print("")
                    exit = input("➜  Masukan Pilihan : " )
                    if not exit:
                         return

                else:
                    clear() 
                    print(Fore.RED + "! Transaksi dibatalkan")
                    time.sleep(1)
                    break
            else:
                clear()
                print(Fore.RED + "! Masukan nominal dengan valid")
                time.sleep(1)
        else:
            clear()
            print(Fore.RED + "! Nomer tidak ditemukan")
            time.sleep(1)         
             
while looplogin:
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
    if inputfirst == "1":
        while looplogin2:
            print("╔══════════════════════════════════════════════╗")
            print("║                 🔐 LOGIN 🔐                  ║")
            print("╚══════════════════════════════════════════════╝")
            print("Selamat Datang di BANK DIGITAL CLI")
            print("Silakan masuk ke akun Anda")
            inputlogin_username = input("👤 Username : ")
            inputlogin_password = input("🔑 Password : ")
            if inputlogin_username == data_user["username1"] and inputlogin_password == data_user["password1"]:
                    time.sleep(1)
                    print(Fore.GREEN + "! Login Berhasil")
                    time.sleep(1)
                    clear()
                    while loopmenu:
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
                        print("║  ➕ [2] Transfer & Top Up                    ║")
                        print("║  🚪 [3] Logout                               ║")
                        print("║                                              ║")
                        print("╚══════════════════════════════════════════════╝")
                        print("")
                        pilihan = input("➜  Pilih menu : ")
                        if pilihan == "1":
                            clear()
                            print("╔══════════════════════════════════════════════╗")
                            print("║               💳 CEK SALDO 💳                ║")
                            print("╚══════════════════════════════════════════════╝")
                            print()
                            print("👤 Nama Nasabah : Azhar")
                            print("💰 Saldo Saat Ini : "+ Style.BRIGHT + f"Rp{data_user['usersaldo1']:,}")
                            print()
                            input("➜  Ketik Enter untuk kembali" )
                        elif pilihan == "2":
                                clear()
                                looptrasnfer = True
                                while looptrasnfer:
                                    print("╔══════════════════════════════════════════════╗")
                                    print("║               💸 TRANSFER 💸                 ║")
                                    print("╚══════════════════════════════════════════════╝")
                                    print()
                                    print("> Pilih Metode Transfer")
                                    print(" [1] 🏦 Transfer Antar Rekening")
                                    print(" [2] 🌐 Transfer Antar Bank")
                                    print(" [3] 📱 Top Up E-Wallet")
                                    print(" [4] < Kembali")
                                    print()
                                    print("══════════════════════════════════════════════")
                                    print()
                                    pilihan_trasnfer = input("➜  Pilih menu : ")
                                    if pilihan_trasnfer == "3":
                                            clear()
                                            loopwallet = True
                                            while loopwallet:
                                                print("╔══════════════════════════════════════════════╗")
                                                print("║                ➕ TOP UP E-WALLET            ║")
                                                print("╚══════════════════════════════════════════════╝")
                                                print()
                                                print("> Pilih E-Wallet Tujuan Anda")
                                                print("[1] DANA")
                                                print("[2] GoPay")
                                                print("[3] < Kembali")
                                                print()
                                                print("══════════════════════════════════════════════")
                                                print()
                                                ewallet = input("➜ Pilih E-Wallet : ")
                                                if ewallet == "1":
                                                        clear()
                                                        print("╔══════════════════════════════════════════════╗")
                                                        print("║                   TOP UP DANA                ║")
                                                        print("╚══════════════════════════════════════════════╝")
                                                        print()
                                                        print("📱 Masukkan nomor DANA tujuan")
                                                        print("Pastikan nomor yang dimasukkan sudah benar.")
                                                        print()
                                                        print("══════════════════════════════════════════════")
                                                        nomer_dana = input("➜ Masukan Nomor : ")
                                                        if nomer_dana in data_nomer_ewallet:
                                                            nama_tujuan = data_nomer_ewallet[nomer_dana]
                                                            time.sleep(1)
                                                            print()
                                                            print(Fore.GREEN +"> NOMER DITEMUKAN")
                                                            print("💡 Ketentuan Top Up Minimal top up Rp 10.000")
                                                            nominal_dana = int(input("➜ Masukan Nominal Transfer :"))                                                 
                                                            if nominal_dana >= 10000:
                                                                    time.sleep(1)
                                                                    clear()
                                                                    print("╔══════════════════════════════════════════════╗")
                                                                    print("║             📋 KONFIRMASI TOP UP             ║")
                                                                    print("╚══════════════════════════════════════════════╝")
                                                                    print()
                                                                    print("   E-Wallet      : Dana")
                                                                    print(f"👤 Nama Tujuan   : {nama_tujuan}")
                                                                    print(f"📱 Nomor Tujuan  : {nomer_dana}")
                                                                    print(f"💰 Nominal Top Up: Rp {nominal_dana:,}")
                                                                    print()
                                                                    print("══════════════════════════════════════════════")
                                                                    print("! Pastikan data tujuan sudah benar.")
                                                                    print("! Transaksi yang berhasil tidak dapat dibatalkan.")
                                                                    print("══════════════════════════════════════════════")
                                                                    print()
                                                                    print("[1] ✅ Konfirmasi")
                                                                    print("[2] ❌ Batal")
                                                                    print()
                                                                    konfirmasi = input("➜ Masukan Pilihan : ")
                                                                    if konfirmasi == "1":
                                                                        time.sleep(3)
                                                                        clear()
                                                                        data_user["usersaldo1"] -= nominal_dana
                                                                        print("")
                                                                        print("==========================================")
                                                                        print("TRANSAKSI BERHASIL".center(40))
                                                                        print("==========================================")
                                                                        print("")
                                                                        print(f"Kirim Ke    : {nama_tujuan}")
                                                                        print(f"No. Tujuan  : {nomer_dana}")
                                                                        print(f"Nominal     : Rp{nominal_dana:,}")
                                                                        print("")
                                                                        print("------------------------------------------")
                                                                        print(f"Sisa Saldo Anda: Rp {data_user['usersaldo1']:,}".center(40))
                                                                        print("==========================================")
                                                                        print("> Ketik apapun Untuk Kembali ke Menu Utama")
                                                                        print("")
                                                                        input("➜  Masukan Pilihan : " )
                                                                    else:
                                                                        clear() 
                                                                        print(Fore.RED + "! Transaksi dibatalkan")
                                                                        time.sleep(1)
                                                                        break
                                                            else:
                                                                clear()
                                                                print(Fore.RED + "! Masukan nominal dengan valid")
                                                                time.sleep(1)
                                                        else:
                                                            clear()
                                                            print(Fore.RED + "! Nomer tidak ditemukan")
                                                            time.sleep(1)

                                                elif ewallet == "2":
                                                    clear()
                                                    print("╔══════════════════════════════════════════════╗")
                                                    print("║                   TOP UP GOPAY               ║")
                                                    print("╚══════════════════════════════════════════════╝")
                                                    print()
                                                    print("📱 Masukkan nomor DANA tujuan")
                                                    print("Pastikan nomor yang dimasukkan sudah benar.")
                                                    print()
                                                    print("══════════════════════════════════════════════")
                                                    nomer_dana = input("➜ Masukan Nomor : ")
                                                    if nomer_dana in data_nomer_ewallet:
                                                        nama_tujuan = data_nomer_ewallet[nomer_dana]
                                                        time.sleep(1)
                                                        print()
                                                        print(Fore.GREEN +"> NOMER DITEMUKAN")
                                                        print("💡 Ketentuan Top Up Minimal top up Rp 10.000")
                                                        nominal_dana = int(input("➜ Masukan Nominal Transfer :"))
                                                        if nominal_dana >= 10000:
                                                            time.sleep(1)
                                                            clear()
                                                            print("╔══════════════════════════════════════════════╗")
                                                            print("║             📋 KONFIRMASI TOP UP             ║")
                                                            print("╚══════════════════════════════════════════════╝")
                                                            print()
                                                            print("   E-Wallet      : GoPay")
                                                            print(f"👤 Nama Tujuan   : {nama_tujuan}")
                                                            print(f"📱 Nomor Tujuan  : {nomer_dana}")
                                                            print(f"💰 Nominal Top Up: Rp {nominal_dana:,}")
                                                            print()
                                                            print("══════════════════════════════════════════════")
                                                            print("! Pastikan data tujuan sudah benar.")
                                                            print("! Transaksi yang berhasil tidak dapat dibatalkan.")
                                                            print("══════════════════════════════════════════════")
                                                            print()
                                                            print("[1] ✅ Konfirmasi")
                                                            print("[2] ❌ Batal")
                                                            print()
                                                            konfirmasi = input("➜ Masukan Pilihan : ")
                                                            if konfirmasi == "1":
                                                                time.sleep(3)
                                                                clear()
                                                                data_user["usersaldo1"] -= nominal_dana
                                                                print("")
                                                                print("==========================================")
                                                                print("TRANSAKSI BERHASIL".center(40))
                                                                print("==========================================")
                                                                print("")
                                                                print(f"Kirim Ke    : {nama_tujuan}")
                                                                print(f"No. Tujuan  : {nomer_dana}")
                                                                print(f"Nominal     : Rp{nominal_dana:,}")
                                                                print("")
                                                                print("------------------------------------------")
                                                                print(f"Sisa Saldo Anda: Rp {data_user['usersaldo1']:,}".center(40))
                                                                print("==========================================")
                                                                print("> Ketik apapun Untuk Kembali ke Menu Utama")
                                                                print("")
                                                                input("➜  Masukan Pilihan : " )
                                                            else:
                                                                    clear() 
                                                                    print(Fore.RED + "! Transaksi dibatalkan")
                                                                    time.sleep(1)
                                                                    break             
                                                        else:
                                                                clear()
                                                                print(Fore.RED + "! Masukan nominal dengan valid")
                                                                time.sleep(1)
                                                    else:
                                                            clear()
                                                            print(Fore.RED + "! Nomer tidak ditemukan")
                                                            time.sleep(1)                        









                                                elif ewallet == "3":
                                                    clear()
                                                    break
                                                else:
                                                    clear()
                                                    print(Fore.RED + "! Masukan pilihan dengan valid")
                                                    time.sleep(1)


                                    if pilihan_trasnfer == "1":
                                            menu_antarrekening()                                                         

                                    elif pilihan_trasnfer == "2":
                                        print("╔══════════════════════════════════════════════╗")
                                        print("║            🌐 TRANSFER ANTAR BANK           ║")
                                        print("╚══════════════════════════════════════════════╝")
                                        print()
                                        print("Pilih Bank:")
                                        print()
                                        print("[1] BCA")
                                        print("[2] BRI")
                                        print("[3] MANDIRI")
                                        print()
                                        print("══════════════════════════════════════════════")
                                        print()
                                        bank = input("➜ Pilih Bank : ")

                                    elif pilihan_trasnfer == "4":
                                        clear()
                                        break
                                        
                                    else:
                                        clear()
                                        print(Fore.RED + "! Masukan pilihan dengan valid")
                                        time.sleep(1)

                        elif pilihan == "3":
                            time.sleep(2)
                            clear()
                            print(Fore.GREEN + "! Logout Berhasil")
                            break
                                        
                        else:
                            clear()
                            print(Fore.RED + "! Masukan pilihan dengan valid")
                            time.sleep(1)


                                
                                
                        
            elif inputlogin_username == "0" or inputlogin_password == "0":
                clear()
                break                   
            elif inputlogin_username != data_user["username1"] and inputlogin_password == data_user["password1"]:
                clear()
                print(Fore.RED + "! Username Salah" + Style.RESET_ALL)
            elif inputlogin_username == data_user["username1"] and inputlogin_password != data_user["password1"]:
                clear()
                print(Fore.RED + "! Password Salah")

            else:
                clear()
                print(Fore.RED + "! Login Gagal")
                
    elif inputfirst == "2":
        break
    else:
        print(Fore.RED + "! Masukan pilihan dengan valid")

