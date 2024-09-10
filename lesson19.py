# FUNKSIYA

def salom_ber(ism):
    # Salom beruvchi funksiya
    print(f"Assalomu alaykum, hurmatli {ism.title()}")

salom_ber('Islombek')
salom_ber('Samandar')

def toliq_ism(ism, familiya):
    # Salom beruvchi funksiya
    print(f"Assalomu alaykum, hurmatli {ism.title()+ ' ' + familiya.title()}")

toliq_ism('Islombek', 'Odiljonov')

def yosh_hisobla(ism, yili):
    # Yoshni hiosblovchi funksiya
    print(f"Assalomu alaykum, hurmatli {ism.title()}\n"
          f'Yoshi: {2024-yili} da')

# yosh_hisobla('Islombek', 2002)  # 1- misol
yosh_hisobla(ism = 'Islombek', yili = 2002) # 2- misol Kalitso'z uslubi

def yosh_hisobla2(tugilgan_yili, joriy_yil = 2024): # default qiymat berish
    print(f'Siz {joriy_yil - tugilgan_yili} yoshdasiz')

# # yosh_hisobla2(2004, 2020) # 16 yoshsiz
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla2(tyil) # 20 yoshsiz, default qiymatni oladi

# ==============Vazifalar===========
# 1
# def t_yil2 (ism, tyil):
#     print(f"{ism.title}ning yoshi {2024-tyil}")

# ism = input("Ismingizni kiriting: ")
# yil = int(input("Yilingizni kiriting: "))
# t_yil2(ism, yil)

# 2
# def sonkv (son):
#     print(f"{son} ning kvadrati: {son**2}\n"
#           f"{son} ning kubi: {son**3}")

# son = int(input("Sonni kiriting: "))
# sonkv(son)

# 3
# def sonkv (son):
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# son = int(input("Sonni kiriting: "))
# sonkv(son)

# 4
# def sonkv (son1, son2):
#     if son1 > son2:
#         print(f"{son1} katta")
#     elif (son2 > son1):
#         print(f"{son2} katta")
#     else:
#         print(f"{son1} va {son2} teng")

# son1 = int(input("Sonni kiriting: "))
# son2 = int(input("Sonni kiriting: "))
# sonkv(son1, son2)

# 5 va 6
# def sonkv (x, y = 2):
#     print(f"{x} va {y}")

# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
# sonkv(x, y)

# 7
def sonkv (son1):
    for n in range(2, 11):
        if not son1 % n: #qoldiq 0 ga teng bo'lganda oladi
            print(f"{son1} {n} ga qoldiqsiz bo'linadi")


son1 = int(input("Sonni kiriting: "))
sonkv(son1)