from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import TNT, DEFAULT_TYPE
import random
class Tnt(PowerUp):
    def __init__(self):
        self.image = TNT
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)
        self.rect.y = random.randint(50, 150)

