#Ejercicio 9
#
class Rectangulo:
    def perimetro(self,):
        self.largo = 1
        self.ancho = 1
        self.calcularPerimetro = (self.largo * 2) + (self.ancho * 2)

    def area(self):
        self.largo = 1
        self.ancho = 1
        self.calcularArea = self.largo * self.ancho

    @property
    def ingresar_datos(self):
        self.ingresarLargo = float(input('Ingrese el largo: '))
        self.ingresarAncho = float(input('Ingresar el ancho: '))
        print(f'El valor de largo es {self.ingresarLargo} y el ancho {self.ingresarAncho}')
        return {self.ingresarLargo, self.ingresarAncho}

    @ingresar_datos.setter
    def validar_largo(self, largo):
        largo1, largo2 = largo
        #self.ancho = ancho
        pass
        if 0.0 <= largo1 <= 20.0:

            if 0.0 <= largo2 <= 20.0:
                print('Valores Ok !')
                return(largo1,largo2)
            else:
                print(f'** ERROR ** {largo2} Valor de ancho fuera de rango 0.0 -> 20.0')
        else:
            print(f'** ERROR ** {largo1} Valor  de largo fuera de rango 0.0 -> 20.0')
        pass
    def es_cuadrado(self, largo1, largo2):
        self.largo = largo1
        self.ancho = largo2
        # self.ancho = ancho

        if self.largo == self.ancho:
            print('Cuadrado')
            return True

        else:
            print('Rectangulo')
            return False

llamandoClase = Rectangulo()
print("Ingreso de Datos (Largo,Ancho)")
largoYancho=list(llamandoClase.ingresar_datos)
largo=largoYancho[0]
if len(largoYancho) == 1:
    ancho=largo
else:
    ancho = largoYancho[1]
llamandoClase.validar_largo = (largo,ancho)
llamandoClase.es_cuadrado(largo,ancho)

