#QIYMAT QAYTARUVCHI FUNKSIYA
# def toliq_ism(ism, familiya):
#     # Salom beruvchi funksiya
#     t_ism = f"Assalomu alaykum, hurmatli {ism.title()+ ' ' + familiya.title()}"
#     return t_ism

# talaba1 = toliq_ism('Islombek', 'Odiljonov')
# talaba2 = toliq_ism('Samandar', 'Odiljonov')
# talaba3 = toliq_ism('Ibrohim', 'Odiljonov')

# print(talaba2)
############
# def toliq_ism(ism, familiya, otasining_ismi = ''):
#     if toliq_ism:
#         t_ism = f"Assalomu alaykum, hurmatli {ism}  {familiya} {otasining_ismi}"
#     else:
#         t_ism = f"Assalomu alaykum, hurmatli {ism}  {familiya}"
#     return t_ism.title()

# talaba1 = toliq_ism('Samandar', 'Odiljonov')
# talaba2 = toliq_ism('Islombek', 'Odiljonov', 'Zafarjon ogli')
# print(talaba1)
###########
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi,
#     }
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 5_000)
# avtolar = [avto1, avto2]

# print(f'Online do\'kondagi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narhi']:
#         narhi = avto['narhi']
#     else:
#         narhi = "Noma'lum"

#     print(f"{avto['rangi']} {avto['model']}. Narhi: {narhi}")
#############
# def oraliq(min, max, qadam = 1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# ora = oraliq(9, 19)
# print(ora)
############
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi,
#     }
#     return avto

# avtolar = []

# print(f'Online do\'kondagi avtomashinalar shakllantirish: ')
# while True:
#     print(f"Quyidagi ma'lumotlarni kiriting: \n")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Model: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = int(input("Yili: "))
#     narhi = int(input("Narhi: "))

#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

#     javob = input("Yana avtomobil qo'shasizmi (yes/no): ")
#     if javob == 'no':
#         break
# print(f"Salonimizdagi avtomobillar: ")
# for avto in avtolar:
#     if avto['narhi']:
#         narhi = avto['narhi']
#     else:
#         narhi = "Noma'lum"

#     print(f"{avto['model']} {avto['rangi']}. Narhi: {narhi}")

# ===========Vazifalar================
# 1 va 2
# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
#3 Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max

kattasi(10,20,-5)
#4 Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
def aylana_info(radius,pi=3.14159):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*pi,
              "yuza":pi*radius**2}
    return aylana

aylana_info(5)
#5 Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
def tub_sonlar_top(min,max):
    tub_sonlar = []
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar

tub_sonlar_top(1,20)

#6 Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))