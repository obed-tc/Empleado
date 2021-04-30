class Directivo():
	def __init__(self,usuario="admin",contraseña="admin",nombre="",apellido="",telefono=0,ci=0,email=""):
		self.__Usuario=usuario
		self.__Contraseña=contraseña
		self.__Nombre=nombre
		self.__Apellido=apellido
		self.__Telefono=telefono
		self.__Ci=ci
		self.__Email=email
	def getUsuario(self):
		return self.__Usuario
	def getContraseña(self):
		return self.__Contraseña
	def getNombre(self):
		return self.__Nombre
	def getApellido(self):
		return self.__Apellido
	def getTelefono(self):
		return self.__Telefono
	def getCi(self):
		return self.__Ci
	def getEmail(self):
		return self.__Email
	
	def setUsuario(self):
		self.__Usuario=usuario
	def setContraseña(self):
		self.__Contraseña=contraseña
	def setNombre(self):
		self.__Nombre=nombre
	def setApellido(self):
		self.__Apellido=apellido
	def setTelefono(self):
		self.__Telefono=telefono
	def setCi(self):
		self.__Ci=ci
	def setEmail(self):
		self.__Email=email