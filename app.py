from gudang import *
import datetime as dt
from dateutil.relativedelta import relativedelta as rd

newGudang = Gudang()

print('\n========================================')
print('[i] Select Menu')
print('========================================')
newGudang.pilihan()

while True:
    inpSelect = input("\n[=] Pilih Menu: ")
    cur.execute("select count(*) as count from item")
    for r in cur.fetchall():
        ct = r[0]

    if(inpSelect == '1'):
        newGudang.info()       
        newGudang.pilihan()
    elif(inpSelect == '2'):
        newGudang.tampil_kategori()
        catid = newGudang.pilih_kategori()
        while True:
            inpName = input("\n[=] Masukkan Nama Barang : ")
            inpStock = input("[=] Masukkan Stock Barang : ")               
            inpPrice = input("[=] Masukkan Harga Barang : ")
            if(inpName == "" or inpStock == "" or inpPrice == ""):
                print("\n[i] Input tidak boleh kosong!\n")
            else:
                if(catid == 1):
                    while True:
                        inpNetto = input("[=] Masukkan Netto/Berat Bersih Barang : ")
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        if(inpNetto == "" or inpBrand == "" or inpComp == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            expdate = dt.datetime.utcnow() + rd(years = 5)
                            newBev = Beverage(0, inpName, catid, inpStock, inpPrice, expdate, inpNetto, inpBrand, inpComp)
                            newBev.tambah()
                            break
                elif(catid == 2):
                    while True:
                        inpNetto = input("[=] Masukkan Netto/Berat Bersih Barang : ")
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        if(inpNetto == "" or inpBrand == "" or inpComp == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            expdate = dt.datetime.utcnow() + rd(years = 5)
                            newBev = Food(0, inpName, catid, inpStock, inpPrice, expdate, inpNetto, inpBrand, inpComp)
                            newBev.tambah()
                            break
                elif(catid == 3):
                    while True:
                        inpNetto = input("[=] Masukkan Netto/Berat Bersih Barang : ")
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        inpUsage = input("[=] Masukkan Kegunaan Barang : ")
                        if(inpNetto == "" or inpBrand == "" or inpComp == "" or inpUsage == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            newBev = Cleaner(0, inpName, catid, inpStock, inpPrice, inpNetto, inpBrand, inpComp, inpUsage)
                            newBev.tambah()
                            break
                elif(catid == 4):
                    while True:
                        inpNetto = input("[=] Masukkan Netto/Berat Bersih Barang : ")
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        inpUsage = input("[=] Masukkan Kegunaan Barang : ")
                        if(inpNetto == "" or inpBrand == "" or inpComp == "" or inpUsage == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            newBev = PersonalCare(0, inpName, catid, inpStock, inpPrice, inpNetto, inpBrand, inpComp, inpUsage)
                            newBev.tambah()
                            break
                elif(catid == 5):
                    while True:
                        inpNetto = input("[=] Masukkan Netto/Berat Bersih Barang : ")
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        inpUsage = input("[=] Masukkan Kegunaan Barang : ")
                        if(inpNetto == "" or inpBrand == "" or inpComp == "" or inpUsage == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            newBev = Other(0, inpName, catid, inpStock, inpPrice, inpNetto, inpBrand, inpComp, inpUsage)
                            newBev.tambah()
                            break
                elif(catid == 6):
                    while True:
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpComp = input("[=] Masukkan Komposisi Barang : ")
                        inpUAdvice = input("[=] Masukkan Anjuran Penggunaan Barang : ")
                        inpUsage = input("[=] Masukkan Kegunaan Barang : ")
                        if(inpUAdvice == "" or inpBrand == "" or inpComp == "" or inpUsage == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            expdate = dt.datetime.utcnow() + rd(years = 2)
                            newBev = Medicine(0, inpName, catid, inpStock, inpPrice, expdate, inpBrand, inpComp, inpUAdvice, inpUsage)
                            newBev.tambah()
                            break
                elif(catid == 7):
                    while True:
                        inpBrand = input("[=] Masukkan Brand Barang : ")
                        inpUsage = input("[=] Masukkan Kegunaan Barang : ")
                        if(inpBrand == "" or inpComp == "" or inpUsage == ""):
                            print("\n[i] Input tidak boleh kosong!\n")
                        else:
                            newBev = HomeAppliance(0, inpName, catid, inpStock, inpPrice, inpBrand, inpUsage)
                            newBev.tambah()
                            break
                break

    elif(inpSelect == '3'):
        if(ct == 0):
            print("\n[i] Tabel Data masih kosong!")
        else:
            print("\n[i] Anda akan mengubah beberapa atribut barang.")
            newGudang.hapus()      
    elif(inpSelect == '4'):
        print("\n[i] Good Bye")
        break
    else:
        print("\n[!] Input Salah")

db.close()