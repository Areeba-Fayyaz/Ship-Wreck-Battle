import pygame
import os
import sys,time
from button import button
from gameframe import frame_for_game
from instructions import frame_for_instructions
pygame.init()


def mainmenu():
    '''This function displays the mainmenu'''
    
    #defining colors
    white=pygame.Color('beige')
    antique=pygame.Color('steelblue')
    grey=pygame.Color('grey65')
    clock=pygame.time.Clock()
    
    #setting screen size
    screen=pygame.display.set_mode((1000,800))
    
    #setting title
    pygame.display.set_caption('Ship Wreck Battle')
    
    #loading picture for the background
    background_image=pygame.image.load('images/menuImage.jpeg').convert()
    
    #to force game to stay open long enough to be visible we have to use
    #a loop otherwise it will only last for a few milliseconds only.
    main=True
    while main==True:
        #buttons that are displayed in main menu
        play_button=button(340,500,300,90,'Play',screen,white,change_c=grey)
        play_button.drawbutton()
        ins_button=button(340,600,300,95,'Instructions',screen,white,change_c=grey)
        ins_button.drawbutton()
        
        for event in pygame.event.get():
            #if user chooses to quit
            if event.type==pygame.QUIT:
                pygame.quit()
            #if user chooses to minimize   
            if event.type==0:
                pygame.display.iconify()

            pos=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEMOTION:
                if play_button.isOver(pos):
                    play_button.changecolor()
                if ins_button.isOver(pos):
                    ins_button.changecolor()

            #button clicks
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    playGame=frame_for_game(screen)
                    if playGame.exit=='Exit':
                        mainmenu()
                if ins_button.isOver(pos):
                    instructions=frame_for_instructions(screen)
                    if instructions.exit=='Exit':
                        mainmenu()
        
        pygame.display.flip()
        clock.tick(10)
        screen.blit(pygame.transform.scale(background_image,[1000,800]),(0,0))

