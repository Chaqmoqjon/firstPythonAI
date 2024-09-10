from avto_info_mod import avto_info as ainfo, info_print as iprint
# from avto_info_mod import *
import math
from math import pi
import random as r # random modulini r deb chaqirayapmiz

avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)

x=400
print(math.sqrt(x))

print(pow(5,5))

print(pi)

print(math.log2(8))
print(math.log10(100))

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))

x = list(range(11))
print(x)
r.shuffle(x)
print(x)