#Basit hesap makinesi

def toplama(x , y) :
    return x + y
def çıkarma(x , y) :
    return x - y
def çarpma(x , y) :
    return x * y 
def bölme(x , y) :
    if y == 0 :
        print("Bir sayıyı 0'a bölemezsin!")
    return x / y 

print("Seçiminizi yapınız")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçimizi yapınız (1/2/3/4) : ")

sayi1 = float(input("Birinci sayıyı giriniz:"))
sayi2 = float(input("İkinci sayıyı giriniz:"))

if secim == '1' :
    print(f"{sayi1} + {sayi2} = {toplama(sayi1 , sayi2)}")
elif secim == '2' :
    print(f"{sayi1} - {sayi2} = {çıkarma(sayi1 , sayi2)}")
elif secim == '3' :
    print(f"{sayi1} * {sayi2} = {çarpma(sayi1 , sayi2)}")
elif secim == '4' :
    print(f"{sayi1} / {sayi2} = {bölme(sayi1 , sayi2)}")
else : 
    print("Yanlış sayı girdiniz")

