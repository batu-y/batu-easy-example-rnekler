# birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
# onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
#
#
# def okunus(sayı):
#     birinci = sayı % 10
#     ikinci = sayı // 10
#
#     return onlar[ikinci] + " " + birler[birinci]
#
#
# sayı = int(input("Sayı:"))
#
# print(okunus(sayı))

# 10'un altında 3 veya 5'in katları olan tüm doğal sayıları listelersek, 3, 5, 6 ve 9'u alırız. Bu katların toplamı 23'tür.
#
# 1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.


toplam = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        toplam += i

print(f"1000'in altındaki 3 veya 5'in tüm katlarının toplamı: {toplam}")