from dino_runner.utils.constants import HAMMER_TYPE,RUNNING,JUMPING,DEFAULT_TYPE,DUCKING  ,SHIELD_TYPE, RUNNING_SHIELD , JUMPING_SHIELD , DUCKING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER
import pygame
class Dinosaur :
    X_pos = 80
    Y_pos = 310
    JUMP_VEL = 8.5
    y_pos_duck = 340
    


    def __init__(self):
        self.run_image = {DEFAULT_TYPE: RUNNING , SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }
        self.jump_image = {DEFAULT_TYPE: JUMPING , SHIELD_TYPE : JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.duck_image = {DEFAULT_TYPE: DUCKING , SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos

        self.jump_vel = self.JUMP_VEL
    

        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.shield = False
        self.shield_time_up =0
        self.has_powerd = False
    
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        
        if self.dino_run:
            self.run()

        if self.dino_duck:
            self.duck()

        if user_input[ pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif user_input[ pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck= False
        elif not self.dino_jump :
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False


        if self.step_index >=10 :
            self.step_index = 0

    def draw(self,screen):
        screen.blit(self.image ,(self.dino_rect.x,self.dino_rect.y))


    def event(self):
        pass

    def run(self):
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = self.run_image[self.type][self.step_index // 5]
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

    def duck(self):
            self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
            self.image = self.duck_image[self.type][self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_pos
            self.dino_rect.y = self.y_pos_duck
            self.step_index += 1
    
    def check_visibility(self,screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if (time_to_show >= 0):
                font = pygame.font.Font('freesansbold.ttf', 18)
                text = font.render(f'Shield enable for {time_to_show}', True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.center = (500, 40)
                screen.blit(text,text_rect)
            else:
                self.shield = False
                if(self.type == SHIELD_TYPE ):
                    self.type = DEFAULT_TYPE
