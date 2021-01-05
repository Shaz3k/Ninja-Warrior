#Import modules
import pygame
import display_settings

#Used to obtain images from the spritesheet based on their coordinates, width and height.
class img_grabber(object):
    
    sprite_sheet = None

    def __init__(self, file_name):

        # Load spritesheet
        self.sprite_sheet = pygame.image.load(file_name)

    def get_image(self, x, y, width, height):

        #Create a blank image
        image = pygame.Surface([width, height])

        #Put the cropped out image from the spritesheet onto the newly created image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        #Use as transparent colour - Got idea from: https://www.pygame.org/docs/ref/surface.html
        image.set_colorkey(display_settings.BLACK)

        #Return the image
        return image

