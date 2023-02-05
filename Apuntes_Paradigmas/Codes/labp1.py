# ===================
# Operaciones basicas
# ==================
print(2 + 3)
print(2 * 3)
print(2 / 3)
print(2 ** 10)
print(2 ** 0.5)  # raiz cuadrada
print(10 % 2)
print(10 % 0.1)  # exclusivo en python

# ==========================================
# Para saber el tipo de objeto se usa type
# ==========================================

t = 0
print(type(t))  # entero
t = 3.6
print(type(t))  # real (flotante)
t = True
print(type(t))  # booleano (bool)

# =====================
# Mensajes a pantalla
# =====================
print("Este es un comando en python. ", "Este es otro enunciado. ", t)
print('id: ', 1)
print('First Name: ', 'Steve')
print('Last Name: ', 'Jobs')
print("vamos a sumar esto" + " con esto otro")

# ===============================================
# Continuar una instruccion en varios renglones
# ===============================================
if 100 > 99 and \
        200 <= 300 and \
        True != False:
    print('Hello World!')

# =======================================
# Comandos diferentes en la misma linea
# =======================================
print("Hola ");
print("tu!!")  # Se considera mala practica

# ================================================
# Usando parentesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
# ================================================
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(list)
print(matriz)

# ==================================================================
# Identacion estricta para procesos dependientes de : (dos puntos)
# ==================================================================
if 10 > 5:
    print("diez es mayor que cinco")
    print("otra identacion")
for i in list:
    print(i)
    print("ok")
if 10 > 5:
    print("verdadero")
    if 10 < 20:
        print("verdadero")
elif 5 > 3:  # comienza segundo condicional
    print("esto no se imprimira")
else:
    print("aqui nunca llega")


# ===========
# Funciones
# ===========

def say_hello(name):
    print("Hello ", name)
    print("Welcome to Python Tutorials")


say_hello("Omar")

# ==================================================
# Input permite obtener datos del usuario en promper
# ==================================================
nombre = input("Dame tu nombre: ")
print("Hola como estas", nombre)

# ========================================
# Los enteros son de precision ilimitada
# ========================================
y = 5000000000000000000000000000000000
print(y)

# =============================================================
# Se pueden delimitar numeros con guion bajo pero no con coma
# =============================================================
y = 5_000_000
print(y)

# ====================================================
# La funcion int() cambia strings y floats a enteros
# ====================================================
# 1.2 x 10^(-9)
# ===============
y = 1.2E-09
print(y)

# =========================================================
# La funcion float() convierte strings y enteros a floats
# =========================================================
y = float("14.3")

# ====================================================
# Los complejos se escriben con la raiz de menos uno
# j siempre con un numero como prefijo
# no acepta la j suelta
# ====================================================
z = 1 + 1j

# suma +
# resta -
# multiplicacion *
# division /
# modulo %
# exponente **
# // funcion piso
# Funciones para transformar numeros int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159, 4))

# ==========================
# Strings de varias lineas
# ==========================
parrafo = """ En el bosque de la china
la chinita se perdio """
print(parrafo)

# ===============================================
# La funcion len() obtiene el tama~no del string
# ===============================================
n = len(parrafo)
print(n)

# =============================================================
# Las letras en un string ocupan lugares como en un arreglo
# (tambien de atras para adelante comenzando en -1 el ultimo)
# =============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])