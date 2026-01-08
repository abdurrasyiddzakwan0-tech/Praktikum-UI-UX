from Personn import *

class Dosenn(Personn):
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self, nama, gender, umur, gelar, jabatan, gaji = 0):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
        self.gaji = gaji

    def setGaji(self,uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print(f"Gelar\t: {self.gelar}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Gaji \t: Rp {self.gaji}")