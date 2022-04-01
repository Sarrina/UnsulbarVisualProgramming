class produk:
    pass

tn1 = produk()
tn2 = produk ()
tn3 = produk  ()

tn1.nama = 'TAS'
tn1.jumlah = '2'

tn2.nama = 'Baju'
tn2.jumlah = '4'

tn3.nama = 'Sepatu'
tn3.jumlah = '6'

print(tn1.__dict__, tn2.__dict__, tn3.__dict__)
