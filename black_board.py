import time
from colorama import Fore, Style, init
init(autoreset=True)


# main_menu_pilihan = ["[1] Sign Up", "[2] Sign In", "[3] Exit"]
# data_user = {
#     "username": "admin",
#     "password": "admin123"
# }


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



# main_menu()



def quiz():
    inputan = int(input("Apa coba : "))
    pilihan = inputan
    match inputan:
        case 1 | 2 | 3:
            print("Jawaban kamu benar!")
        case _:
            print("Jawaban kamu salah.")

quiz()