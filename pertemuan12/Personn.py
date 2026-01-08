class Personn:
    nama = ""
    gender = ""
    umur = 0

    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    def cetak(self):
        print(f"Nama \t: {self.nama}")
        print(f"Gender \t: {self.gender}")
        print(f"Umur \t: {self.umur} tahun")

orang1 = Personn("Wafi", "L", 17)

orang1.nama = "Wafi"
orang1.gender = "L"
orang1.umur = 17

orang1.nama = "Siti Aisyah"
orang1.gender = "perempuan"
orang1.umur = 21


orang1.cetak()