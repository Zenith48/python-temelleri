# key - value 

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ['kocaeli', 'istanbul']
plakalar = [41,34]

#print(plakalar[0],sehirler[0])
#print(plakalar[1],sehirler[1])

#print(plakalar.index('istanbul'))

plakalar = {'kocaeli': 41, 'istanbul': 34}

#print(plakalar['kocaeli'])
#print(plakalar['istanbul'])

plakalar['rize'] = 53

#print(plakalar)

ogrenciler = {
    100: {
        "ad": "Agit",
        "soyad": "Zenith",
        "yas": 19
    },
    101: {
        "ad": "Eren",
        "soyad": "Yeager",
        "yas": 21
    }

}

sonuc = ogrenciler[100]["ad"]

print(sonuc)


