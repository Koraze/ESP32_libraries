from toolbox.timer import Timer

# Création d'un objet Timer
timer = Timer(500, True)
timer.set_pas(1000) # Exécution chaque seconde
timer.reinit()

# Exemple bloquant
while True :
    timer.waiting()
    print("hello")

# Exemple non bloquant
while True :
    if timer.remaining() <= 0 :  # Non bloquant
        print("hello")