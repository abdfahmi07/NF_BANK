import menu
import random, string

def buka():
    # silahkan isi logika anda di dalam fungsi ini
    print(end="\n")
    print("*** BUKA REKENING ***")

    listNasabah = []

    nasabah = open('nasabah.txt')
    for element in nasabah:
        data = element.split(',')
        rekNum = data[0]
        nama = data[1]
        balance = data[2]
        listNasabah.append([rekNum, nama, balance])
    nasabah.close()

    nama = input("Masukkan Nama: ")
    setoranAwal = int(input('Masukkan nominal yang akan disetor: '))
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    listNasabah.append([norek, nama, setoranAwal])
    
    nasabah = open('nasabah.txt', 'w+')
    itemElement = str(listNasabah).replace('[','').replace(']','').replace("'",'').replace(' ','')
    nasabah.write(itemElement + '\n')
    nasabah.close()

    print(end='\n')


    






    # balik dan cetak list menu kembali untuk memilih menu,
    # jika menu ini sudah selesai dilakukan.
    menu.mainMenu()