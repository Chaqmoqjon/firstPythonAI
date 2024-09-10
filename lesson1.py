# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:11:33 2023

@author: Chaqmoqjon
"""

print('Salom Dunyo')
print('Assalomu alaykum. Men "Dell" markasidagi noutbuk sotib oldim')
print('''Har kimki va\'fo qilsa, va\'fo topg\'usidir,
Har kimki ja\'fo, qilsa ja\'fo topg\'usidir.''')
print('Har kimki va\'fo qilsa, va\'fo topg\'usidir, \nHar kimki ja\'fo, qilsa ja\'fo topg\'usidir.')
print(2+4*5)
print(19/5)
print(19//5)
print(2**4)
print(15 % 6)  # qoldiqni chiqaradi
print("To'qqizning kvadrati", 9**2, "ga teng")
print('3 * 3 =', 3*3, 'ga teng')

print('5 ning 4 - darajasi', 5**4, 'ga teng')
print('22 ni 4 ga bo\'lganda', 22 % 4, 'qoldiq qoladi')
print('Tomonlai 125 ga teng bo\'lgan kvadratni yuzi',
      125*125, 'ga peimetri', 125*4, 'ga teng')
print('Diametri 12 ga teng bo\'lgan doirani yuzi', 3.14*6**2, 'ga teng')
print('Katetlari 6 va 7 bo\'lgan to\'g\'ri burchakli uchburchakni gipotenuzasi',
      (6**2+7**2)**(1/2))

# =============================================================================
# ism = 'Sardorbek'
# yosh = 21
# print(ism)
# print(yosh)
# =============================================================================

ism = 'Sardorbek'
print(ism)
ism = 'Islombek'
print(ism)

radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)

kocha = 'Bog\'bon'
mahalla = 'Sog\'bon'
tuman = 'Bodomzor'
viloyat = 'Samarqand'
manzil = f'{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati'

print(manzil)
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

# =============================================================================
# manzil1 = input('Ko\'changiz nima? \n>>> ')
# manzil2 = input('Mahallangiz nima? \n>>> ')
# manzil3 = input('Tumaninigiz nima? \n>>> ')
# manzil4 = input('Viloyatingiz nima? \n>>> ')
# print(f'{manzil1} ko\'chasi, \n{manzil2} mahallasi, \n{manzil3} tumani, \n{manzil4} viloyati.')
#
# print(f'{manzil1} ko\'chasi, {manzil2} mahallasi, {manzil3} tumani, {manzil4} viloyati.')
#
#
# #Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha = input("Ko'changiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaningiz: ")
# viloyat = input("Viloyatingiz: ")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")
# =============================================================================

# lesson 6  5/28/2023

kvadrat_tmni = 20
kvadrat_yuzi = kvadrat_tmni ** 2
print(kvadrat_yuzi)

PI = 3.14159
radius2 = 10
diametr = radius2 * 2
print('Aylana uzunligi', PI*diametr, 'ga teng')

a = -20
b = 40
c = b/a
print(c)

a = 2
b = 3.0
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))

aholi_soni = 7_828_932_256
print('Yer yuzidagi aholi soni', aholi_soni, ' dan oshdi')

x, y, z = 3.3, 5, 'salom'


ism = 'Akmal'
yosh = 23
xabar = f'{ism} {yosh} da'
print(xabar)

ism = 'Jobir'
yosh = 36
xabar2 = ism + ' ' + str(yosh) + ' yoshda'
# xabar2 = f'{ism} {yosh} yoshda'
print(xabar2)
print(type(ism))
print(type(yosh))

# t_yil = int(input('Tug\'ilgan yilngizni kiriting >>> '))
# yoshing = 2023 - t_yil
# print('Sizning yoshingiz ', yoshing, ' da')

# kv_kub = input('Isatalgan sonni kiriting >>> ')
# print(f'{kv_kub} sonining kvadrati {int(kv_kub) ** 2} ga teng')
# print(f'{kv_kub} sonining kubi {int(kv_kub) ** 3} ga teng')

# yosh_nech = input('Yoshingizni kiriting >>> ')
# yil = 2023 - int(yosh_nech)
# print('Siz', yil, ' yilda tug\'ilgansiz')

# bir_son = input('Birinchi sonni kiriting >>> ')
# ikki_son = input('Ikkinchi sonni kiriting >>> ')
# print(f'{float(bir_son)} + {float(ikki_son)} = {float(bir_son) + float(ikki_son)}')
# print(f'{float(bir_son)} - {float(ikki_son)} = {float(bir_son) - float(ikki_son)}')
# print(f'{float(bir_son)} * {float(ikki_son)} = {float(bir_son) * float(ikki_son)}')
# print(f'{float(bir_son)} / {float(ikki_son)} = {float(bir_son) / float(ikki_son)}')

# Foydalanuvchidan ikki son kiritshini so'rab,
# kiritilgan sonlarning yig'indisi, ayirmasi,
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a}+{b}=", a+b)
# print(f"{a}-{b}=", a-b)
# print(f"{a}x{b}=", a*b)
# print(f"{a}/{b}=", a/b)

# lesson 7

mevalar = ['olma', 'anor', 'behi', 'uzum', 'anjir']
narxlar = [12_000, 15_000, 5_000, 14_000, 5_600]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []  # bo'sh list

# birinchi mevani olib harfini kattalashtirish
print('Birinchi meva: ', mevalar[0].upper())
print('Ikkinchi meva: ', mevalar[1].title())
print(narxlar[2] + narxlar[1])  # narxlarni bir-biriga qo'shish
print(mevalar[-1])  # oxiridan bitta oldingini olish

narxlar[3] = narxlar[3] + 3_100
print(narxlar)  # narxlarga narx qo'shish

mevalar.append('qulupnay')  # oxiriga yangi mahsulot qo'shish
print(mevalar)

ismlar.append('Jamshid')  # oxiriga yangi mahsulot qo'shish
ismlar.append('Shoxrux')  # oxiriga yangi mahsulot qo'shish
ismlar.append('Ulug\'bek')  # oxiriga yangi mahsulot qo'shish
ismlar.append('Samandar')  # oxiriga yangi mahsulot qo'shish
ismlar.insert(0, 'Behruz')  # xohlagan joyga yangi mahsulot qo'shish
print(ismlar)

del mevalar[0]  # index bo'yicha o'chirish

mevalar.remove('behi')  # nomiga ko'ra o'chirish !faqat bittasi o'chadi
print(mevalar)

bozorlik = ['un', 'yog\'', 'uzum', 'guruch', 'asal']
# mahsulotni sug'urib olish !index berilmasa oxirgisini oladi
mahsulot = bozorlik.pop(2)
print('Men', bozorlik, 'sotib oldim')
print('Men', mahsulot, 'olmadim')

# AMALIYOT
ismlar_dost = ['Abu Bakir Siddiq', 'Umar ibn Hattob',
               'Abdurahmaon ibn Avf', 'Abdulloh ibn Muborak']
print(ismlar_dost[0], 'halifa bo\'ldi')
print(f'{ismlar_dost[1]} amir ul-mo\'minin deb chaqirishar edi')
print('Dunyodagi eng boy sahoba ' + ismlar_dost[2] + ' edi')
print(f'{ismlar_dost[3]} boylikda va ilmda sahobalarga tenglasha olgan')

sonlar_harxil = [3.3, -4, 5, -3.4, 36]
qiymat = sonlar_harxil[2] + sonlar_harxil[3] + 3_2 + sonlar_harxil[-1]
del sonlar_harxil[0]
print(qiymat)

t_shaxslar = ['Muhammadali Eshonqulov', 'Temurbek Adhamov']
m_shaxslar = ['Imom Buxoriy', 'Al-Farg\'oniy']
tanish = t_shaxslar.pop(0)
tanish2 = m_shaxslar.pop(0)
print(f'Men {tanish}ni taniyman. {tanish2}ni ziyoratiga bordik')

friends = []
friends.append('Abdujalil')
friends.append('Shoxrux')
friends.append('Ulug\'bek')
friends.append('Salimboy')
friends.append('Jamshidbek')
friends.append('Sayyadjon')

friends.remove('Sayyadjon')
friends.remove('Shoxrux')
friends.remove('Salimboy')

friends.insert(2, 'Samandar')
friends.append('Islombek')
friends.insert(0, 'Ibrohim')


mehmonlar = [{friends.pop(1)}, {friends.pop(1)}]
mehmonlar.append('Abdurahmon')
print(mehmonlar)

mehmonlar2 = []
mehmonlar2.append(friends.pop(3))
mehmonlar2.append(friends.pop(-1))
mehmonlar2.append(friends.pop(0))
print("Kelgan mehmonlar: ", mehmonlar2)

print(friends)

# lesson8

cars = ['bmw', 'ferrari', 'ford', 'lambargini', 'tesla X', 'audi']
cars.sort()  # alibo tartibida joylash
print(cars)

cars.sort(reverse=True)  # alibo tartibiga teskari joylash
print(cars)

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# ro'yxatni o'zgartirmasdan chiqarish
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# ro'yxatni o'zgartirmasdan teskari chiqarish
print(sorted(mehmonlar, reverse=True))


ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()  # tartiblash
print(ages)
print(sorted(ages, reverse=True))  # teskari tartiblash

fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()  # teskari tartiblash
print(fruits)

fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# len(fruits) ro'yxat uzunligini qaytaradi
print("Elementlar soni:", len(fruits))


sonlar = list(range(0, 10))  # 0 dan 9 gacha qaytaradi
print(sonlar)

juft_sonlar = list(range(0, 20, 2))  # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1, 20, 2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)  # eng kichigini qaytaradi
qimmat = max(narhlar)  # eng kattasini qaytaradi
jami = sum(narhlar)  # jami qiymatni qaytaradi
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3]  # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars)

print(cars[:4])  # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:])  # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

sonlar = [1, 2, 3, 4, 5]  # sonlar degan ro'yxat yaratamiz
sonlar2 = sonlar  # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6)  # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7)  # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)

tomonlar = (20, 30, 55.2)  # o'zgarmas list
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])


toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')  # o'zgarmas ro'yxat
toys = list(toys)  # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
# Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
toys = tuple(toys)
print(toys)

# AMALIYOT

davlatlar = ['O\'zbekiston', 'Latviya', 'Estoniya',
             'Niderlandiya', 'Saudiya Arabistoni']
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
davlatlar.sort(reverse=True)
# sonlar3 = list(range(120,1201))
# sonlar3 = sum(sonlar3)
# print(sonlar3)
# eng_ki = min(sonlar3)
# eng_ka = max(sonlar3)
# print(eng_ka-eng_ki)
# elem_soni = len(sonlar3)
# print(sonlar3[:20])
# print(sonlar3[-20:])
# print(sonlar3[530:550])
taomlar = ['osh', 'sho\'rva', 'mastava', 'manti', 'chuchvara']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.append('olma')
nonushta.append('uzum')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)

# lesson9

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    # print('Assalomu alaykum. Mehmonimiz bo\'lmish', mehmon, 'aka.')
    # print('Sizni va oilangizni taklif qilamiz')
    # print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    # print("Hurmat bilan, Palonchiyevlar oilasi\n")
    print(mehmon)
print(mehmonlar)

sonlar = list(range(1, 11))
for son in sonlar:
    print(f'{son} ning kvadrati {son**2} ga teng')

sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

dostlar = []  # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
# dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# AMALIYOT

yangi_ismlar = ['Behruz', 'Bekzod', 'Humoyun', 'Alimardon', 'Jamshid', 'Oybek']
for yangi_ism in yangi_ismlar:
    print(f'{yangi_ism} sizni tabriklayman')
print(f'Kod {len(yangi_ismlar)} marta takrorlandi')

toq_sonlar2 = list(range(11, 35, 2))
for son_kub in toq_sonlar2:
    print(f'{son_kub} ning kubi {son_kub**3}')

# sev_kino = []
# for k in range(5):
#     sev_kino.append(input(f'{k+1}-kino nomini kiriting: '))
# print(sev_kino)

# Foydalanuvchidan bugun nechta odam bilan
# uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)


planetas = ['earth', 'yupiter', 'saturn', 'neutron', 'uran', 'mars']

for planeta in planetas:
    if planeta == "mars" or planeta == "earth":
        print(planeta.upper())
    else:
        print(planeta.title())

cars2 = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars2:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

# name2 = input('Ismingizni kiriting: ')
# if name2.lower() == 'admin':
#     print(f'Xush kelibsiz Admin!')
# else:
#     print(f'Xush kelibsiz {name2.title()}')

# son01 = int(input('Birinchi sonni kiriting: '))
# son02 = int(input('Ikkinchi sonni kiriting: '))

# if son01 == son02:
#     print(f'Sonlar bir-biriga teng!')
# else:
#     print(f'Sonlar bir-biriga teng emas!')

# if son01 > 0:
#     print(son01 ** (1/2) )
# else:
#     print(f'Musbat son kiriting!')
# print(son01 ** (1/2) ) if son01 > 0 else print(f'Musbat son kiriting!')

# ============Lesson 11===================

# juft_son01 = int(input(f'Juft son kiriting: '))
# if juft_son01 % 2 == 0:
#     print(f'Rahmat!')
# else:
#     print(f'Juft son kiriting!')

# muz_yosh = int(input(f'Yoshingizni kiriting: '))
# if muz_yosh > 60 or muz_yosh < 4:
#     price = "Bepul"
# elif muz_yosh < 18:
#     price = 10_000
# else:
#     price = 20_000

# print(f'Sizning xizmat narxingiz: {price}')

# tengkat1 = int(input(f'Birinchi sonni kiriting: '))
# tengkat2 = int(input(f'Ikkinchi sonni kiriting: '))
# if tengkat1 == tengkat2:
#     print("Bu sonlar  bir-biriga teng!")
# elif tengkat1 > tengkat2:
#     print(f'{tengkat1} katta')
# else:
#     print(f'{tengkat2} katta')

# mahsulotlar = ['olma','behi','anor','qulupnay','anjir', 'gilos', 'nok', 'ananas','banan', 'kakao']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f'{n+1}-mahsulotni kiriting: ' ))
# print(savat)

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f'Quyidagi mahsulotlar do\'konimizda yo\'q {mavjud_emas}')
# else:
#     print(f'Siz so\'raga barcha mahsulotlar do\'konimizda bor!')


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'{mahsulot} bizda bor')
#     else:
#         print(f'{mahsulot} bizda yo\'q')


# foydalanuvchilar = ['s', 't', 'k', 'l', 'o', 'p', 'a', 'q']

# new_log = input(f'Yangi login kiriting: ')

# if new_log in foydalanuvchilar:
#     print('Bu nom band!')
# else:
#     print(f'{new_log} xush kelibsiz')

# bolinma = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# n = int(input(f'Butun son kiriting: '))

# for newN in bolinma:
#     if n % newN == 0:
#         print(f'{n} soni {newN} ga qoldiqsiz bo\'linadi')

# ===========Lesson 14==================

dadam = {'ism': 'Zafarjon', 'yil': 1973, 'manzil': 'Namangan'}
abam = {'ism': 'Nafisaxon', 'yosh': 1980, 'manzil': 'Namangan'}
ukam = {'ism': 'Ibrohim', 'yosh': 2010, 'manzil': 'Namangan'}

print(
    f"Dadamning ismi {dadam['ism'].title()}, {dadam['yil']} - yilda, {dadam['manzil'].title()} viloyatida tug'ilgan")

sev_taom1 = {"ism": "sardorbek", "taom": "mastava"}
sev_taom2 = {"ism": "Islombek", "taom": "manti"}
sev_taom3 = {"ism": "Samandar", "taom": "osh"}
sev_taom4 = {"ism": "Inrohim", "taom": "lag'mon"}
sev_taom5 = {"ism": "Nomonjon", "taom": "chuchvara"}

sevT = sev_taom1["taom"].lower()
sevI = sev_taom1["ism"].title()

# print(f'{sevI}ning sevimli taomi {sevT}')
# print(
#     f'{sev_taom2["ism"].title()}ning sevimli taomi {sev_taom2["taom"].lower()}')
# print(
#     f'{sev_taom3["ism"].title()}ning sevimli taomi {sev_taom3["taom"].lower()}')

# izoh_log = {"int": "Faqat butun sonlarni qabul qiladi", "float": "Barcha sonlarni qabul qiladi",
#             "string": "Harfiy ifodalarni qabul qiladi", "if": "Shart bajarish operatori hisoblanadi"}
# kalit = input(f'Kalit so\'ozni kiriting: ').lower()
# print(izoh_log.get(kalit, "Bunday so'z mavjud emas!"))


# lugat = {"apple": "olma", "peach": "shaftoli",
#          "banana": "banan", "orange": "apelsin"}
# word = input(f'Ixtiyoriy so\'z kiritimg: ').lower()
# tarjima = lugat.get(word)
# if tarjima == None:
#      print("Bunday so'z mavjud emas!")
# else:
#     print(f"{word.title()} so'zi {tarjima} deb ataladi")

# ==================Lesson 15=================

paython_lug = {'items': 'Kalit va qiymatlarni chiqarish', 'keys': 'Faqat kalitlarni ekranga chiqarish', 'values': 'Faqat qiymatlarni ekranga chiqarish', 'set': 'Listdagi ma\'lumotlarni faqat bittadan chiqaradi',
               "int": "Faqat butun sonlarni qabul qiladi", "float": "Barcha sonlarni qabul qiladi", "string": "Harfiy ifodalarni qabul qiladi", "if": "Shart bajarish operatori hisoblanadi"}


for kalit1, qiymat1 in sorted(paython_lug.items()):
    print(f'{kalit1}() ning ma\'nosi {qiymat1} \n')

dav_poy = {"O'zbekiston": 'Toshkenti', 'rossiya': 'moskva', 'xitoy': 'pekin',
           'yaponiya': 'tokio', 'kanada': 'ottava', 'turkiya': 'istanbul', 'saudia arabiston': 'arriyad'}

for kalit2 in sorted(dav_poy.keys()):
    print(f'{kalit2.upper()} davlat \n')

for qiymat2 in sorted(dav_poy.values()):
    print(f'{qiymat2.title()} poytaxt\n')

# country = input('Istalgan davlat nomini kiriting: ').lower()
# capital = dav_poy.get(country)

# if capital == None:
#     print("Bunday ma'lumot yo'q")
# else:
#     print(f'{country.upper()}ning potaxti {capital}')


# res_menu = {'osh' : 20_000, 'mastava' : 10_000, 'manti' : 15_000,'lag\'mon' : 18_000, 'chuchvara' : 22_000}
# buy_taom = []

# print("3 xil taomni kiriting: ")
# for i in range(3):
#     buy_taom.append(input(f"{i+1} - taomni kiriting: "))

# for buyTaom in buy_taom:
#     if buyTaom in res_menu:
#         print(f'{buyTaom.title()} {res_menu[buyTaom]} so\'m')
#     else:
#         print(f"Bizda {buyTaom.title()} yo'q")


# ==================Lesson 16================
# Nesting
car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km': 50000,
    'korobka': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narh': 9000,
    'km': 89000,
    'korobka': 'mexanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2019,
    'narh': 15000,
    'km': 20000,
    'korobka': 'mexanika'
}

# Terminalga chiqarish
car = car0
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

# Terminalga chiqarish qisqasi
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

# Listdagi birinchi bo'limni ekranga chiqarish
print(cars[0])

# Kerakni ma'lumotni chiqarish
print(cars[0]['model'])

malibus = []  # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
        'model': 'malibu',
        'rang': None,  # rangi noaniq
        'yil': 2020,
        'narh': None,  # narhi belgilanmagan
        'km': 0,
        'korobka': 'avto'
    }
    malibus.append(new_car)  # yangi lug'atni ro'yxatga qo'shamiz

# Ro'yxatdagi 1 dan 3-gacha bo'lgan mashinalarga qizil rang berish
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

# Ro'yxatdagi 3 dan 6-gacha bo'lgan mashinalarga qizil rang berish
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

# Ro'yxatdagi 6 dan boshlab barcha mashinalarga qizil rang berish va narh belgilash
for malibu in malibus[6:]:
    malibu['korobka'] = 'mexanika'
    malibu['rang'] = 'qora'

# Ro'yxatdagi avto bo'lgan mashinalarga qizil rang berish va narh belgilash
for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000

for malibu in malibus:
    print(malibu)

# Lyg'at ichidagi ro'yxat
dasturchilar = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')

# Lug'at ichidagi lug'at
hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyil': 1995,
            'malumot': 'oliy',
            'tillar': ['python', 'c++']
            },
    'vali': {'familiya': 'aliyev',
             'tyil': 2001,
             'malumot': "o'rta-maxsus",
             'tillar': ['html', 'css', 'js']},
    'hasan': {'familiya': 'husanov',
              'tyil': 1999,
              'malumot': 'maxsus',
              'tillar': ['python', 'php']}
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())

# Vazifa
buxoriy = {"ism": "Imom al-Buxoriy",
           "tug_yil": 810,
           "tug_joyi": "Buxoro",
           "kasbi": "Muhaddislar imomi",
           "yoshi": 60,
           "mash_asar": ["Sahih al-Buxoriy", "Tarixi al-Kabir", "Al-Adhkar"]
           }
fargoniy = {"ism": "Ahmad al-Farg'oniy",
            "tug_yil": 797,
            "tug_joyi": "Farg'ona",
            "kasbi": "Astronoiya, matematika",
            "yoshi": 68,
            "mash_asar": ["Kitob al-Maknun", "Hidayat al-Muluk"]
            }
navoiy = {"ism": "Alisher Navoiy",
          "tug_yil": 1441,
          "tug_joyi": "Hirot",
          "kasbi": "So'z mulkining sultoni",
          "yoshi": 59,
          "mash_asar": ["Hayrat ul-Abror", "Saddi Iskandariy", "Farhod va Shirin"]
          }
temur = {"ism": "Amir Temur",
         "tug_yil": 1336,
         "tug_joyi": "Shahrisabz",
         "kasbi": "Temuriylar imperiyasi asoschisi",
         "yoshi": 68,
         "mash_asar": ["Temur tuzuklari", "Zafar-nama", "Risala-yi Abhariya"]
         }
bobur = {"ism": "Zahiriddin Muhamamd Bobur",
         "tug_yil": 1483,
         "tug_joyi": "Andijon",
         "kasbi": "Boburiylar sulolasi asoschisi",
         "yoshi": 47,
         "mash_asar": ["Buburnoma", "Mubayn-nama"]
         }
mash_shaxs = [buxoriy, fargoniy, navoiy, temur, bobur]

for shaxs in mash_shaxs:
    print(f"{shaxs['ism']}")
    print(f"{shaxs['tug_yil']} - yilda tug'ilgan")
    print(f"{shaxs['tug_joyi']}da tug'ilgan")
    print(f"{shaxs['kasbi']}")
    print(f"{shaxs['yoshi']} yil yashagan")

    for asar in shaxs["mash_asar"]:
        print(asar.upper(), end=' ')

# loveMovies = {
#     "Sobirjon" : [],
#     "Jo'rabek" : []
#     # "Alijon" : [],
#     # "Ulug'bek" : [],
#     # "Sayyadjon" : [],
# }

# for name, movie in loveMovies.items():
#     for n in range(3):
#         movi =  input(f"\n{name} ning {n+1} - yoqtirgan kinosi: ")
#         movie.append(movi)
# print(loveMovies)

# for name, movie in loveMovies.items():
#     print(f"\n{name} ning yoqtirgan kinolari: ", end=" ")
#     for movName in movie:
#         print(f"{movName}", end=" ")

davlatlar01 = {
    "O'zbekiston": {"hududi": 448.9,
                    "potaxti": "Toshkent",
                    "tili": "o'zbek",
                    "aholisi": 36},
    "Rossiya": {"hududi": 17_125.2,
                "potaxti": "Moskva",
                "tili": "rus",
                "aholisi": 146},
    "AQSH": {"hududi": 9_800.2,
             "potaxti": "Vashinton",
             "tili": "ingliz",
             "aholisi": 331},
    "Yaponiya": {"hududi": 377.9,
                 "potaxti": "Tokyo",
                 "tili": "japan",
                 "aholisi": 126},
    "Xitoy": {"hududi": 14_500.2,
              "potaxti": "Pekin",
              "tili": "xitoy",
              "aholisi": 1_400}
}

# for dav_name, dav_infos in davlatlar01.items():
#     print(f"{dav_name} davlati")
#     print(f"Maydoni: {dav_infos['hududi']} ming km.kv")
#     print(f"Poytaxti: {dav_infos['potaxti'].title()} viloyati")
#     print(f"Davlat tili: {dav_infos['tili']} tili")
#     print(f"Aholisi: {dav_infos['aholisi']} mln kishi")

# ix_dav = input(f"Ixtiyoriy davlartni kiriting: ")
# word = davlatlar01.get(ix_dav.title())

# if word == None:
#     print("Bunday davlat bizda mavjud emas!")
# else:
#     for dav_name, dav_infos in davlatlar01.items():
#         print(f"{dav_infos} davlati")
#         print(f"Maydoni: {dav_infos['hududi']} ming km.kv")
#         print(f"Poytaxti: {dav_infos['potaxti']} viloyati")
#         print(f"Davlat tili: {dav_infos['tili']} tili")
#         print(f"Aholisi: {dav_infos['aholisi']} mln kishi")

# if ix_dav.title() in davlatlar01:
#     dav_infos = davlatlar01[ix_dav.title()]
#     print(f"Maydoni: {dav_infos['hududi']} ming km.kv")
#     print(f"Poytaxti: {dav_infos['potaxti']} viloyati")
#     print(f"Davlat tili: {dav_infos['tili']} tili")
#     print(f"Aholisi: {dav_infos['aholisi']} mln kishi")
# else:
#     print("Bizda bunday davlar mavjud emas!")

# ==============Lesson 17================
# # 1
# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')

# 2
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

# 3
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# 4
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.

# 5
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# 6
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# 7
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# 8
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# 9
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# 10
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# ============Vazifa==========

# books = []
# while True:
#     book = input("Yoqtirgan kitoblaringizni kiritng: ")
#     if book != "stop":
#         books.append(book)
#     else:
#         break

summa = 0
# while True:
#     yosh3 = input("Yoshingizni kiritng: ")
#     if yosh3 != "stop" and yosh3 != "exit":
#         if int(yosh3) < 7:
#             print("Chiptaning narxi 2 000 so'm")
#             summa += 2_000
#         elif 7 <= int(yosh3) < 18:
#             print("Chiptaning narxi 3 000 so'm")
#             summa += 3_000
#         elif 18 <= int(yosh3) < 65:
#             print("Chiptaning narxi 10 000 so'm")
#             summa += 10_000
#         else:
#             print("Chiptaning narxi BEPUL")
#     else:
#         break

# print("Jami chiptalar narxi: ", summa)


# ishora1 = True
# while ishora1:
#     yosh3 = input("Yoshingizni kiritng: ")
#     if yosh3 != "stop" and yosh3 != "exit":
#         if int(yosh3) < 7:
#             print("Chiptaning narxi 2 000 so'm")
#             summa += 2_000
#         elif 7 <= int(yosh3) < 18:
#             print("Chiptaning narxi 3 000 so'm")
#             summa += 3_000
#         elif 18 <= int(yosh3) < 65:
#             print("Chiptaning narxi 10 000 so'm")
#             summa += 10_000
#         else:
#             print("Chiptaning narxi BEPUL")
#     else:
#         ishora1 = False

# print("Jami chiptalar narxi: ", summa, " so'm")

# yosh3 = input("Yoshingizni kiritng: ")
# while yosh3 != "stop" and yosh3 != "exit":
#     if int(yosh3) < 7:
#         print("Chiptaning narxi 2 000 so'm")
#         summa += 2_000
#     elif 7 <= int(yosh3) < 18:
#         print("Chiptaning narxi 3 000 so'm")
#         summa += 3_000
#     elif 18 <= int(yosh3) < 65:
#         print("Chiptaning narxi 10 000 so'm")
#         summa += 10_000
#     else:
#         print("Chiptaning narxi BEPUL")
#     yosh3 = input("Yoshingizni kiritng: ")

# print("Jami chiptalar narxi: ", summa)

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# ==============Lesson 18================

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())




# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")




# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)



# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     baholangan_talabalar[talaba] = baho
#     print(f"{talaba.title()} baholandi")

# =======Vazifa==========

# buyurtmalar = []

# while True:
#     savol = f"Nimani istaysiz: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     sorash = input(f"Yana nimadur istaysizmi? ha/yoq: ")
#     if sorash == "yoq":
#         break
# print(buyurtmalar)



# bozor = {}
# ishora = True
# while ishora:
#     maxsulot = input(f"Maxsulotni kiriting: ")
#     narx = input(f"Maxsulotni narxini kiriting: ")
#     bozor[maxsulot] = int(narx)
#     sorash = input(f"Yana nimadur kiritasizmi? ha/yoq: ")
#     if sorash == "yoq":
#         ishora = False
# print(bozor)




bozor = {"olma": 34, "behi": 30, "uzum": 28}
# ishora = True
# while ishora:
#     maxsulot = input(f"Maxsulotni kiriting: ")
#     narx = input(f"Maxsulotni narxini kiriting: ")
#     bozor[maxsulot] = int(narx)
#     sorash = input(f"Yana nimadur kiritasizmi? ha/yoq: ")
#     if sorash == "yoq":
#         ishora = False
# print(bozor)

buyurtmalar = ["olma", "behi", "olcha"]

# while True:
#     savol = f"Nimani istaysiz: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     sorash = input(f"Yana nimadur istaysizmi? ha/yoq: ")
#     if sorash == "yoq":
#         break
# print(buyurtmalar)

# while buyurtmalar in bozor.items():
#     print(bozor.values())

# ==============Lesson 19================
