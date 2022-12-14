from dino_runner.utils.constants import RUNNING , JUMPING , DEFAULT_TYPE
import pygame
class Dinosaur :
    X_pos = 80
    Y_pos = 310
    JUMP_VEL = 8.5


    def __init__(self):
        self.run_image = {DEFAULT_TYPE: RUNNING}
        self.jump_image = {DEFAULT_TYPE: JUMPING}
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos

        self.jump_vel = self.JUMP_VEL
    

        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
    
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        
        if self.dino_run:
            self.run()

        if user_input[ pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
        elif not self.dino_jump :
            self.dino_run = True
            self.dino_jump = False


        if self.step_index >=10 :
            self.step_index = 0

    def draw(self,screen):
        screen.blit(self.image ,(self.dino_rect.x,self.dino_rect.y))


    def event(self):
        pass

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 3
            self.jump_vel -= 0.8 
        if self.jump_vel <- self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL