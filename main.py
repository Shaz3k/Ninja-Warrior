"""Ninja Warrior
By: Shazil Razzaq

Sprites are from: https://www.gameart2d.com/ninja-adventure---free-sprites.html
Platforms are from: https://www.gameart2d.com/free-graveyard-platformer-tileset.html
Splat audio is from: https://www.youtube.com/watch?v=xD98iODedWk
Background music is from: https://www.youtube.com/watch?v=lR4Sik1zyqo, https://www.youtube.com/watch?v=VzMh1O-MJYE, https://www.youtube.com/watch?v=bl9MSkMIxa8
Background images are from: http://appreskinning.blogspot.ca/2017/07/backgrounds-for-2d-platforms-pack.html, https://chewyfa.deviantart.com/art/Abandoned-City-Background-362762133, http://www.misucell.com/group/cool-black-and-red-wallpapers/
Gold Medal Template is from: http://www.pngall.com/gold-medal-png
"""

#Import modules
import pygame
from display_settings import *
import course
import time
from player import Player
from decimal import Decimal
import platforms
from spritesheet_img_grabber import img_grabber

#Initialization
pygame.init()
pygame.font.init()

#Icon
icon = pygame.image.load("images\\icon.png")
pygame.display.set_icon(icon)

#Audio
splat=pygame.mixer.Sound("audio\\splat_sound.wav")
pygame.mixer.music.load("audio\\background_music.mp3")


#Global variables
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pause = False
score_list = []

#Import different backgrounds
intro_background = pygame.image.load("images\\intro_background.png")
intro_background_rect = intro_background.get_rect()

paused_background = pygame.image.load("images\\paused_background.png")
paused_background_rect = intro_background.get_rect()

ending_background = pygame.image.load("images\\ending_background.png")
ending_background_rect = intro_background.get_rect()

winner_background = pygame.image.load("images\\winner.png")
winner_background_rect = winner_background.get_rect()

controls_background = pygame.image.load("images\\controls.png")
controls_background_rect = controls_background.get_rect()

#Text object function that will be used to create buttons for interactive menus
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#Button function
#I had a bit of help creating this function. I watched this video: https://www.youtube.com/watch?v=kK4xhHr1QeQ
def button(msg,x,y,w,h,ic,ac,action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,100,50))
        if click[0] == 1 and action != None:
            
            if action == "play":
                game()
                
            elif action == "quit":
                pygame.quit()
                quit()
                
            elif action == "controls":
                controls()
                
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#Game intro function
def game_intro():
    
    #Play looped music
    pygame.mixer.music.play(-1)
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Draw background on display       
        screen.blit(intro_background, intro_background_rect)

        button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,"play")
        button("Quit",550,450,100,50,RED,BRIGHT_RED,"quit")
        button("Controls",350,450,100,50,BLUE,BRIGHT_BLUE,"controls")

        #Update the display
        pygame.display.update()
        clock.tick(15)

#Control function
def controls():
    
    while controls:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #Draw background on display
            screen.blit(controls_background, controls_background_rect)

            #Buttons
            button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,"play")
            button("Quit",550,450,100,50,RED,BRIGHT_RED,"quit")

            #Update the display
            pygame.display.update()
            clock.tick(15)

#Pause function
def paused(pause):

    #Pause music
    pygame.mixer.music.pause()
    pause=True
    return pause

#Unpause function
def unpause(pause):

    #Unpause music
    pygame.mixer.music.unpause()
    pause = False
    return pause

#Crash function
def crash(current_position):

    #Stop background music
    pygame.mixer.music.stop()

    #Play splat sound
    pygame.mixer.Sound.play(splat)

    #Score
    file = open("score.txt","a+")
    current_position-=10
    score=str(abs(current_position))
    file.write(score+"\n")
    file.close()
    file = open ("score.txt","r")
    file_list = file.readlines()
    for s in file_list:
        score_list.append(int(s))
    file.close()

    #Highscore
    high_score=str(max(score_list))

    #Draw background on display
    screen.blit(ending_background, ending_background_rect)

    largeText = pygame.font.Font('freesansbold.ttf',64)
    TextSurf, TextRect = text_objects(score, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(374))
    screen.blit(TextSurf, TextRect)

    smallText = pygame.font.Font('freesansbold.ttf',24)
    TextSurf, TextRect = text_objects("High Score: " + high_score, smallText)
    TextRect.center = ((SCREEN_WIDTH/2),(444))
    screen.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Buttons
        button("Play!",154,540,100,50,GREEN,BRIGHT_GREEN,"play")
        button("Quit",550,540,100,50,RED,BRIGHT_RED,"quit")
        button("Controls",350,540,100,50,BLUE,BRIGHT_BLUE,"controls")

        #Update the display
        pygame.display.update()
        clock.tick(15)
        
#Winner Function
def winner():      
    while winner:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            screen.blit(winner_background, winner_background_rect)
            
            button("Play!",150,450,100,50,GREEN,BRIGHT_GREEN,"play")
            button("Quit",550,450,100,50,RED,BRIGHT_RED,"quit")

            pygame.display.update()
            clock.tick(15)

#Game function
def game():
    running = True
    
    #Play music
    pygame.mixer.music.play(-1)

    global pause

    #Create the player
    player = Player()
    
    #I had some help from Stack Overlow: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame and from a video: https://www.youtube.com/watch?v=FpufbRZxKRM
    #Create the course
    level_list = []
    level_list.append(course.Course(player))
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #Initial position
    player.rect.x = 1000
    player.rect.y = SCREEN_HEIGHT - player.rect.height-300

    #Add the player to the list of sprites that will be drawn 
    active_sprite_list.add(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            if event.type == pygame.KEYDOWN:

                #If right key clicked, go right
                if event.key == pygame.K_RIGHT:
                    player.right()

                #If spacebar clicked, jump
                if event.key == pygame.K_SPACE:
                    player.jump()
                    
                #If left key clicked, go left
                if event.key == pygame.K_LEFT:
                    player.left()

                #If p is clicked, pause the game
                if event.key == pygame.K_p:
                    pause=paused(pause)

                #If q is clicked, unpause the game
                if event.key==pygame.K_q:
                    pause=unpause(pause)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        if not pause:
            #Update
            active_sprite_list.update()
            current_level.update()

            #To be able to move the background I watched two YouTube videos: https://www.youtube.com/watch?v=AX8YU2hLBUg and https://www.youtube.com/watch?v=qKyy6374V8E
            #If the player goes towards the right, shift the world left
            if player.rect.x >= 500:
                diff = player.rect.x - 500
                player.rect.x = 500
                current_level.shift_world(-diff)

            #If the player goes towards the left, shift the world right
            if player.rect.x <= 120:
                diff = 120 - player.rect.x
                player.rect.x = 120
                current_level.shift_world(diff)

            #What happens if the player finishes the entire course
            current_position = player.rect.x + current_level.world_shift
            if current_position <= -27000:
                winner()

            #What happens if the player hits the bottom of the screen 
            if player.rect.y + player.rect.height >= SCREEN_HEIGHT:

                #Run the crash function
                crash(current_position)
                running = False

            #Draw the course
            current_level.draw(screen)

            #Draw the sprites
            active_sprite_list.draw(screen)


            #I read through a website on how to reduce the FPS in my game due to it being too fast to play properly: https://www.pygame.org/docs/ref/time.html
            clock.tick(66)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #Pause menu     
            screen.blit(paused_background, paused_background_rect)           
            button("Quit",550,450,100,50,RED,BRIGHT_RED,"quit")

        #Update the display
        pygame.display.update()

#Run the game
game_intro()
