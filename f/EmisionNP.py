from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#   Tama~no del arreglo
n = 10
if rank == 0:
    #   Arreglo de enteros del 0 al n - 1
    data = numpy.arange(n, dtype='i')
else:
    #   Arreglo vacio de enteros de tama~no n
    data = numpy.empty(n, dtype='i')

#============================================
#   Broadcast pro que indica el tipo de dato
#   optimizado para comunicacion rapida
#============================================
comm.Bcast([data, MPI.INT], root=0)

#==================================
#   Asegurarse que todo salio bien
#==================================
for i in range(n):
    assert data[i] == i
print(data)