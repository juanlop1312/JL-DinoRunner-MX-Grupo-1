from asyncio import shield
import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.points = 0

    def update(self, point, game_speed, player):
        self.genrate_random_power_up()
        
        for powerup in self.power_ups:
            powerup.update(game_speed, self.power_ups)
            if (player.dino_rect.colliderect(powerup.rect)):
                powerup.start_time = pygame.time.get_ticks()
                player.shield = True
                player.type = powerup.type
                powerup.start_time = pygame.time.get_ticks()
                player.shield_time_up = powerup.start_time + ((random.randint(5,8) * 1000))
                self.power_ups.remove(powerup)
   
   
    def draw(self,screen):
        for powerup in self.power_ups:
            powerup.draw(screen)


    def genrate_random_power_up(self):
        random_power_up = random.randint(0,100)
        if random_power_up == 10:
            random_type = random.randint(0,1)
            if random_type == 0:
                self.generate_power_ups(Shield())
            if random_type == 1:
                self.generate_power_ups(Hammer())
    def generate_power_ups(self, power):
        if len(self.power_ups) == 0:
            self.power_ups.append(power)





