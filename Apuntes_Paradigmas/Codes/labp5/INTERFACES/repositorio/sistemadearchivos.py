from INTERFACES.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from INTERFACES.modelos.usuario import Usuario

# Implementa la interfaz RepositorioDeUsuarios

class SistemaDeArchivos(RepositorioDeUsuarios):
    __directorio: str

    def __init__(mi, directorio: str):
        mi.__directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi, usuario: Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lasName></age>{usuario.getEdad()}</age></root>"

        print(f"Guardando usuario en el archivo: {mi.__directorio}/{usuario.getNombre()}")
        print(xml)

    def cerrar(mi) -> None:
        print("Cerrando el archivo")

