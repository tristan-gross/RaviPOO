from agario.creep import Creep
from agario.player import Player
from p5 import core
from p5.core import getMouseLeftClick

player1 = None
creeps = []

def setup():
    print("setup START")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    global player1
    player1 = Player()
    print("setup END")
    for i in range(0, 1000):
        creeps.append(Creep())

def run():
    print("run")
    for d in creeps:
        d.afficher(core)
    player1.afficher(core)
    if getMouseLeftClick() is not None:
        player1.deplacer(getMouseLeftClick())


core.main(setup, run)
