# Elif koşul ifadesi, if ve else'nin ikisinin de doğru olmadığı durumlarda kullanulır.

# x = 20
# y = 20

# if x > y:
#     print("x y'den büyüktür")
# elif x == y:
#     print("x y'ye eşittir")
# else:
#     print("y x'ten büyüktür")

sayi = int(input("sayı: "))

if sayi > 0:
    print("sayı pozitiftir")
elif sayi == 0:
    print("sayı 0'dır")
else:
    print("sayı nedatiftir")
