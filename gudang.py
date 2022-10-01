import mysql.connector
import datetime as dt
from prettytable import PrettyTable as pt

db = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "gudang" 
)

cur = db.cursor()

class Gudang:
    def __init__(self, id = 0, name = "", catid = 0, stock = 0, price = 0, input_date = ""):
        self.id = id
        self.name = name
        self.catid = catid
        self.stock = stock
        self.price = price
        self.input_date = input_date

    def pilihan(self):
        main_menu = ["[1] LIHAT DATA ITEM", 
                "[2] TAMBAH DATA ITEM", 
                "[3] HAPUS DATA ITEM",
                "[4] KELUAR DARI APP"]
        
        for i in main_menu:
            print(i)

    def info(self):
        colItems = ['Id', 'Nama Barang', 'Kategori', 'Stok', 'Harga', 'Tanggal Input',
                    "Tanggal Kadaluarsa", "Berat Bersih", "Brand", "Komposisi", "Kegunaan", "Anjuran Pemakaian"]
        print("\n[i] Daftar Barang\n")
        cur.execute("""select 
                        item.ID as 'Id', item.name, category.name, item.stock, item.price,item.inputdate,
                        item.exp_date, item.netto, item.brand, item.composition, item.usages, item.usage_advice
                        from item left join category on item.catID = category.ID
                    """)
        
        newPT = pt()
        newPT.field_names = colItems
        for r in cur.fetchall():
            newPT.add_row(r)
        print(f"{newPT}\n")

    def tampil_kategori(self):
        colCat = ['Id', 'name Kategori']
        print("\n[i] name Kategori\n")
        cur.execute("""select ID as 'Id', name as 'name Kategori' from category""")
        newPT = pt()
        newPT.field_names = colCat
        for r in cur.fetchall():
            newPT.add_row(r)
        print(newPT)
        
    def pilih_kategori(self):
        print("\n[i] Untuk memasukkan kategori anda bisa mengisinya dengan Id maupun name dari kategori tersebut.")
        inpCat = input("\n[=] Masukkan Id/name Kategori : ")
        while True:
            if(inpCat == ""):
                break
            elif(inpCat.isdigit()):
                cur.execute("select * from category where ID=%s", (inpCat,))
                row = cur.fetchone()
                if row == None:
                    print("\n[i] Tidak ada kategori yang ber-ID " + inpCat)
                    return self.pilih_kategori()
                else:
                    self.catid = row[0]
                    print("\n[i] Kategori yang anda pilih adalah " + row[1])
                    #break
                    return self.catid
            else:
                cur.execute("select * from category where name like %s", (inpCat,))
                row = cur.fetchone()
                if row == None:
                    print("\n[i] Tidak ada kategori yang bername " + inpCat)
                    return self.pilih_kategori()
                else:
                    self.catid = row[0]
                    print("\n[i] ID Kategori yang anda pilih adalah " + str(row[0]))
                    #break
                    return self.catid

    def tambah(self, name = "", catid = "", stock = "", price = "",
    exp_date = "", netto = "", brand = "", komposisi = "", anjuran = "", kegunaan = ""):
        print("\n[i] Anda akan memasukkan barang baru ke server.")
        cur.execute("""insert into item (name, catID, stock, price, inputdate, 
                    exp_date, netto, brand, composition, usages, usage_advice) 
                    values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                    (name, catid, stock, price, dt.date.today(),
                    exp_date, netto, brand, komposisi, anjuran, kegunaan),)
        db.commit()
        print("\n[i] Data berhasil ditambahkan.\n")
        self.pilihan()

    def hapus(self):
        self.info()
        print("[i] Masukkan ID atau name barang untuk menghapus.")
        print("[i] Masukkan 0 atau Exit untuk kembali ke Menu Pilihan.")
        while True:
            inpID = input("[=] Masukkan ID atau name barang : ")
            if(inpID == ""):
                print("[!] Input tidak boleh Kosong")
            elif(inpID.isdigit()):
                cur.execute("select * from item where ID=%s", (inpID,))
                row = cur.fetchone()
                if row == None:
                    print("\n[i] Tidak ada barang yang ber-ID " + inpID)
                else:
                    inpID = row[0]
                    print("\n[i] Barang yang anda pilih adalah " + row[1])
            elif(inpID == "0" or inpID == "exit" or inpID == "Exit" or inpID == "EXIT"):
                return
            else:
                cur.execute("select * from item where name like %s", (inpID,))
                row = cur.fetchone()
                if row == None:
                    print("\n[i] Tidak ada barang yang bername " + inpID)
                else:
                    inpID = row[0]
                    print("\n[i] ID Kategori yang anda pilih adalah " + str(row[0]))
                
                    print("[i] Apakah anda yakin ingin menghapus data ini?")
                    inpUsure = input("[=] Y/N : ")
                    if(inpUsure == "y" or inpUsure == "Y"):
                        cur.execute("delete from item where id=%s", (inpID,))
                        db.commit()
                        print("\n[i] Data berhasil dihapus.\n")
                        self.pilihan()
                        break
                    elif(inpUsure == "n" or inpUsure == "N"):
                        break
                    else:
                        continue

class Food(Gudang):
    def __init__(self, id, name, catid, stock, price,
            exp_date, netto, brand, komposisi):
        super().__init__(id, name, catid, stock, price)
        self.exp_date = exp_date
        self.netto = netto
        self.brand = brand
        self.komposisi = komposisi

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    self.exp_date, self.netto, self.brand, self.komposisi, "", "")
            
class Beverage(Gudang):
    def __init__(self, id, name, catid, stock, price,
            exp_date, netto, brand, komposisi):
        super().__init__(id, name, catid, stock, price)
        self.exp_date = exp_date
        self.netto = netto
        self.brand = brand
        self.komposisi = komposisi

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    self.exp_date, self.netto, self.brand, self.komposisi, "", "")

class Medicine(Gudang):
    def __init__(self, id, name, catid, stock, price,
            exp_date, brand, komposisi, anjuran, kegunaan):
        super().__init__(id, name, catid, stock, price)
        self.exp_date = exp_date
        self.brand = brand
        self.komposisi = komposisi
        self.anjuran = anjuran
        self.kegunaan = kegunaan

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    self.exp_date, "", self.brand, self.komposisi, self.anjuran, self.kegunaan)

class Other(Gudang):
    def __init__(self, id, name, catid, stock, price,
            netto, brand, komposisi, kegunaan):
        super().__init__(id, name, catid, stock, price)
        self.netto = netto
        self.brand = brand
        self.komposisi = komposisi
        self.kegunaan = kegunaan

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    "", self.netto, self.brand, self.komposisi, self.kegunaan, "")

class PersonalCare(Gudang):
    def __init__(self, id, name, catid, stock, price,
            netto, brand, komposisi, kegunaan):
        super().__init__(id, name, catid, stock, price)
        self.netto = netto
        self.brand = brand
        self.komposisi = komposisi
        self.kegunaan = kegunaan

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    "", self.netto, self.brand, self.komposisi, self.kegunaan, "")

class Cleaner(Gudang):
    def __init__(self, id, name, catid, stock, price,
            netto, brand, komposisi, kegunaan):
        super().__init__(id, name, catid, stock, price)
        self.netto = netto
        self.brand = brand
        self.komposisi = komposisi
        self.kegunaan = kegunaan

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    "", self.netto, self.brand, self.komposisi, self.kegunaan, "")

class HomeAppliance(Gudang):
    def __init__(self, id, name, catid, stock, price, brand, kegunaan):
        super().__init__(id, name, catid, stock, price)
        self.brand = brand
        self.kegunaan = kegunaan

    def tambah(self):
        Gudang.tambah(self, self.name, self.catid, self.stock, self.price,
    "", "", self.brand, "", self.kegunaan, "")