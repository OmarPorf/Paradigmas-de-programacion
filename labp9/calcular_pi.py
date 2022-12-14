#===============================================================
#   Calculo de PI por metodo de Montecarlo en Python-Cuda_Numba
#===============================================================
from __future__ import print_function, absolute_import
from numba import cuda
from numba.cuda.random import xoroshiro128p_uniform_float64
from numba.cuda.random import create_xoroshiro128p_states
import numpy as np
import random

@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    """
    Encontrar el valor maximo en value y guardarlo en result[0]
    """
    ii = cuda.grid(1)

    #   Calcular pi dibujando puntos (x, y) al azar y encontrando
    #   la fraccion de ellos que caen dentro del circulo unitario
    cae_dentro = 0
    for i in range(iteraciones):
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        if x ** 2 + y ** 2 <= 1.0:
            cae_dentro += 1
        out[ii] = 4.0 * cae_dentro / iteraciones

#======================
#   Procesos para cuda
#======================
hilosporbloque = 64
bloques = 24

#=======================
#   Arreglos necesarios
#=======================
seed1 = random.uniform(-1, 1)
seed2 = random.seed(seed1)
seed = random.randint(0, 1000)
rng_states = create_xoroshiro128p_states(hilosporbloque * bloques, seed)
out = np.zeros(hilosporbloque * bloques, dtype=np.float64)

#=======================
#   Llamar a la funcion
#=======================
calcularpi_kernel[bloques, hilosporbloque](rng_states, 10000, out)
print("pi =", out.mean())