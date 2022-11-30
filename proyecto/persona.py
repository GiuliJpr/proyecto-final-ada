import requests
import json
import datetime


from cuenta import Cuenta


#Clima

url = "https://api.openweathermap.org/data/2.5/weather"
querystring = {"lat":"-31.417","lon":"-64.183","appid":"25f674984b4ff7636dca3b6d8f2be561","units":"metric","lang":"38"}
headers = {
    'Cache-Control': 'no-cache'
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
data = json.loads(response.content)

def dar_fecha():
    fecha = str(datetime.datetime.now())

    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    return f"Hoy es {dia} de {dar_mes()} de {anio}"


def dar_mes():
        fecha_mes = str((datetime.datetime.now()))
        if fecha_mes[5:7]=="01":
            return "Enero"
        if fecha_mes[5:7]=="02":
            return "Febrero"
        if fecha_mes[5:7]=="03":
            return "Marzo"
        if fecha_mes[5:7]=="04":
            return "Abril"
        if fecha_mes[5:7]=="05":
            return "Mayo"
        if fecha_mes[5:7]=="06":
            return "Junio"
        if fecha_mes[5:7]=="07":
            return "Julio"
        if fecha_mes[5:7]=="08":
            return "Agosto"
        if fecha_mes[5:7]=="09":
            return "Septiembre"
        if fecha_mes[5:7]=="10":
            return "Octubre"
        if fecha_mes[5:7]=="11":
            return "Noviembre"
        if fecha_mes[5:7]=="12":
            return "Diciembre"
            
def convertir_fecha(string_fecha):
    #que pasa si la fecha no tiene los 10 caracteres esperados?
    fecha_no_valida = True
    
    while fecha_no_valida:
        if len(string_fecha)!=10:
            string_fecha = input()
        else:
            fecha_no_valida = False

    anio = string_fecha[0:4]
    mes = string_fecha[5:7]
    dia = string_fecha[8:10]
    return datetime.date(int(anio), int(mes), int(dia))


class Persona(object):
    def __init__(self, dni, nombre, str_fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    def crear_cuenta(self):
        #Segun la edad, debería crear Cuenta o CuentaJoven()
        cuenta = Cuenta()
        cuenta.crear_movimiento(" | Cuenta creada. Se le otorgaron de bienvenida $", 1500)
        self.cuentas.append(cuenta)

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos
    
    
        
    def saludo(self):
        #Saludo que indique hora, fecha y clima
        fecha = dar_fecha()
        mes = dar_mes()
        return f"Hola, {self.nombre}. {fecha} y la temperatura es de {data['main']['temp']}°C."