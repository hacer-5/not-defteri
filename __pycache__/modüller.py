# Random modülü
# import random

# for i in range(10):
#     print(random.random()) #sıfır ile 1 rasında rastegele degerler için kullanılır

# for i in range(10):
#     print(random.uniform(10,30))# belirli aralılarla sayı uretme

# for i in range(10):
#     print(random.randint(1,5))# 1 ıle 5 arasında ıkısıde dahıl random tam sayılar

# for i in range(10):
#     print(random.randrange(1,10,2)) #2 şer artarak random sayılar

# listeden rastegele eleman secme random.choice(listename)
# list1=["siyah","beyaz","mavi","yeşil"]
# print(random.choice(list1))

# random.shuffle(list1) # listeyi karıstırıyor
# print(list1)
# import random
# list1=["siyah","beyaz","mavi","yeşil"]
# print(random.sample(list1,3)) # listeden 3 tane rastgele sec

# zarlar={1:0,2:0,3:0,4:0,5:0,6:0}
# for i in range(100):
#     zar=random.randint(1,6)
#     zarlar[zar]+=1

# for zar in zarlar:
#     print(f"{zar} gelme olasılığı: {zarlar[zar]/100}")   

# denemesayisi=0
# denkgelmesayisi=0
# while True:
#     denemesayisi+=1
#     ilk_zar=random.randint(1,6)
#     ikinci_zar=random.randint(1,6)
#     if ilk_zar==6 and ikinci_zar==6:
#         denkgelmesayisi+=1

#     if denkgelmesayisi== 10:
#         print(f"6-6 gelmesi için {denemesayisi} tane deneme yapıldı")
#         break

#TIME MODÜLÜ
# import time
# zaman=time.time()
# print(zaman) # 1 ocak 1970 den beri geçen toplam saniye

# KODUN KAÇ SANİYEDE ÇALIŞTIĞINI ÖLÇMEK İÇİN KULLANILIR
# baslangic=time.time()
# list1=[]
# for i in range(100000000):
#     list1.append(i)
# bitiszamanı=time.time()
# print(bitiszamanı-baslangic)

# zaman=time.ctime()
# print(zaman) şimdiki zaman
# zaman=time.ctime(100000000)
# print(zaman) #baslangıctan 
# #ıtıbaren bu kadra snıye sonra hangı gun olur

# localtime() zamanı bana değişik formatta ayıra ayıra verıyor
# asctime ctime aynısı sadece içine değer yazarsak hata verir localtime yazarsak 
# parametrenın ıcıne ctıme gıbı formatta yazdırır

# strftime
# zaman=time.strftime("%d:%m:%Y %H:%M:%S") # istediğin fornatta yazma
# print(zaman)

# PROGRAM NE KADRA BEKLESIN
# SUAN 3 SANIYE BEKLIYOR IKI KOD ARASI
# print("program başladı")
# time.sleep(3)
# print("program sonlandı")

# from datetime import date
# bugun=date.today()
# print(bugun)
# print(type(bugun))
# print(bugun.day)
# print(bugun.month)
# print(bugun.year)
# print(bugun.weekday()) #index
# print(bugun.isoweekday())#kacıncu gun

# gecmis_tarih=date(2015,8,13)
# print(gecmis_tarih)
# print(gecmis_tarih.weekday())

# gecen_zaman = bugun-gecmis_tarih
# print(gecen_zaman)

from datetime import datetime
suan = datetime.now()
# print(suan)
# print(type(suan))
# print(suan.day)
# print(suan.month)
# print(suan.year)
# print(suan.hour)
# print(suan.minute)
# print(suan.second)
# print(datetime.ctime(suan))
# print(suan.ctime())
# print(suan.date())
# print(suan.time())
# print(suan.date().month)

gecmis_zaman=datetime(2018,3,5,7,23,27,12)
print(suan-gecmis_zaman)


