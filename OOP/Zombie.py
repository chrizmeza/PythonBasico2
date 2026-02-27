from enemigo import *


class zombie(enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='zombie', puntos_energia=puntos_energia, ataque=ataque)


        def habla(self):
            print("hummm....*")


        def propagar_enfermedad(self):
            print("el zombie esta tratando de propagar la enfermedad!!")
