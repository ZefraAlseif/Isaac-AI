import pygame as p

p.init()
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
    running = True
    while running:
        # Player inputs
        for e in p.event.get():
            # Player exits window 
            if e.type == p.QUIT:
                running = False 
            # Player inputs
            if e.type == p.KEYDOWN:
                pass
        clock.tick(MAX_FPS)
        p.display.flip()

def loadLevels():
    bg_level1 = p.image.load("Background/bg_level1.png")
    bg_level1 = p.transform.scale(bg_level1, (960,540)) 
    return bg_level1


if __name__ == "__main__":
    main()
