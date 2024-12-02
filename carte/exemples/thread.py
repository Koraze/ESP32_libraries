from toolbox.thread import Thread

# Fonction type
def show():
    print("hello")

# Création d'un thread sur notre foction
exemple = Thread("hello", show, dt=2000)

# Lancement puis arrêt du thread
print("start")
exemple.start()
sleep(6)
exemple.stop()

# Lancement puis arrêt de tous les threads
print("start all")
Thread.start_all()
sleep(6)
Thread.stop_all()