from INTERFACES.modelos.usuario import Usuario
from INTERFACES.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

# Clase storemanager
# NO TIENE VARIABLES !!!

class ManejoDeInscripciones:
    #
    # Decorador 'static method'
    # El objeto solo tiene la funcion inscribirUsuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones contiene la interfaz intercambiable
    #
    @staticmethod
    
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("-----> Guardando usuario...\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
