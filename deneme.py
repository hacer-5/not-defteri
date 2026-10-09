# puanlar = [45, 78, 90, 22, 85, 90, 60, 33]
# # Sıralama ve Ekleme: Bu listeye önce 100 puanını sonradan ekle (append), ardından 
# # listeyi küçükten büyüğe sırala (sort). Son halini ekrana yazdır.
# # puanlar.append(100)
# # print(puanlar)
# # # puanlar.sort()
# # # puanlar.reverse()
# # # print(puanlar)
# # puanlar.sort(reverse=True)
# # print(puanlar)
# puanlar1=str(puanlar)
# puanlar2="-".join(puanlar1)
# print(puanlar2)

sayilar = [12, 5, 8, 19, 24, 7, 30]
print("Orijinal Liste:", sayilar)

print(min(sayilar))  # En küçük sayıyı bulma
print(max(sayilar))  # En büyük sayıyı bulma
print(sum(sayilar))  # Sayıların toplamını bulma

print("Sıralanmış Liste:", sayilar.sort())  