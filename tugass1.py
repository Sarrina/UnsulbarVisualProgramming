print('==========================')
print('SARINA_D0219413')
print('Tugas Pemrograman Visual')
print(' 1. Penjumlahan ')
print(' 2. Pengurangan ')
print(' 3. Perkalian ')
print(' 4. Pembagian ')
print('==========================')

def a (x, y):
    return x + y

def b (x, y):
    return x - y

def c (x, y):
    return x * y

def d (x, y):
    return x / y


op = input ("Masukkan Pilihan : ")
bil1 = int (input ("Masukkan Bilangan 1: "))
bil2 = int (input ("Masukkan Bilangan 2: "))

if op == '1':
    print (bil1, " + ", bil2, " = ", a(bil1, bil2))

elif op == '2':
    print (bil1, " - ", bil2, " = ", b(bil1, bil2))

elif op == '3':
    print (bil1, " * ", bil2, " = ", c(bil1, bil2))

elif op == '4':
    print (bil1, " / ", bil2, " = ", d(bil1, bil2))

else :
    print ("EROR")
    
