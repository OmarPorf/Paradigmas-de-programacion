#==============================================================
# Del directorio "INTERFACES", el subdirectorio "repositorio",
# el archivo "basededatos.py" importar el objeto BaseDeDatos
#==============================================================
from INTERFACES.repositorio.basededatos import BaseDeDatos

from INTERFACES.repositorio.s3 import S3

from INTERFACES.repositorio.sistemadearchivos import SistemaDeArchivos

from INTERFACES.modelos.usuario import Usuario

from INTERFACES.negocios.manejodeinscripciones import ManejoDeInscripciones

#=========================
# Crear el objeto Usuario
#=========================

usuario = Usuario("Roberto","Jimenez", 18)

# Crear el objeto s3

repositorioS3 = S3("321221321", "sdf324223", "MiCubeta")

# Interfaz inscribirUsuario del objeto ManejoDeInscripciones

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioS3)
print("\n")

# Crear el objeto sistemadearchivos

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

# Interfaz inscribirUsuario del objeto ManejoDeInscripciones

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioSistemaDeArchivos)
print("\n")

# Crear objeto basededatos

repositorioBaseDeDatos = BaseDeDatos("localhost", "admin", "admin123")

# Interfaz inscribirUsuario del objeto ManejoDeInscripciones

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioBaseDeDatos)
print("\n")

