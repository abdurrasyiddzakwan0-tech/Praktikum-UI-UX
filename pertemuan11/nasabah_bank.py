from Bank import *

#bikin objek
siti = Bank('001','Siti Aminah',500000)
desi = Bank('002','Desi Ratnasari',700000)
dedi = Bank('003','Dedi Mulyadi',800000)
budi = Bank('004','Budi Santoso',300000)
Zaki = Bank('005','Muhammad Zaki',400000)
#consume
siti.nabung(200000)
budi.nabung(600000)
dedi.tarik(300000)
budi.tarik(100000)

siti.cetak()
desi.cetak()
dedi.cetak()
budi.cetak()
Zaki.cetak()

print("Jumlah Nasabah: %i orang" %Bank.jmlNasabah)

