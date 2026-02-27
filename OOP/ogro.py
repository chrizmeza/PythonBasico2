from Enemigo import*
import random

class ogro(enemigo):
    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("ogro aplasta todo!!!")

    def ataque_especial(self):
        print("ogro ataque especial")
        funciona_ataque_especial= random.random() < 0.20
        if funciona_ataque_especial:
            self.ataque_especial += 4
            print("ogro enojado y increemento su ataque por 4")