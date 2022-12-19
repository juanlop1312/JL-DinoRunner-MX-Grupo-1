import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cloud import Cloud
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS , BIRD, CLOUD
from dino_runner.components.obstacles.bird import bird
from dino_runner.utils.constants import DAMAGE_SOUND

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_cloud = []
        self.disable_obstacles = False


    def update(self, game):
        # agregar al screen
        if len(self.obstacle_cloud) == 0:
            random_cloud = random.randint(0,1)
            if random_cloud == 1:
                self.obstacle_cloud.append(Cloud(CLOUD))
        for cloud in self.obstacle_cloud:
            cloud.update(game.game_speed + cloud.speed, self.obstacle_cloud)
        if self.disable_obstacles == False:
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
                DAMAGE_SOUND.play()
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


    def clear_all_obstacle(self):
        self.obstacles = []
        self.disable_obstacles = True
    def draw_cloud(self, screen):
        for obstacle_cloud in self.obstacle_cloud:
            obstacle_cloud.draw(screen)
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        