#Import modules
import pygame
from spritesheet_img_grabber import img_grabber

#These are the coordinates of where the platforms are located in the spritesheet. I decided to use a spritesheet that was full with the coordinates given already, which then I changed with my own favourable platforms. Here is the link to the spritesheet https://opengameart.org/content/platformer-pack-industrial-100
plat_l = (576, 720, 70, 70)
plat_r = (576, 576, 70, 70)
plat_m = (504, 576, 70, 70)

#I learned that doing this is possible from this video: https://www.youtube.com/watch?v=mfX3XQv9lnI
class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = img_grabber("images\\tiles_spritesheet.png")

        #Get each part of the platform from the spritesheet
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        #Convert into rectangles so it can collide with the ninja
        self.rect = self.image.get_rect()


