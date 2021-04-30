from Empleado import Empleado
import os
from colorama import Fore
from colorama import init
init()
class GestionEmpleado():
	
	opcion=1
	listaEmpleado=[]
	#MENU
	def menu(self):
	    os.system("cls")
	    print(Fore.RED+"""


███████╗███╗░░░███╗██████╗░██╗░░░░░███████╗░█████╗░██████╗░░█████╗░
██╔════╝████╗░████║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░██╔████╔██║██████╔╝██║░░░░░█████╗░░███████║██║░░██║██║░░██║
██╔══╝░░██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░██╔══██║██║░░██║██║░░██║
███████╗██║░╚═╝░██║██║░░░░░███████╗███████╗██║░░██║██████╔╝╚█████╔╝
╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░

         """+Fore.GREEN+"    Create by: Jesus,Obed,Josias"+Fore.WHITE+"""

	    1.Registrar
	    2.Eliminar
	    3.Editar
	    4.Listar
	    0.Salir

	    """)
	#OPCION REGISTRAR A LOS CLIENTES
	def Registrar(self,listaEmpleado):
	    os.system("cls")
	    print("REGISTRO: \n")
	    nombre=input("Ingrese su nombre: \n------» ")
	    ci=int(input("Ingrese su Cedula de Identidad:\n------» "))
	    codigo=input("Ingrese su codigo: \n------» ")
	    nit=int(input("Ingrese su NIT: \n------» "))
	    direccion=input("Ingrese su Direccion: \n------» ")
	    mail=input("Ingrese su Correo electronio:\n------» ")
	    celular=int(input("Ingrese su numero de Celular:\n------» "))
	    
	    print("EMPLEADO REGISTRADO")
	    input("")
	    empleado=Empleado(nombre,ci,codigo,nit,direccion,mail,celular)
	    self.listaEmpleado.append(empleado)
	
	#OPCION LISTAR LOS CLIENTES REGISTRADOS 
	def ListarEmpleado(self,listaempleado):
	    os.system("cls")
	    for i in range(len(listaempleado)):
	        print("============================")
	        print("EMPLEADO N° ",(i+1))
	        print("Nombre= ",listaempleado[i].getNombre())
	        print("Ci= ",listaempleado[i].getCi())
	        print("Codigo= ",listaempleado[i].getCodigo())
	        print("NIT=",listaempleado[i].getNIT())
	        print("Direccion=",listaempleado[i].getDireccion())
	        print("Mail=",listaempleado[i].getmail())
	        print("Celular=",listaempleado[i].getCelular())
	        print("============================")
	    input()
	#MENU DE ELIMINAR
	def menuEliminarEmpleado(self):
	    print("1.Eliminar por # Cliente")
	    print("2.Eliminar por codigo")
	    print("3.Eliminar por CI")
	    print("0.Cancelar")
	  
	#MENU ELIMINAR POR CODIGO
	def eliminarCodigo(self,codigo,listaempleado):
	    for i in range(len(listaempleado)):
	        if codigo==listaempleado[i].getCodigo():
	            del listaempleado[i]
	#MENU ELINMINAR POR CI
	def eliminarCi(self,ci,listaempleado):
	    for i in range(len(listaempleado)):
	        if ci==listaempleado[i].getCi():
	            del listaempleado[i]
	#OPCION ELIMINAR CLIENTE
	def EliminarEmpleado(self,listaempleado):
	    os.system("cls")
	    self.ListarEmpleado(listaempleado)
	    self.menuEliminarEmpleado()
	    opcion=int(input(">>  "))
	    if opcion==1:
	        numeroEmpleado=int(input("Ingrese el numero del empleado: "))
	        del listaempleado[numeroEmpleado-1]
	    elif opcion==2:
	        codigoEliminar=input("Ingrese el codigo del empleado: ")
	        self.eliminarCodigo(codigoEliminar,listaempleado)
	    elif opcion==3:
	        ciEliminar=int(input("Ingrese ci:"))
	        self.eliminarCi(ciEliminar,listaempleado)
	    else:
	        print("Eliminicion cancelada")


	#OPCION ACTUALIZAR CLIENTES
	def ActualizarDatos(self,listaempleado):
		codigo=input("Codigo empleado: ")
		for i in listaempleado:
			if i.getCodigo()==codigo:
				nombre=input("Nombre: ")
				ci=input("Cedula de Identidad:")
				nit=input("NIT: ")
				direccion=input("Direccion")
				mail=input("Correo electronico: ")
				celular=input("Celular: ")
			if nombre!=None:
				i.setNombre(nombre)
			if ci!=None:
				i.setCi(ci)
			if nit!=None:
				i.setNIT(nit)
			if direccion!=None:
				i.setDireccion(direccion)
			if mail!=None:
				i.setmail(mail)
			if celular!=None:
				i.setCelular(celular)
			print("DATOS ACTUALIZADOS")
			input()
			break
		print("	 Usuario no encontrado  :(")
		input()
	def EmpleadoInicio(self):	
		while self.opcion!=0:
			self.menu()
			opcion=(input(">>> "))
			while opcion.isdigit()==False:
				self.menu()
				print("Por favor, introduzca un valor numerico")
				opcion=(input(">>> "))
			if int(opcion)==1:
				self.Registrar(self.listaEmpleado)
			elif int(opcion)==2:
				self.EliminarEmpleado(self.listaEmpleado)
			elif int(opcion)==3:
				self.ActualizarDatos(self.listaEmpleado)
			elif int(opcion)==4:
				self.ListarEmpleado(self.listaEmpleado)

			elif int(opcion)==0:
				print("Sistema guardando datos...")
				break
			else:
				print("Opción Invalida!!!")
x=GestionEmpleado()
x.EmpleadoInicio()