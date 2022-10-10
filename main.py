from game import *
from profile import *


repository = Repository()
game = Game(repository, random_number_start = 0, random_number_end = 5)
game.start()
