#====================================
#   mpirun -n 4 python3 TareasMPI.py
#====================================
from mpi4py import MPI

#===========================
#   Objeto de comunicadores
#===========================
comm = MPI.COMM_WORLD

#==========================
#   Cuantos somos en total
#==========================
size = comm.Get_size()

#=============
#   Quien soy
#=============
rank = comm.Get_rank()

#============================
#   Si soy el cero hago esto
#============================
if rank == 0:
    print("Yo soy el proceso 0")

#===================================
#   Si yo soy el uno hago esto otro
#===================================
elif rank == 1:
    print("Yo soy el proceso 1")

#===============================================
#   Si yo no soy ni el uno ni el dos, hago esto
#===============================================
else:
    print("Yo no soy ninguno de los dos primeros procesos")

print("Reportandome, soy el proceso", str(rank), "de", str(size))