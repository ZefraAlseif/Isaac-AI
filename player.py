import pygame as p
import os
from os import listdir
class Player(p.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        
        # player movement
        self.direction = p.math.Vector2(0,0) # direction is 1,2,3 or 4
        self.speed = 8  
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
            
    # Look in the location to move
    def get_input(self,key_press):
        if key_press == p.K_w:
            self.direction.x = 0
            self.direction.y = -1
            self.current_sprite = 0
        elif key_press == p.K_s:
            self.direction.x = 0
            self.direction.y = 1
            self.current_sprite = 1
        elif key_press == p.K_a:
            self.direction.x = -1
            self.direction.y = 0
            self.current_sprite = 2
        elif key_press == p.K_d:
            self.direction.x = 1
            self.direction.y = 0
            self.current_sprite = 3
        else:
            self.direction.x = 0
            self.direction.y = 0
            self.current_sprite = self.current_sprite


    def update(self,key_press):
        self.get_input(key_press)
        self.image = self.sprites[self.current_sprite]
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
