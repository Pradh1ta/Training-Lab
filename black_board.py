# import time
# from colorama import Fore, Style, init
# init(autoreset=True)


# # main_menu_pilihan = ["[1] Sign Up", "[2] Sign In", "[3] Exit"]
# # data_user = {
# #     "username": "admin",
# #     "password": "admin123"
# # }


# def main_menu():
#     loop = True
#     while loop:
#         for menu in main_menu_pilihan:
#             print(menu)
        
#         input_menu = input("Masukan Pilihan : ")
#         match input_menu: 
#             case "1":
#                 print("-> Menjalankan fitur Sign Up...")
#                 menu_signup()
#             case "2":
#                 print("-> Menjalankan fitur Sign In...")
#                 break
#             case "3":
#                 print("-> Menjalankan fitur Exit...")
#                 break
#             case _:
#                 print( Fore.RED + "-> Pilih dengan benar...")
#                 break

# def menu_signup():
#     print("\n--- REGISTRASI AKUN ---")
#     inputusn = input("Masukan Username : ")
#     inputpw = input("Masukan Password : ")
#     if inputusn == data_user["username"] and inputpw == data_user["password"]:
#         login()
#     else:
#         return

# def login():
#     while True:
#         print("Anda Berhasil Login")


#========================================================================================================

# main_menu()



# def quiz():
#     inputan = int(input("Apa coba : "))
#     pilihan = inputan
#     match inputan:
#         case 1 | 2 | 3:
#             print("Jawaban kamu benar!")
#         case _:
#             print("Jawaban kamu salah.")

# quiz()

# cukimak = "10"
# print(cukimak, type(cukimak))

# cukimak_int = int(cukimak)
# print(cukimak_int, type(cukimak_int))

# cukimak_float = float(cukimak)
# print(cukimak_float)

# cukimak_bool = bool(cukimak)
# print(cukimak_bool)

#========================================================================================================

# a = 10
# b = 40

# hasil = a + b 
# print(hasil)

# hasil = a - b 
# print(hasil)

# hasil = a / b 
# print(hasil)

# hasil = a * b 
# print(hasil)

# hasil = a ** b 
# print(hasil)

# hasil = a % b 
# print(hasil)

# hasil = a // b 
# print(hasil)

# inputuser = int(input(": "))
# hasil = (inputuser > 0)
# hasil2 = (inputuser < 5)
# hasil3 = (inputuser > 8 )
# hasil4 = (inputuser < 11)

# hasil_akhir = (hasil and hasil2) or (hasil3 and  hasil4)
# print(hasil_akhir)

# inputuser = int(input(": "))

# hasil_akhir = inputuser > 0 and inputuser < 5 or inputuser > 8 and inputuser < 11
# print(hasil_akhir)


# a = 1
# b = a + 1

# print(b)

#========================================================================================================

# while True:
#     inputuser = int(input("Masukan nominal lebih dari Rp 10.000 dan kurang dari Rp 25.000 : "))
#     hasil = inputuser > 10000 and inputuser < 25000
#     if hasil == False:
#         print("Nominal Tidak Sesuai")
#     else:
#         print("Nominal Sesuai")

# data = ["1. Pertambahan", "2. Perkalian", "3. Pengurangan"]

# def pertambahan():
#     while True:
#         inputuser = int(input("Masukan Angka : "))
#         hasil1 = inputuser  
#         inputuser2 = int(input("Masukan Angkat : "))
#         hasil2 = inputuser2
#         if hasil1 == 00 and hasil2 == 00:
#             return 
#         else:
#             hasil_total  = inputuser + inputuser2
#             print(hasil_total)

# def perkalian():
#     while True:
#         inputuser = int(input("Masukan Angka : "))
#         hasil1 = inputuser  
#         inputuser2 = int(input("Masukan Angkat : "))
#         hasil2 = inputuser2
#         if hasil1 == 00 and hasil2 == 00:
#             return 
#         else:
#             hasil_total  = inputuser * inputuser2
#             print(hasil_total)

# def perkurangan():
#     while True:
#         inputuser = int(input("Masukan Angka : "))
#         hasil1 = inputuser  
#         inputuser2 = int(input("Masukan Angkat : "))
#         hasil2 = inputuser2
#         if hasil1 == 00 and hasil2 == 00:
#             break 
#         else:
#             hasil_total  = inputuser - inputuser2
#             print(hasil_total)
            
# def menu():
#     print("Masukan Pilihan dibawah")
#     for pilihan in data:
#         print(pilihan)
#     inputuser_menu = int(input("> Masukan Pilihan : "))
#     if inputuser_menu == 1:
#         pertambahan()
        
#     elif inputuser_menu == 2:
#         perkalian()
        
#     if inputuser_menu == 3:
#         perkurangan()
        
# while True:
#     menu()

#========================================================================================================

# a = 1
# a += 1 

# .startswith
# .endwith
# .count
# .upper
# .lower
# .isalpha
# .isalnum
# .isdecimal
# .isspace
# .istitle
# len
# .join
#  .split

#========================================================================================================

# data = ['cuki', 'muki', 'luki']
# print(data[0])

# gabungan = 'cukipmukipluki'.split('p')
# print(gabungan[0])

# judul = "MENU UTAMA".center(50,"=")
# print(judul)


# judul1 = "MENU UTAMA".ljust(50,"=")
# print(judul1)


# judul2 = "MENU UTAMA".rjust(50,"=")
# print(judul2)

#========================================================================================================

# teks = "halo dunia"
# print(teks.startswith("ha"))
# print(teks.count("a"))
# print(teks.upper())
# print(teks.capitalize())
# print(teks.title())
# print(teks.swapcase())
# print(teks.isalpha())
# print(len(teks))
# print(teks.index("h"))




# if len(teks) < 5:
#     print("teks ini dibawah 5 huruf")
# else:
#     print("teks ini diatas 5 huruf")


# akun = {
#     "azhar": {
#         "pw": 123,
#         "nama": "AZHAR RAAFI PRADHITA"
#     },
    
#     "ira": {
#         "pw": 321,
#         "nama": "IRA AULIA"
#     }

 
# }
    

# inputan = input()
# print(akun["azhar"]["pw"])
    
# def menu_login():
#     while True:
#         print('> Silahkan Login untuk melanjutkan : ')
#         inputuser = (input("Username :"))
#         inputpw = int(input("Password :"))

#         if inputuser in akun and akun[inputuser]["pw"] == inputpw:
#             print(f"Login Berhasil, {akun[inputuser]["nama"]}")
#         else:
#             print("Login Gagal")


# # menu_login()


# data = {
#     "password": 1234
# }

# inputan = input(" : ")

# print(data['password'])

# akun = {
#     "azhar": {
#         "pw": "abc123",
#         "pin": {
#             "nilai_pin": "123456",
#             "pin_id": "PIN001"
#         },
#         "nama": {
#             "nama_lengkap": "Azhar Raafi Pradhita",
#             "id": "USR001"
#         }
#     }
# }

# print(akun["azhar"]["pin"]["pin_id"])


# akun = {
#     "azhar": {
#         "pw": "abc123",
#         "nama": "AZHAR"
#     }
# }

# inputan = input("Masukan Usn :")
# inputan2 = input("Masukan Pw :")

# if inputan in akun and akun[inputan]["pw"] == inputan2:
#     print(f"Login berhasil, Selamat Datang {akun[inputan]["nama"]}")

#===================================================================================================

# menu = ['1. Cek Saldo', '2. Lihat PIN ID', '3. Lihat User ID','4. Transfer']

# def menus():
#     while True:
#         for tampilan in menu:
#             print(tampilan)
#         input_menu = input("Masukan Pilihan : ")
#         match input_menu:
#             case "1":
#                 print(f"{"saldo anda sisa :"}{akun[input_dari_username]["bank"]["saldo"]}") 
#             case "2":
#                 print(f"{"Lihat Pin id :"}{akun[input_dari_username]["bank"]["pin"]["id_pin"]}") 
#             case "3":
#                 print(f"{"Lihat user id :"}{akun[input_dari_username]["nama"]["id"]}") 
#             case "4":
#                 nominal_input = int(input("Masukan Nominal : "))
#                 (akun[input_dari_username]["bank"]["saldo"]) -= nominal_input
#                 print('Transaksi Berhasil')



# akun = {
# "azhar": {
#     "pw": "abc123",
#     "nama": {
#         "nama_lengkap": "Azhar Raafi Pradhita",
#         "id": "USR001"
#     },
#     "bank": {
#         "saldo": 1500000,
#         "rekening": "1234567890",
#         "pin": {
#             "nilai": "123456",
#             "id_pin": "PIN001"
#         }
#     }
# },

# "fahri": {
#     "pw": "fahri456",
#     "nama": {
#         "nama_lengkap": "Fahri",
#         "id": "USR002"
#     },
#     "bank": {
#         "saldo": 500000,
#         "rekening": "9876543210",
#         "pin": {
#             "nilai": "654321",
#             "id_pin": "PIN002"
#         }
#     }
# }
# }


# input_dari_username = input("Masukan Username :")
# input_dari_Password = input("Masukan Password :")

# if input_dari_username in akun and akun[input_dari_username]["pw"] == input_dari_Password:
#     print("="*20)
#     print("LOGIN BERHASIL")
#     print(f"Selamat Datang, {akun[input_dari_username]["nama"]["nama_lengkap"]}")
#     print("="*20)
#     print()
#     print(f"{"Nama":<10}: {akun[input_dari_username]["nama"]["nama_lengkap"]}")
#     print(f"{"Id User":<10}: {akun[input_dari_username]["nama"]["id"]}")
#     print(f"{"Rekening":<10}: {akun[input_dari_username]["bank"]["rekening"]}")
#     print(f"{"Saldo":<10}: {akun[input_dari_username]["bank"]["saldo"]}")
#     print(f"{"Pin":<10}: {akun[input_dari_username]["bank"]["pin"]["id_pin"]}")
#     menus()

# else:
#     print("Login Gagal")


# # a = 1000
# # a -= 500

# # print(a)

# # def halo():
# #     print("Halo}")

# # halo()

# akun = {
#     "azhar": {
#         "pw": "123",
#         "nama": "Azhar Raafi Pradhita",
#         "id": "USR001",
#         "saldo": 1000000,
#         "pin": "1111"
#     },
#     "fahri": {
#         "pw": "456",
#         "nama": "Fahri",
#         "id": "USR002",
#         "saldo": 500000,
#         "pin": "2222"
#     }
# }

# print(akun.items())

# inputan = input("Cari id : ")

# for data in akun.values():
#     if data["id"] == inputan:
#         print("Ketemu")
#         break
# else:
#     print("Tidak ketemu")

# akun = {
#     "azhar": {
#         "pw": "123",
#         "profil": {
#             "nama": "Azhar Raafi Pradhita",
#             "id": "USR001",
#             "umur": 17
#         },
#         "saldo": 1000000,
#         "wallet": {
#             "dana": 500000,
#             "gopay": 200000
#         }
#     },
#     "fahri": {
#         "pw": "456",
#         "profil": {
#             "nama": "Fahri",
#             "id": "USR002",
#             "umur": 18
#         },
#         "saldo": 500000,
#         "wallet": {
#             "dana": 300000,
#             "gopay": 100000
#         }
#     }
# }

# inputan = input('Masukan Id : ')
# # for data in akun.values():
# #     if data["profil"]["id"] == inputan:
# #         print('Sesuai')
# #         break
# if inputan in (akun[inputan]["profil"]["id"]):
#     print("sesuai")


#====================================================================================

# import os
# import time
# def clear():
#     os.system('cls' if os.name == "nt" else 'clear')


# akun = {
#     "azhar": {
#         "pw": "123",
#         "nama": "Azhar Raafi Pradhita",
#         "id": "USR001",
#         "saldo": 1000000,
#         "pin": "1111"
#     },
#     "fahri": {
#         "pw": "456",
#         "nama": "Fahri",
#         "id": "USR002",
#         "saldo": 500000,
#         "pin": "2222"
#     }
# }


# menu_utama_list = ["1. Cek Saldo", "2. Lihat ID User", "3. Transfer", "4. Keluar"]

# def login_menu():
#     while True:
#         login_usn = input("Masukan Username :")
#         login_pw = input("Masukan  Password :")
#         if login_usn in akun and login_pw == akun[login_usn]["pw"]:
#             print('Login Berhasil')
#             time.sleep(2)
#             clear()
#             menu_utama(login_usn)
#         else:
#             print('Login Gagal')
#             time.sleep(2)
#             clear()
#             break

# def menu_utama(login_usn):
#     while True:
#         time.sleep(2)
#         clear()
#         print("="*10)
#         print("LOGIN BERHASIL")
#         print("="*10)
#         print("")
#         print(f"Selamat Datang, {akun[login_usn]['nama']}")
#         print(f"User id, {akun[login_usn]['id']}")
#         print(f"Sisa Saldo Anda, {akun[login_usn]['saldo']}")
#         print()

#         for menu in menu_utama_list:
#             print(menu)
#         input_menu = input("Masukan Pilihan : ")
#         match input_menu:
#             case "1":
#                 clear()
#                 print(f'Sisa Saldo Anda : {akun[login_usn]["saldo"]}')
#                 time.sleep(3)
#             case "2":
#                 clear()
#                 print(f'Id User Anda : {akun[login_usn]["id"]}')
#                 time.sleep(3)
#             case "3":
#                 clear()
#                 username_tujuan = input('Masukan Tujuan Transfer : ')
#                 nominal = int(input('Masukan Nominal Transfer : '))
#                 if username_tujuan in akun and nominal <= akun[login_usn]["saldo"] and nominal >= 10000:
#                     akun[login_usn]["saldo"] -= nominal
#                     akun[username_tujuan]["saldo"] += nominal
#                     print("Transaksi Berhasil")
#                     time.sleep(3)
#                 elif username_tujuan not in akun: 
#                     print("Tujuan Tidak Ditemukan")
#                     time.sleep(2)
#                 elif nominal > akun[login_usn]["saldo"]:
#                     print("saldo tidak Cukup")
#                     time.sleep(2)
#                 elif nominal < 10000:
#                     print("Minimal Transaksi Rp 10.000")
#                     time.sleep(2)
#                 else:
#                     print("Transaksi Gagal")
#                     time.sleep(2)
#             case "4":
#                 clear()
#                 print("Terima kasih telah menggunakan bank")
#                 return
#             case _:
#                 print('Masukan Menu yang Valid')
                

        

# login_menu()

#=========================================================================

# persen = 47
# format_persen = f"{persen:.2%}"
# print(format_persen)
# print(type(format_persen))

# plus = +47
# format_plus = f"{plus:+}"
# print(format_plus)
# print(type(format_plus))

# koma = 47.279301
# format_koma = f"{koma:.2f}"
# print(format_koma)
# print(type(format_koma))


# #====

# inputan = float(input('Masukan Nilai : '))
# hasil = [f"1. Nilai Asli : {inputan}", f"2. Nilai Integer : {int(inputan)}",
#          f"3. Nilai 2 Desimal : {inputan:.2f}", f"4. Nilai Persen : {inputan:.2f}%"]

# for menu_hasil in hasil:
#     print(menu_hasil)




inputan = float(input('Masukan Angka Pertama : '))
inputan2 = float(input('Masukan Angka Kedua : '))

hasil_menu = [f'Penjumlahan : {(inputan)+(inputan2)}',
              f'Perkalian : {(inputan)*(inputan2)}',
              f'Pembagian : {(inputan)/(inputan2):.2f}',
              f'Pengurangan : {(inputan)-(inputan2)}']
                    
for hasil in hasil_menu:
    print(hasil)





