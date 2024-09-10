# KLASS VA OBYEKT

class Kompyuter:
    def __init__(self, model, ram, sdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.sdd = sdd
        self.gpu = gpu
        self.cpu = cpu

    def info(self):
        inf = (f"Model: {self.model}, RAM: {self.ram}, SDD: {self.sdd}, GPU: {self.gpu}, CPU: {self.cpu}")
        return inf

myLoptop = Kompyuter('HP', '8GB', '256GB', 'INTEL', 'i5 12Gen')
print(myLoptop.info())

#O'zgartirildi
