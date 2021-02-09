from p5 import core
from p5.POO.drop import Drop

drops=[]

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    for i in range(0, 1000):
        drops.append(Drop(400))


def run():
    print("run")
    for d in drops:
        d.tomber(400)
        d.afficher(core)


core.main(setup, run)
