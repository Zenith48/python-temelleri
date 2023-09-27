sayilar = [1,2,3,4,5,60]
harfler = ['abc','b','e','s','ac','y']

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

#ekleme
sayilar.append(10)
sayilar.insert(-3,50)

#silme
sayilar.pop() #eleman siler(sondan)
sayilar.remove(4) #seçilen elemanı siler

#sıralama
sonuc = sayilar.sort() #küçükten büyüğe
harfler.sort() #küçükten büyüğe
sayilar.reverse() #büyükten küçüğe

sonuc = sayilar
sonuc = harfler

print(sonuc)