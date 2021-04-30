class Oficial:
	def __init__(self,nombre="admin",apellido="",ci=0,celular=0,contraseña="admin"):
		self.__Nombre=nombre
		self.__Apellido=apellido
		self.__Ci=ci
		self.__Celular=celular
		self.__Contraseña=contraseña
	def getNombre(self):
		return self.__Nombre
	def getApellido(self):	
		return self.__Apellido
	def getCi(self):
		return self.__Ci
	def getCelular(self):
		return self.__Celular
	def getContraseña(self):
		return self.__Contraseña

	def setNombre(self,nombre):
		self.__Nombre=nombre
	def setApellido(self,apellido):	
		self.__Apellido=apellido
	def setCi(self,ci):
		self.__Ci=ci
	def setCelular(self,celular):
		self.__Celular=celular
	def setContraseña(self,contraseña):
		self.__Contraseña=contraseña






