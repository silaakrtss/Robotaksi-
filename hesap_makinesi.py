def hesap_makinesi():
    print("Lütfen işlem yapmak istediğiniz iki sayıyı ve işlem türünü giriniz.")
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
        islem = input("Yapmak istediğiniz işlemi giriniz (+, -, *, /): ")

        if islem == "+":
            sonuc = sayi1 + sayi2
            print(f"Sonuç: {sonuc}")
        elif islem == "-":
            sonuc = sayi1 - sayi2
            print(f"Sonuç: {sonuc}")
        elif islem == "*":
            sonuc = sayi1 * sayi2
            print(f"Sonuç: {sonuc}")
        elif islem == "/":
            try:
                sonuc = sayi1 / sayi2
                print(f"Sonuç: {sonuc}")
            except ZeroDivisionError:
                print("Bir sayı 0'a bölünemez!")
        else:
            print("Hatalı işlem. Lütfen +, -, *, / işlemlerinden birini giriniz!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")


hesap_makinesi()
