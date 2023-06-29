import pygame as p
import os
from os import listdir
import random
class Player(p.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        
        # player movement
        self.direction = p.math.Vector2(0,0) # direction is 1,2,3 or 4
        self.speed = 5  
        #self.map = {(0,1):0,(0,-1):1,(-1,0):2,(1,0):3}
        self.sprites = []
        folder_dir = "D:\Programming Projects\Isaac AI\Player_Sprites"
        """
        {0:stand_bw,1:stand_fw,2:stand_lf,3:stand_rt,4:walkbw_lff,5:walkbw_rff
         6:walkfw_lff,7:walkfw_rff,8:walklf_lff,9:walklf_rff,10:walkrf_lff,11:walkrf_rff}
        """
        for image in os.listdir(folder_dir):
            temp_image = p.image.load(f"Player_Sprites\{image}")
            temp_image = p.transform.scale(temp_image, (64,64))
            self.sprites.append(temp_image)
        print(self.sprites)
        self.current_sprite = 1
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        # Animate the player movement
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
    # Look in the location to move
    def getInput(self):
        keys = p.key.get_pressed()
        if  keys[p.K_w] or keys[p.K_UP]:
            self.direction.y = -1
            self.current_sprite = 0
            self.move_up = True
        elif keys[p.K_s] or keys[p.K_DOWN]:
            self.direction.y = 1
            self.current_sprite = 1
            self.move_down = True
        else:
            self.direction.y = 0
            self.move_down = False
            self.move_up = False
        if keys[p.K_a] or keys[p.K_LEFT]:
            self.direction.x = -1
            self.current_sprite = 2
            self.move_left = True
        elif keys[p.K_d] or keys[p.K_RIGHT]:
            self.direction.x = 1
            self.current_sprite = 3
            self.move_right = True
        else:
            self.direction.x = 0
            self.move_left = False
            self.move_right = False

    def getAnimation(self):
        if self.move_up:
            # 4 or 5
            temp = [4,5]
            if self.current_sprite != 4 or self.current_sprite != 5:
                self.current_sprite = random.choice(temp)
            else:
                self.current_sprite = not temp[self.current_sprite]
        elif self.move_down:
            # 6 or 7
            temp = [6,7]
            if self.current_sprite != 6 or self.current_sprite != 7:
                self.current_sprite = random.choice(temp)
            else:
                self.current_sprite = not temp[self.current_sprite]
        elif self.move_left:
            # 8 or 9
            temp = [8,9]
            if self.current_sprite != 8 or self.current_sprite != 9:
                self.current_sprite = random.choice(temp)
            else:
                self.current_sprite = not temp[self.current_sprite]
        elif self.move_right:
            # 10 or 11
            temp = [10,11]
            if self.current_sprite != 10 or self.current_sprite != 11:
                self.current_sprite = random.choice(temp)
            else:
                self.current_sprite = not temp[self.current_sprite]
    
    def update(self):
        self.getInput()
        self.getAnimation()
        self.image = self.sprites[self.current_sprite]
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
