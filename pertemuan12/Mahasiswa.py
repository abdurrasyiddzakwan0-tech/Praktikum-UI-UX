from Person import *

class Mahasiswa(Person):
    prodi = ""
    semester = 0
    IPK = 0

    def __init__(self,nama,gender,umur,prodi,semester,IPK):
        super().__init__(nama,gender,umur)
        self.prodi = prodi
        self.semester = semester
        self.IPK = IPK
        
    def cetak(self):
        super().cetak()
        print("-----------------------------"
              "\nProdi\t: %s"
              "\nSemester\t: %i"
              "\nIPK\t: %.2f "
              %(self.prodi,self.semester,self.IPK)
              )