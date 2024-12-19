import random

sayı = random.randint(1,100)
tahmin_hakkı = 7

while True :
    tahmin = int(input("Bir tahmin giriniz (1-100):"))

    if tahmin == sayı :
        print("Tebrikler doğru tahmin!")
        break

    elif tahmin > sayı :
        print("Daha küçük bir sayı giriniz.")

    else :
        print("Daha büyük bir sayı giriniz")

    tahmin_hakkı -= 1
    if tahmin_hakkı == 0 :
        print("Tahmin hakkınız bitmiştir")
        print("Doğru sayı" , sayı  , "idi.")
        break