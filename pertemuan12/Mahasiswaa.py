from Personn import *

class Mahasiswaa(Personn):
    nim = ""
    prodi = ""
    semester = ""

    def __init__(self, nama, gender, umur, nim, prodi,semester):
        super().__init__(nama, gender, umur)
        self.nim = nim
        self.prodi = prodi
        self.semester = semester

    def cetak(self):
        print(f"NIM \t: {self.nim}")
        print(f"Prodi \t: {self.prodi}")
        print(f"semester: {self.semester}")