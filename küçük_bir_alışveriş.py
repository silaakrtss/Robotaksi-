def alışveriş_sepeti():
    
    ürünler = ["çizme", "kaban", "bluz", "gömlek", "etek", "çanta"]
    sepet = []

    print("Ürünlerimiz:")
    for ürün in ürünler:
        print(f"- {ürün}")
    
    print("\nAlışverişe başlamak için bir ürün seçin veya 'bitti' yazın.")

    while True:
        ürün = input("\nSepetinize eklemek için bir ürün adı girin: ").lower()

        if ürün == "bitti":
            break
        elif ürün in ürünler:
            sepet.append(ürün)
            print(f"{ürün} sepete eklendi.")
        else:
            print("Bu ürün listede bulunmamaktadır, lütfen geçerli bir ürün girin.")
    
    print("\nAlışveriş Sepetiniz:")
    if sepet:
        for sepetim in sepet:
            print(f"- {sepetim}")
alışveriş_sepeti()
