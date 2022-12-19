import random
from dino_runner.components.obstacles.cactus import Cactus
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS , BIRD
from dino_runner.components.obstacles.bird import bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,3)
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 3:
                self.obstacles.append(bird(BIRD))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect)  and game.player.shield == False: #CHocar y no tener el escudo
                game.Player_Heart_Manager.reduce_heart()
                if game.Player_Heart_Manager.heart_count > 0 :
                        self.obstacles.pop()
                else :
                    pygame.time.delay(500)
                    self.obstacles.remove(obstacle)
                    game.playing = False
                    game.death_count += 1
                    break
            if game.player.dino_rect.colliderect(obstacle.rect)  and game.player.shield == True: #CHocar y no tener el escudo
                if game.Player_Heart_Manager.heart_count > 0 :
                        self.obstacles.pop()



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)