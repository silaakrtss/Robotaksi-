import random  

def sayi_tahmin_oyunu():
    bilinmeyen_sayi = random.randint(1, 100)
    tahmin_sayisi = 0 

    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin!")

    while True:
        try:
            tahmin = int(input("Tahmininizi girin: ")) 
            tahmin_sayisi += 1  

            if tahmin < bilinmeyen_sayi:
                print("Çok küçük! Tekrar dene.")
            elif tahmin > bilinmeyen_sayi:
                print("Çok büyük! Tekrar dene.")
            else:
                print(f"Tebrikler! {bilinmeyen_sayi} sayısını doğru tahmin ettiniz!")
                print(f"{tahmin_sayisi} deneme sonunda başardınız!")
                break  # Döngüden çık
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")  

sayi_tahmin_oyunu()
