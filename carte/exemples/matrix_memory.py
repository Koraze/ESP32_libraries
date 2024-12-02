#### Essai - Calcul de la mémoire consommée ####
from display.neopixel_matrix import *

# Calcul de la mémoire déjà occupée
import gc
gc.collect()
start = gc.mem_free()

# Création, puis enregistrement de notre image pic dans la matrix
matrix = Matrix(13, 5, 5)

pic = Picture(model  = "frame_char",
               frame  = ["00001", "00010", "00002", "00002", "00002"],
               color  = [[0, 0, 0], [4, 0, 0], [0, 4, 0]],
               size_x = 5,
               size_y = 5)

matrix.write(pic)

# Calcul de la mémoire consommée par la création et l'utilisation de notre image
print(start - gc.mem_free())