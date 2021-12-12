class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if (color == colores[0] or color == colores[1] or color == colores[2] or color == colores[3] or color == colores[4]): 
            self.color = color    
            
            
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.registro = registro
        self.motor = motor
        
    def cantidadAsientos(self):
        numero_asientos = 0
        
        for i in range(0, len(self.asientos)):
            if isinstance(self.asientos[i], Asiento):
                numero_asientos += 1
                
        return numero_asientos
    
    def verificarIntegridad(self):
        cadena = "Auto original"
        
        for i in range(0, len(self.asientos)):
            if (self.asientos[i] != None):
                if (self.registro != self.asientos[i].registro or self.registro != self.motor.registro or self.asientos[i].registro != self.motor.registro):
                    cadena =  "Las piezas no son originales"          
            else:
                pass
 
        return cadena
    

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo
