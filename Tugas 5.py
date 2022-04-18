print("Sarina_D0219413_Tugas_5")
class Tas:

     def __init__(self, nama, warna):
         self.nama = nama     
         self.warna = warna

class Ransel(Tas):
     def jual(self):
         print("Tas Ransel terjual")

totebag = Ransel("Pink", "Maroon")
 
print(totebag.nama)
totebag.jual()


print(totebag.warna)
totebag.jual()
