import myModul
import myModul as hitung
from myModul import tambah,pangkat
from myModul import*
from myModul import tambah as t,pangkat as p

print('-----------cara1 menggunakan modul----------')
myModul.tambah(2,3)
myModul.pangkat(2,3)
myModul.kali(2,3)
myModul.bagi(2,3)
myModul.kurang(2,3)

print('-----------cara2 mengaliaskan nama modul----------')
hitung.tambah(2,3)
hitung.bagi(2,3)
hitung.kali(2,3)
hitung.kurang(2,3)
hitung.pangkat(2,3)

print('-----------cara3 memanggil sebagian fungsi----------')
tambah(4,6)
pangkat(4,6)

print('-----------cara4 memanggil semua fungsi----------')
tambah(19827,10928)
pangkat(9,5)
kali(21,7)
bagi(300,15)
kurang(1789,998)

print('-----------cara5 mengasliaskan nama fungsi----------')
t(189,1290)
p(7,8)
