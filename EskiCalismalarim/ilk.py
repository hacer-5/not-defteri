#STRİNGLER
# mesaj1="merhaba"
# mesaj2="dunya"
# print(mesaj1+"\n "+ mesaj2 )
# print (mesaj1[-1])
# print(mesaj1[1:4])
# print(mesaj1[::-1])
# print(mesaj1.upper())
# print(mesaj1.capitalize())
# print(mesaj1.startswith("Mer"))
# print(len(mesaj1+mesaj2))
# print("merhaba" * 10)
# isim ="hacer"
# yaş="20"
# print("{} , {} yaşındadır".format("yar",15))

# INTEGER - FLOAT

# sayi1=5 ** 100;
# sayi2=3.8;
# print(type(sayi2))
# print(sayi1)

#Matematiksel işlemler

#Toplama         " + "
#Çıkarma        " - "
#Çarpma         " * "
#Bölme          " / "
#Tamsayı bölmesi "//"
#Kuvvet Alma    "**"
#Mutlak Değer   "abs"
#Yuvarlama      "round"

# String ve integerları birine çevirmek için kullanılan fonksiyonlar
# int()  -  float()  -  str()
# sayı1="6";
# sayı2=6;
# print((int(sayı1)) == sayı2)
# sayı1=int(sayı1)
# print(sayı1 == sayı2)

# sayı3=3.9;
# sayı4=int(sayı3)
# print(sayı4)

# sayi7=6;
# str1=str(sayi7)
# print(type(str1))

#LİSTELER
# renkler=["siyah","beyaz","sarı","mavi","yeşil"]
# print(type(renkler))
# print(len(renkler))
# print(renkler[-1])
# print(renkler[1:4])
# print(renkler)

# # append -listenın sonuna eleman ekleme
# renkler.append("lacivert")
# print(renkler)

# # insert - listenın istediğimiz indexine eleman ekleme
# renkler.insert(3,"gri")
# print(renkler)

# # remove - listenın istediğimiz elemanını silme
# renkler.remove("sarı")
# print(renkler)

# # extend - birden fazla elemanı listeye ekleme

# renkler2=["turuncu","pembe"]
# renkler.append(renkler2)
# print(renkler)
# # ['siyah', 'beyaz', 'gri', 'mavi', 'yeşil', 'lacivert', ['turuncu', 'pembe']] 
# # listenin kendisini append ile içindekileri tek tek extend ile ekliyorum
# renkler.extend(renkler2)
# print(renkler) 
# # ['siyah', 'beyaz', 'gri', 'mavi', 'yeşil', 'lacivert', 'turuncu', 'pembe']

# pop - listenın sonundaki elemanı siler ve silinen elemanı geri döndürür

# silinen=renkler.pop()
# print(silinen)
# print(renkler)

# # REVERSE - listenin elemanlarını ters çevirir
# renkler.reverse()
# print(renkler)

# # SORT - listenin elemanlarını sıralar
# renkler.sort()
# print(renkler)

# # listeyi tersten sırlamak için önce listeyi sırala sonra reverse ile ters çevir
# renkler.reverse()
# print(renkler)

# #  listeyi ters çevirmeyi tek hamlede yapmak
# print(renkler)
# renkler.sort(reverse=True) # sıralamayı tersten yap demek tek satırda
# print(renkler)
#

# # SORTED -LİSTEYİ SIRALAMK İSTORSAK AMA AYNI ZAMANDA ESKI LİSTE DE AYNI KLASIN İSTİYORSAK
# print(renkler)
# renkler_sirali=sorted(renkler)
# print(renkler_sirali)
# print(renkler)

# #  MİN- MAX -IN
# renkler=["siyah","beyaz","sarı","mavi","yeşil"]
# sayılar=[2,5,8,2,9,34]
# print(min(renkler))
# print(min(sayılar))
# print(max(renkler))
# print(max(sayılar))

# # SUM
# print(sum(sayılar))

# renkler=["siyah","beyaz","sarı","mavi","yeşil"]
# sayılar=[2,5,8,2,9,34]

# #  FOR - İN
# for i in renkler:
#     print(i)

# # enumerate bir listeyi numaralandırıyor ve index numarası ile birlikte elemanları döndürüyor
# #  for olmadan kullanımda elemanları once lısteye donusturuyoruz
# print(list(enumerate(renkler)))
# # [(0, 'siyah'), (1, 'beyaz'), (2, 'sarı'), (3, 'mavi'), (4, 'yeşil')]
# print(list(enumerate(renkler,start=2)))
# # [(2, 'siyah'), (3, 'beyaz'), (4, 'sarı'), (5, 'mavi'), (6, 'yeşil')]

# # IN
# print("siyah" in renkler)  # True
# print("mor" in renkler)    # False

# # JOIN
# # listeyi tek metın dosyasına cevırmek ıcın
# stringrenkler="-".join(renkler )
# print(stringrenkler)
# # siyah-beyaz-sarı-mavi-yeşil
# stringrenkler="".join(renkler )
# print(stringrenkler)
# # siyahbeyazsarımaviyeşil
# print(type(stringrenkler))

# # SPLİT -herhangi bir metni belirlediğimiz bir karaktere göre parçalara ayırmak için kullanılır
# stringrenkler="-".join(renkler )
# print(stringrenkler)
# # siyah-beyaz-sarı-mavi-yeşil
# renkler2=stringrenkler.split("-")
# print(renkler2)
# # ['siyah', 'beyaz', 'sarı', 'mavi', 'yeşil']
# print(type(renkler2))
# renkler3=stringrenkler.split("ma")
# print(renkler3)
# # ['siyah-beyaz-sarı-', 'vi-yeşil']

# # TUPLE - demetler
# # listelerden farkı değiştirilemezler
#  listelerde olan ekleme çıkarma gibi işlemler tuplelarda yoktur
# demet=("siyah","beyaz","sarı","mavi","yeşil")
# print(demet)
# print(type(demet))
# print(len(demet))
# print(demet[0])
# demetsayısı=demet.count("siyah")
# print(demetsayısı)
# demetındex=demet.index("sarı")
# print(demetındex)
# for i in demet:
#     print(i)
# print(demet[3])


# SET - kümeler 
# sırasızdır ve tekrarlayan elemanları yoktur
# kume={"siyah","beyaz","sarı","mavi","yeşil"}
# print(kume)
# print(type(kume))
# print(len(kume))
# for i in kume :
#     print(i)

# print ("siyah" in kume)  # True
# kume.add("mor")
# print(kume)
# kume.remove("sarı")
# print(kume)
# kume.add("beyaz") # beyaz zaten var olduğu için eklenmez
# print(kume)
# kume.remove("pembe") # pembe olmadığı için hata verir
# kume.discard("pembe") # pembe olmadığı için hata vermez

# kümelerin kesişimi, birleşimi ve farkı
# kume1={"siyah","beyaz","sarı","mavi","yeşil"}
# kume2={"siyah","beyaz","pembe","turuncu","mor"}
# print(kume1.intersection(kume2)) # kesişim
# print(kume1.union(kume2)) # birleşim
# print(kume1.difference(kume2)) # fark
# print(kume2.difference(kume1)) # fark
# print("sarı" in kume1.intersection(kume2)) # False

# boş liste, demet ve küme oluşturma
# bosliste1=[]
# bosliste2=list()
# print(bosliste1)
# print(len(bosliste2))

# bosdemet1=()
# bosdemet=tuple()
# print(bosdemet1)
# print(len(bosdemet))

# boskume2=set()
# print(boskume2)
# boskume1={}
# print(type(boskume1)) # dict

# SET FONKSİYONU
# python=set("PYTHON") #STRİNGİ KÜMEYE ÇEVİRİR
# print(python) #{'Y', 'O', 'P', 'T', 'N', 'H'} KÜMEYE ÇEVİRİR
# python=set([1,2,3,4,5]) #LİSTEYİ KÜMEYE ÇEVİRİR
# print(python) #{1, 2, 3, 4, 5} KÜMEYE ÇEVİRİR
# python=set((1,2,3,4,5)) #TUPLEYİ KÜMEYE ÇEVİRİR
# print(python) #{1, 2, 3, 4, 5}

# DİCTIONARY - SÖZLÜKLER
# sözlükler key-value (anahtar-değer) çiftlerinden oluşur
# kisi={"ad":"Ali","soyad":"Veli","yaş":30,"hobiler":["futbol","kitap okuma","yüzme"]}
# print(kisi)
# print(type(kisi))
# print(len(kisi))
# print(kisi["ad"])
# print(kisi["hobiler"])
# kisi["ad"]="Ahmet" # sözlükteki "ad" anahtarının değerini değiştirir
# print(kisi["ad"])
# kisi.update({"ad":"Mehmet","yaş": 50}) # sözlükteki "ad" ve "yaş" anahtarlarının değerlerini değiştirir
# print(kisi)

# DEL - sözlükten anahtar-değer çiftini siler
# kisi["id"]=12345 # sözlüğe yeni bir anahtar-değer çifti ekler
# print(kisi)
# del kisi["id"] # sözlükten "id" anahtarını ve değerini siler
# print(kisi)
# for x in kisi:
#     print(x) # anahtarları yazdırır
#     print(kisi[x]) # değerleri yazdırır
# print(kisi.keys()) # anahtarları yazdırır
# print(kisi.values()) # değerleri yazdırır
# print(kisi.items()) # anahtar-değer çiftlerini yazdırır
# for k in kisi.items():
#     print(k) # anahtar-değer çiftlerini yazdırır

# for x,y in kisi.items():
#     print(x,y) # anahtar ve değerleri ayrı ayrı yazdırır

# # print(kisi["id"]) # sözlükte "id" anahtarı olmadığı için hata verir
# print(kisi.get("id")) # sözlükte "id" anahtarı olmadığı için None döndürür
# print(kisi.get("ad"))
# print(kisi.get("ad","Anahtar bulunamadı")) # sözlükte "ad" anahtarı olduğu için değerini döndürür
# print(kisi.get("id","Anahtar bulunamadı")) # sözlükte "id" anahtarı olmadığı için "Anahtar bulunamadı" döndürür

# if - else
# if True:
#     print("kosul dogru")
#     print("hala kosuln ıcındeyım")

# a=5
# b=5
# if a==b:
#     print("a ve b eşittir") 

# a=6
# b=8
# if a==b:
#     print("a ve b eşittir")
# else:
#     print("a ve b eşit değildir")

# renk="siyah"
# if renk=="mavi":
#     print("renk mavidir")
# elif renk=="beyaz":
#     print("renk beyazdır")
# else:
#     print("renk mavi veya beyaz değildir")        

# OR - AND
# a =1
# b=4
# c=5
# if a==5 or b==5:
#     print("kosul dogru")
# else:
#     print("kosul yanlıs")
# a =1
# b=4
# c=5
# if a==1 and b==4:
#     print("kosul dogru")
# else:
#     print("kosul yanlıs")    

# IN
# liste1=[1,2,3,4,5]
# a=6
# if a in liste1:
#     print("a listede var")
# else:
#     print("a listede yok")

# NOT
# liste1=[1,2,3,4,5]
# a=6
# if a not in liste1:
#     print("a listede yok")

# IS hafızada da aynı yerde olması gerekir özdeş olmarı gerekir
# a="Phyton"
# b="Phyto"
# b+="n"
# if a is b:
#     print("a ve b özdeştir")
# else:
#     print("a ve b özdeş değildir")    ---a ve b özdeş değildir
#     print(id(a))
#     print(id(b))

# FOR DÖNGÜSÜ
# liste=[1,2,3,4,5,6]
# for rakam in liste:
#     print(rakam)

# isim="hacer"
# for harf in isim:
#     print(harf)

# demet=(1,2,3,4,5)
# for rakam in demet:
#     print(rakam)

# for i in range(3,10,2): # 3 den başla 10 a kadar 2 şer 2 şer git
#     print(i)
# liste1=["a","b","c","d","e"]
# liste2=[1,2,3,4,5]
# for i in range(len(liste1)):
#     print(liste1[i], liste2[i])

# liste=[1,2,3,4,5,6,7,8,9]
# for i in liste:
#     if i==3:
#         print("3 atlandı")
#         continue # continue ile 3 ü atlıyoruz ve döngüye devam ediyoruz
#         #break ile 3 ü atlıyoruz ve döngüden çıkıyoruz 
#     print(i)

# liste=range(100)
# for i in liste:
#     if(i==81):
#         break
#     if(i % 3 == 0):
#         print(i)
#     else:
#         continue    
        
# WHİLE DÖNGÜSÜ BELİRLİ BİR KOŞUL SAĞLANDIGINDA
# x=2
# while x<10:
#     print(x)
#     x+=1

# x=1
# while True:
#     print(x)
#     x+=2
#     if(x>1000):
#         break

# sayi = int(input("bir sayı gır:"))
# print("gırdıgınız sayı", sayi)
# result=1
# for i in range(1,sayi + 1):
#     result*=i

# print(f"{sayi}! = {result}")

# sayi2=int(input("sayı gır : "))
# res=1
# k=1
# while k<=sayi2:
#     res*=k
#     k+=1
# print(res)    

# sayi = int(input("Bir sayı giriniz: "))

# if sayi <= 1:
#     print("Asal sayı değildir")
# elif sayi == 2:
#     print("2 sayısı asaldır")
# else:
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             print("Asal sayı değildir")
#             break
#     else:
#         # Bu 'else', for döngüsü hiç 'break' komutuna uğramadan 
#         # başarılı bir şekilde biterse çalışır.
#         print("Asal sayı")

# sayi = int(input("Bir sayı giriniz: "))
# str_sayi=str(sayi)
# toplam=0
# for i in str_sayi:
#     toplam+=int(i)

# print(f"{sayi} sayısının rakammları toplamı {toplam} dır")

# list=[];

# for i in range(1,6):
#     sayılar=int(input("bir sayı giriniz:"))
#     list.append(sayılar)
# print(list)
# list.sort()
# print(list)
# print(f"en küçük sayı {list[0]},en büyük sayı {list[4]}")



# x=int(input("bir sayı giriniz:"))
# for i in range(0,x+1):
#     if i**2==x:
#         print(f"{x} sayısının karekökü {i} dır")
#         break
#     else:
#         continue

# x=int(input("bir sayı giriniz:"))   
# karekok=x**0.5
# if karekok==int(karekok):
#     print("tamkare")
# else:
#     print("tamkare değil")    

# metin=input("bir metin giriniz:")
# sozluk=dict()
# for i in metin:
#     if i  in sozluk:
#         sozluk[i]+=1
#     else:
#         sozluk[i]=1
# for harf,adet in sozluk.items():
#     print(f"{harf} harfi {adet} kez geçiyor")        

# metin=input("bir metin giriniz:")
# liste=[]
# for i in metin:
#     if i == "a" :
#         liste.append("A")
#     else:
#         liste.append(i)    

# print("".join(liste))
# kactane = 0
# liste=[]
# for i in range(3, 10001):
#     varmı = True
#     y = 2
#     while y < i:
#         if i % y == 0:
#             varmı = False
#             break 
#         else:
#             y+=1
#             continue   
        
#     if varmı == True:
#         ıstenılenler=str(i)
#         if ıstenılenler[0]=="3" and ıstenılenler[len(ıstenılenler)-1]=="7":
#             kactane+=1
#             liste.append(ıstenılenler)

# print(kactane)
# print(liste)


# list1=[]

# for i in range(100,1000):
#     toplam=0
#     strsayı=str(i)
#     for y in range(3):
#         intsayı=int(strsayı[y])
#         toplam+=intsayı**3

#     if toplam==i:
#         list1.append(i)

# print(list1)

# list1=list()
# a=1
# b=1
# list1.append(a)
# list1.append(b)
# while True:
#     toplam= a+b
#     a=b
#     b=toplam
#     list1.append(toplam)
#     if len(list1)==10:
#         break

# print(list1)
# print(len(list1))

# fibo_list=[]
# fibo_list.append(1)
# fibo_list.append(1)
# index=2
# while True:
#     fibo_list.append(fibo_list[index-2]+ fibo_list[index-1])
    
#     say=str(fibo_list[index])
#     if len(say) == 1000:
#         print(say)
#         print(index)
#         break
#     index+=1

# FONKSIYONLAR
# def topla(x,y):
#     print(x+y)

# topla(3,9)    

# def topla(x,y=6):
#     print(x+y)

# topla(3)
# eğer ben dger yazmazsam y 
# ıcın varsayılan olarak yazdıgım 6 kabul edılır

# def topla(x,y=6):
#      return x+y

# print(topla(3))

# def buyuk_harfe_cevir(metin):
#     return metin.upper()

# fonk=buyuk_harfe_cevir
# sonuc=fonk("hacer")
# print(sonuc)
#

# MODULLER hazır olan fonksıyonları kullanmak ıcın 
# import math
# sonuc=math.sqrt(625)
# print(sonuc)

# math modulunden sadece faktöriyel ıcın bukullanılır
# from math import factorial
# sonuc=factorial(5)
# print(sonuc)

# from math import* 
# bu sekılde math degıl ama math ıc ıcındekı
#  tum fonksıyonlar kullanılabılır
