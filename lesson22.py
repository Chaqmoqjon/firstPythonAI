# 22-DARS. MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)
#1
def summa(x, y, *sonlar): #hohlagancha sonlar qo'shish mumkin (tuple() qaytaradi)
    return x+y+sum(sonlar)

print(summa(1,2))
print(summa(1,2,4,5,6,7))
# print(summa(2)) #ikkita o'zgaruvchiga yetadigan qiymat berish majburiy (x va y uchun)
#2
def avto_info(kompaniya, model, **malumotlar):#hohlagancha sonlar qo'shish mumkin (lug'at() qaytaradi)
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("GM", "Malibu", rang = "qora", yil = 2018)
avto2 = avto_info("Tesla", "Model X", rang = "oq", yil = 2024, narx = 50_000)
#============Vazifalar============
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def summa(*sonlar): #hohlagancha sonlar qo'shish mumkin (tuple() qaytaradi)
    qiymat = 1
    for son in sonlar:
        qiymat *= son
    return qiymat
print(summa(4,5,6))
# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')