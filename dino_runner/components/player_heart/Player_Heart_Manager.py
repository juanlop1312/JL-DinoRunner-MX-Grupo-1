from dino_runner.utils.constants import HEART_COUNT
from dino_runner.components.player_heart.heart import Heart


class PlayerHeartManager :
    def __init__(self):
        self.heart_count = HEART_COUNT
    


    def draw(self,screen):
        x_position = 10
        for counter in range(self.heart_count):
            heart = Heart (x_position)
            heart.draw(screen)
            x_position += 30

    def reduce_heart(self):
        self.heart_count -= 1
        