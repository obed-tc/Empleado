class Operario:
    def __init__(self,nombre,ci,codigo,nit,direccion,mail,celular):
        self.__Nombre=nombre
        self.__Ci=ci
        self.__codigo=codigo
        self.__NIT=nit
        self.__Direccion=direccion
        self.__mail=mail
        self.__Celular=celular
    def getNombre(self):
        return self.__Nombre
    def getCi(self):
        return self.__Ci
    def getNIT(self):
        return self.__NIT
    def getCodigo(self):
        return self.__codigo
    def getDireccion(self):
        return self.__Direccion
    def getmail(self):
        return self.__mail
    def getCelular(self):
        return self.__Celular

    def setNombre(self,nombre):
        self.__Nombre=nombre
    def setCi(self,ci):
        self.__Ci=ci
    def setNIT(self,nit):
        self.__NIT=nit
    def setCodigo(self,codigo):
        self.__codigo=codigo
    def setDireccion(self,direccion):
        self.__Direccion=direccion
    def setmail(self,mail):
        self.__mail=mail
    def setCelular(self,celular):
        self.__Celular=celular
    
