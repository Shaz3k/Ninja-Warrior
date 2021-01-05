#Import modules
import pygame
from display_settings import *
import platforms

#I had some help getting an idea of how to create this through this video https://www.youtube.com/watch?v=OmlQ0XCvIn0
class Level():  

    #List of platforms
    platform_list = []

    # Background image
    background = None

    #Shifting in the x-axis
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.player = player

    # Update everything in this course
    def update(self):
        self.platform_list.update()

    def draw(self, screen):

        #Depth effect - Watched a YouTube Video: https://www.youtube.com/watch?v=i0PaigPo6KM
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw platforms
        self.platform_list.draw(screen)

    #Shift the course
    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

# Create platforms for the course
class Course(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        #Load Background
        self.background = pygame.image.load("images\\background_01.png")

        #Generate the platforms relatve to one another and make it challenging
        z=0
        x=700
        y=550
        level=[]
        while z<100:
            z+=1

            if y>=550:   
                level.append([platforms.plat_l,x,y])
                level.append([platforms.plat_m,x+70,y])
                level.append([platforms.plat_r,x+140,y])
                y-=220
                x+=280
            
            if y<550:
                level.append([platforms.plat_l,x,y])
                level.append([platforms.plat_m,x+70,y])
                level.append([platforms.plat_r,x+140,y])
                x+=280
                y+=200

        #To be able to properly implement the platforms, I read through pages 251-252 of the book called "Program Arcade Games: With Python and Pygame" by Paul Craven and also read this: https://www.pygame.org/docs/ref/rect.html   
        for platform in level:
            block = platforms.Platform(platform[0])

            #X-position
            block.rect.x = platform[1]

            #Y-position
            block.rect.y = platform[2]
            
            block.player = self.player

            #Add to list
            self.platform_list.add(block)
