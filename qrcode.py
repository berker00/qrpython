import pyqrcode

x = input("LINK GIRIN : ")

url = pyqrcode.create(x)

print("QR KOD 'qr_kod.png' OLARAK KAYDEDILDI! ")

print("AUTHOR : BERKER KESKIN")

url.png('qr_kod.png', scale=6)