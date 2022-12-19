import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.player_heart.Player_Heart_Manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur() 
        self.obstacle_manager = ObstacleManager()
        self.Player_Heart_Manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()


        self.death_count = 0
        self.points = 0
        self.running = True

    def execute(self):
        while self.running :
            if not self.playing :
                self.show_menu()
                



    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.obstacle_manager)





    def draw(self):
        self.draw_score()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_score()
        self.obstacle_manager.draw_cloud(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.Player_Heart_Manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
       
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    
    def draw_score(self):
        self.points += 1 

        if self.points % 100 == 0:
            self.game_speed +=1

        text,text_rect = text_utils.get_score_element(self.points)
        self.player.check_visibility(self.screen, self.obstacle_manager)
        self.screen.blit(text,text_rect)
    


    def show_menu(self):
        whit_color = (255,255,255)
        self.screen.fill(whit_color)
        
        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()


    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT//2

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("presione cualquier tecla para iniciar")
            self.screen.blit(text,text_rect)
        elif self.death_count > 0:
            text, text_rect = text_utils.get_centered_message(" ")
            score , score_rect =text_utils.get_centered_message("your score is:"+str(self.points), height = half_screen_height + 100)
            death , death_rect = text_utils.get_centered_message("-     death count : "+ str(self.death_count), half_screen_height + 150 )
            self.screen.blit(score, score_rect)
            self.screen.blit(text , text_rect)
            self.screen.blit(death , death_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.obstacle_manager = ObstacleManager()
                self.Player_Heart_Manager = PlayerHeartManager()
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.obstacle_manager = ObstacleManager()
                self.points = 0
                self.game_speed = 20
                self.Player_Heart_Manager = PlayerHeartManager() 
                self.run()
                



