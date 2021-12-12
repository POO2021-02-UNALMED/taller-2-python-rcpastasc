class Asiento:
	def __init__(self, color, precio, registro):
		self.color = color
		self.precio = precio
		self.registro = registro

	def cambiarColor(self, color):
		if(color in ["rojo","verde","amarillo","negro","blanco"]):
			self.color = color
class Auto:
	cantidadCreados = 0
	def __init__(self, modelo, precio, asientos, marca, motor,registro):
		self.modelo = modelo
		self.precio = precio
		self.asientos = asientos
		self.marca = marca
		self.motor = motor
		self.registro = registro
		
	def cantidadAsientos(self):
		i=0
		for asiento in self.asientos:
			if asiento != None:
				i+=1
		return 

	def verificarIntegridad(self):
		cadena = "Auto original"
		for i in range(0, len(self.asientos)):
			if(self.asientos[i] !=None):
				if (self.registro != self.asientos[i].registro or self.registro != self.motor.registro or self.asientos[i].registro != self.motor.registro):
					cadena = "Las piezas no son originales"
			else:
				pass

		return cadena

class Motor:
	def __init__(self, numero, tipo, registro):
		self.numero = numero
		self.tipo = tipo
		self.registro = registro
	
	def cambiarRegistro(self, registro):
		self.registro = registro
	def asignarTipo(self, tipo):
		if(tipo in ["electrico", "gasolina"]):
			self.tipo = tipo




	


		
