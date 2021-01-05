#Import modules
import pygame
import display_settings
from spritesheet_img_grabber import img_grabber

#When creating this class, I referred to two videos: https://www.youtube.com/watch?v=3Bk-Ny7WLzE and https://www.youtube.com/watch?v=mBC5VqxnFLA
class Player(pygame.sprite.Sprite):

    #Change in speed
    change_x = 0
    change_y = 0

    #Animation pictures
    walking_frames_l = []
    walking_frames_r = []

    #Initial direction of player
    direction = "R"

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        #Load the spritesheet that will be used to animate
        sprite_sheet = img_grabber("images\\player.png")
        
        #Going Right
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        #Going Left
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #Starting image
        self.image = self.walking_frames_r[0] 

        #Convert it to a rectangle
        self.rect = self.image.get_rect()

    def update(self):

        #Gravity
        self.calc_grav()

        #Moving in the x-axis
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        
        #I had some help from this video: https://www.youtube.com/watch?v=ldh13IP8GAY
        #What happens if the player is moving right
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]

        #What happens if the player is moving left
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Collisions
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            
            if self.change_x > 0:
                self.rect.right = block.rect.left
                
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        #Moving in the y-axis
        self.rect.y += self.change_y

        #Collisions
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            #Stop from moving up and down
            self.change_y = 0

    #I watched this video to help me make the jumping function work properly with gravity: https://www.youtube.com/watch?v=G8pYfkIajE8 and this one as well: https://www.youtube.com/watch?v=pN9pBx5ln40     
    #Gravity function
    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
            
        else:
            self.change_y += .35

        #Check if player on platform
            
        if self.rect.y >= display_settings.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = display_settings.SCREEN_HEIGHT - self.rect.height

    #Jump function
    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= display_settings.SCREEN_HEIGHT:
            self.change_y = -10

    #Movement with animations    
    def left(self):
        self.change_x = -6
        self.direction = "L"

    def right(self):
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        self.change_x = 0
