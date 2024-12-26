from datetime import datetime

def gunluk_yaz():
    with open("gunluk.txt","a",encoding="utf-8") as file:
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yazi = input("Bugün ne yaptınız?")
        file.write(f"{tarih} - {yazi}\n")

def gunluk_oku():
    with open("gunluk.txt","r",encoding="utf-8") as file:
        icerik = file.read()
        print(icerik)

secim = input("1- Günlük Yaz\n2-Günlük Oku\nSeçiminiz: ")

if secim == "1":
    gunluk_yaz()
elif secim == "2":
    gunluk_oku()
else:
    print("Geçersiz Seçim!")