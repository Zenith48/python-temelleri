# 1- Girişen bir sayının 50-100 arasında olup olmadığını kontrol edin.

# sayi = int(input('sayı: '))
# sonuc = (sayi > 50) and (sayi < 100)
# if sonuc:
#     print(f"{sayi}, 50 ile 100 arasındadır.")
# else :
#     print(f"{sayi}, 50 ile 100 arasında değildir.")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol edin.
sayi = int(input('sayı: '))
tek = sayi%2
pozitif = (sayi > 0)
if pozitif:
    if (tek == 1):
        print(f"{sayi}, pozitiftir ve tektir.")
elif (sayi < 0):
    if (tek == 1):
        print(f"{sayi}, negatiftir ama tektir.")