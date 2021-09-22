# Clase_6_Actividad_ASincronica POO
# Ejercicio 10
# Integrantes del grupo: Fernanda Guillen / Mauricio / Danny / Merlin Arias
import operator
class Vuelo_En_El_Aire:
    # Formato={Id_Vuelo,Hora Salida, Hora LLegada, Ciudad Origen. Ciudad Destino, Id Avion}
    def __init__(self, Id_Vuelo="", Hora_Salida="", Hora_Llegada="", Aerop_Salida="", Aerop_Llegada="", Id_Avion=""):
        self.Id_Vuelo    = Id_Vuelo
        self.Hora_Salida = Hora_Salida
        self.Hora_Llegada = Hora_Llegada
        self.Aerop_Salida = Aerop_Salida
        self.Aerop_Llegada = Aerop_Llegada
        self.Id_Avion = Id_Avion

    def __str__(self):
        return f"Id Vuelo: {self.Id_Vuelo},Id Avión:{self.Id_Avion}"
class Aeropuertos:
    def __init__(self, Id_Aeropuerto="", Ubicacion=""):
        self.Id_Aeropuerto   = Id_Aeropuerto
        self.Ubicacion = Ubicacion
    def __str__(self):
        return f"Id Aeropuerto: {self.Id_Aeropuerto},Ubicación:{self.Ubicacion}"

class Aviones:
    def __init__(self, Id_Avion="", Tipo="", Capacidad=""):
        self.Id_Avion = Id_Avion
        self.Tipo = Tipo
        self.Capacidad = Capacidad
    def __str__(self):
        return f"Id Avion: {self.Id_Avion},Tipo:{self.Tipo}, Capacidad:{self.Capacidad}"

def Salida_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo, Hora_Salida, Hora_Llegada, Aerop_Salida, Aerop_Llegada, Id_Avion):

    Dic_Vuelos_En_El_Aire[Id_Vuelo]={"Id_Vuelo": Id_Vuelo,"Hora_Salida": Hora_Salida,"Hora_Llegada": Hora_Llegada,
                            "Aerop_Salida": Aerop_Salida,"Aerop_Llegada":Aerop_Llegada,"Id_Avion": Id_Avion}



def Llegada_De_Vuelo(Dic_Vuelos_En_El_Aire): # Elimina el vuelo del diccionario Dic_Vuelos_En_El_Aire
    Eliminar=input("Indique Vuelo a Eliminar: (XXX)")
    if Eliminar in Dic_Vuelos_En_El_Aire:
        del Dic_Vuelos_En_El_Aire[Eliminar]
        print(f"Vuelo {Eliminar} eliminado. presione cualquier tecla")
        input()
    else:
        print(f"Vuelo {Eliminar} no está en el aire !")
    input()
def Cant_Vuelos_En_El_Aire(Dic_Vuelos_En_El_Aire):
    print(f"Cantidad de Vuelos en el Aire: {len(Dic_Vuelos_En_El_Aire)}")
def Primer_Vuelo_En_Llegar(Dic_Vuelos_En_El_Aire): # Mostrar el aeropuerto al cual llega, tambien la demas informacion sobre ese vuelo. (Segun Dic Vuelo_En_El_Aire)

    Vuelo_Llegada=[]
    for clave, valor in Dic_Vuelos_En_El_Aire.items():
        Vuelo_Llegada.append(Dic_Vuelos_En_El_Aire[clave]["Hora_Llegada"]+"-"+clave)
    Vuelo_Llegada.sort()

    Id_Vuelo=Vuelo_Llegada[0][6:9]
    Id_Vuelo in Dic_Vuelos_En_El_Aire
    Aerop_Llegada = Dic_Vuelos_En_El_Aire[Id_Vuelo]["Aerop_Llegada"]
    Hora_Legada = Dic_Vuelos_En_El_Aire[Id_Vuelo]["Hora_Llegada"]
    Id_Avion = Dic_Vuelos_En_El_Aire[Id_Vuelo]["Id_Avion"]
    Hora_Salida = Dic_Vuelos_En_El_Aire[Id_Vuelo]["Hora_Salida"]
    Aerop_Salida = Dic_Vuelos_En_El_Aire[Id_Vuelo]["Aerop_Salida"]
    print(f"El más próximo en llegar es el vuelo {Id_Vuelo}, llegará al Aeropuerto {Aerop_Llegada} , a las {Hora_Legada} hrs.",end="")
    print(f" El avión es el {Id_Avion}, partió del Aeropuerto de {Aerop_Salida} a las {Hora_Salida}.")

def Vuelos_por_llegar_Segun_Aeropuerto(): # Para todos los aeropuerto vuelos por llegar y la hora de llegada.


    Vuelo_Llegada = []
    for clave, valor in Dic_Vuelos_En_El_Aire.items():
        Vuelo_Llegada.append(Dic_Vuelos_En_El_Aire[clave]["Hora_Llegada"] + "-" + clave)
    Vuelo_Llegada.sort()

    i=-1
    for vuelo in Vuelo_Llegada:
        i+=1
        id_Vuelo=(Vuelo_Llegada[i][6:9])
        if id_Vuelo in Dic_Vuelos_En_El_Aire:
            Aerop_Llegada = Dic_Vuelos_En_El_Aire[id_Vuelo]["Aerop_Llegada"]
            Hora_Legada   = Dic_Vuelos_En_El_Aire[id_Vuelo]["Hora_Llegada"]
            Id_Avion      = Dic_Vuelos_En_El_Aire[id_Vuelo]["Id_Avion"]
            Hora_Salida   = Dic_Vuelos_En_El_Aire[id_Vuelo]["Hora_Salida"]
            Aerop_Salida  = Dic_Vuelos_En_El_Aire[id_Vuelo]["Aerop_Salida"]
            print(f"Vuelo {id_Vuelo}, llegará al Aeropuerto {Aerop_Llegada} , a las {Hora_Legada} hrs.",
            end="")
            print(f" El avión es el {Id_Avion}, partió del Aeropuerto de {Aerop_Salida} a las {Hora_Salida}.")




# Agregar un vuelo en el diccionario Vuelo_En_El_Aire:
Dic_Vuelos_En_El_Aire={}
print("_"*120)
print("Proceso  # 1. Agregar vuelos:")
Salida_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo="001", Hora_Salida="15:00", Hora_Llegada="18:00", Aerop_Salida="Panamá", Aerop_Llegada="San José", Id_Avion="Airbus")
Salida_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo="002", Hora_Salida="16:00", Hora_Llegada="17:15", Aerop_Salida="San José", Aerop_Llegada="México", Id_Avion="737")
Salida_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo="003", Hora_Salida="17:00", Hora_Llegada="18:30", Aerop_Salida="México", Aerop_Llegada="Managua", Id_Avion="370")
Salida_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo="004", Hora_Salida="18:00", Hora_Llegada="19:45", Aerop_Salida="Managua", Aerop_Llegada="Panamá", Id_Avion="Concord")
print(Dic_Vuelos_En_El_Aire)
#Llegada_De_Vuelo(Dic_Vuelos_En_El_Aire,Id_Vuelo="001") # Elimina el vuelo del diccionario Vuelo_En_El_Aire
print("_"*120)
print("Proceso  # 2. Cantidad de vuelos en el aire:")
Cant_Vuelos_En_El_Aire(Dic_Vuelos_En_El_Aire)
print("_"*120)
print("Proceso  # 3. Elimina vuelo que ya llegó:")
Llegada_De_Vuelo(Dic_Vuelos_En_El_Aire)
print("_"*120)
print("Proceso  # 4. Consulta cuál será el primer vuelo en llegar:")
Primer_Vuelo_En_Llegar(Dic_Vuelos_En_El_Aire) # Mostrar el aeropuerto al cual llega, tambien la demas informacion sobre ese vuelo. (Segun Dic Vuelo_En_El_Aire)
print("_"*120)
print("Proceso  # 5. Imprime lista de vuelos según aeropuerto y orden de llegada:")
Vuelos_por_llegar_Segun_Aeropuerto() # Para todos los aeropuerto vuelos por llegar y la hora de llegada.


