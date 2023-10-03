class Alumno:
    def __init__(self, nombre, edad, numero_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.numero_estudiante = numero_estudiante

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y mi número de estudiante es {self.numero_estudiante}.")

# Crear una instancia de la clase "Alumno"
alumno1 = Alumno("Emilio", 21, "L20230236")

# Acceder a los atributos y métodos de la instancia
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.numero_estudiante)
alumno1.presentarse()

# Clases y objetos

class Alumnos:
    def __unit__(self,numControl, nombre, edad):
        self.numControl = numControl
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"({self.numControl}: {self.nombre}, edad: {self.edad})"

#Creando el objeto.
AlumnosX = Alumnos
print(AlumnosX.nombre)