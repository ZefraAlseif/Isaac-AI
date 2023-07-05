import pygame as p
from player import Player

WIDTH = 960
HEIGHT = 540
MAX_FPS = 60 # for animations


def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    current_level = loadLevels()
    screen.blit(current_level,(0,0))
    moving_sprites = p.sprite.Group()
    player = Player(WIDTH/2,HEIGHT/2)
    moving_sprites.add(player)
    running = True
    while running:
        moving_sprites.clear(screen,current_level)
        # Player inputs
        for e in p.event.get():
            # Player exits window 
            if e.type == p.QUIT:
                running = False 
            
        # Player inputs      
        moving_sprites.update()    
        moving_sprites.draw(screen)
        p.display.flip()
        clock.tick(MAX_FPS)
        print(moving_sprites)
        

def loadLevels():
    bg_level1 = p.image.load("Background/level_test.png")
    bg_level1 = p.transform.scale(bg_level1, (960,540)) 
    return bg_level1


if __name__ == "__main__":
    main()
