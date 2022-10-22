import string
from xmlrpc.client import boolean


nama = input("masukkan nama :")
umur = int(input("masukkan umur anda :"))
tinggi = float(input("masukkan tinggi anda :"))
status = boolean(input("masukkan status :"))
hobby = string(input("masukkan hobby anda :"))

print("nama : ", nama)
print("umur : " ,umur)
print("tinggi : " ,tinggi)
print("status : " ,status)
print("hobby : " ,hobby)
