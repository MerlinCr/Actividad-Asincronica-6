# Ejercicio Numero 8
# Curso Python Basico
class Reloj():
    Hora="00"
    Minutos = "00"
    Segundos = "00"

    def Cambiar_Hora(self):  # Metodo
        Reloj.Hora=input(f"Cambiar Hora: ({Reloj.Hora}) ")
    def Cambiar_Minutos(self):  # Metodo
        Reloj.Minutos=input(f"Cambiar Minutos: ({Reloj.Minutos}) ")
    def Cambiar_Segundos(self):  # Metodo
        Reloj.Segundos=input(f"Cambiar Segundos: ({Reloj.Segundos}) ")

    def Ver_Hora(self):  # Metodo
        print(f"La Hora es: ({Reloj.Hora})")
    def Ver_Minutos(self):  # Metodo
        print(f"Los Minutos son: ({Reloj.Minutos})")
    def Ver_Segundos(self):  # Metodo
        print(f"Los Segundos son: ({Reloj.Segundos}) ")
    def Ver_Tiempo(self):
        print(f"La Hora HH:MM:SS es {Reloj.Hora+':'+Reloj.Minutos+':'+Reloj.Segundos}.")
Mi_Hora=Reloj()
print("Cambiar Hora:")
Mi_Hora.Cambiar_Hora()
print("Cambiar Minutos:")
Mi_Hora.Cambiar_Minutos()
print("Cambiar Segundos:")
Mi_Hora.Cambiar_Segundos()
print("Ver Hora:")
Mi_Hora.Ver_Hora()
print("Ver Minutos:")
Mi_Hora.Ver_Minutos()
print("Ver Segundos:")
Mi_Hora.Ver_Segundos()
print("Ver Tiempo (HH:MM:SS")
Mi_Hora.Ver_Tiempo()

