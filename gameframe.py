import pygame,sys,time
from button import button
pygame.init()



class lives:
    '''class for lives'''
    def __init__(self,sc,x=12,y=410):
        '''class constructor
        Parameters:
        sc: screen on which lives should be displayed
        x1: x co-ordinate where life should be displayed
        y1: y co-ordinate where life should be displayed'''
        self.lives=15
        self.screen=sc
        self.x=x
        self.y=y
        
    def print_livenum(self):
        '''function to print number of lives left'''
        font=pygame.font.SysFont('calibri',35)
        if self.lives<0:
            self.lives=0
        text=font.render(str(self.lives),1,[0,0,0],[255,255,255])
        self.screen.blit(text,(self.x,self.y))

    def decrement_lives(self):
        '''function to decrement lives'''
        self.lives-=1
        

    def lives_sq(self):
        '''function to draw square'''
        pygame.draw.rect(self.screen,[255,255,255],(7,370,40,100))
        pygame.draw.rect(self.screen,[0,0,0],(7,350,43,100),3)
        
    def endgame(self):
        '''function to end the game if no lives left'''
        if self.lives<=0:
            return True



class cannon:
    '''class for cannon'''
    def __init__(self,sc,x1=300,y1=150,speed=4):
        '''class constructor
        Parameters:
        sc: screen where cannon is displayed
        x1: x co-ordinate of cannon
        y1: y co-ordinate of cannon
        speed: speed of the cannon'''
        self.dy=speed
        self.dx=2.75
        self.screen=sc
        self.x=x1
        self.y=y1
        self.cannon_rect=pygame.Rect([self.x,self.y,30,30])
        self.load_image()
        self.clock=pygame.time.Clock()
        
        
    def load_image(self):
        '''function to load image of a cannon'''
        self.cannon=pygame.image.load('images\\cannon.jpeg').convert()
        self.cannon_image=pygame.transform.scale(self.cannon,(30,30))
        return self.cannon_image
        
    def print_cannon(self):
        '''function to print cannon image'''
        self.cannon_rect=pygame.Rect([self.x,self.y,30,30])
        pygame.draw.rect(self.screen,[0,0,0],self.cannon_rect)
        self.screen.blit(self.cannon_image,(self.x,self.y))
        
       
    def collision_with_shield(self):
        '''function  which detects collision of cannon with user
        ship and perform functions on cannon accordingly'''
        if self.cannon_rect.colliderect(self.shield_rect):
           
            if abs(self.shield_rect.top-self.cannon_rect.bottom)<10:
                self.dy*=-1
            if abs(self.shield_rect.bottom-self.cannon_rect.top)<10:
                self.dy*=-1
            
            if abs(self.shield_rect.right-self.cannon_rect.left)<10 and self.dx<0:
                self.dx*=-1
            if abs(self.shield_rect.left-self.cannon_rect.right)<10 and self.dx>0:
                self.dx*=-1
           
    def collision_with_compshield(self):
        '''function  which detects collision of cannon with computer
        ship and perform functions on cannon accordingly'''
        if self.cannon_rect.colliderect(self.compshield_rect):
            if abs(self.compshield_rect.top-self.cannon_rect.bottom)<10:
              self.dy*=-1
            if abs(self.compshield_rect.bottom-self.cannon_rect.top)<10:
                self.dy*=-1
                
            if abs(self.compshield_rect.right-self.cannon_rect.left)<10 and self.dx<0:
                self.dx*=-1
            if abs(self.compshield_rect.left-self.cannon_rect.right)<10 and self.dx>0:
                self.dx*=-1
                
    def collision_with_ship(self):
        '''functiion which decrements one life if there is a collision of cannon
        with user ship and returns True'''
        if self.cannon_rect.colliderect(self.ship_rect):
            self.lives.decrement_lives()
            return True
            
    def collision_with_compship(self):
        '''functiion which decrements one life if there is a collision of cannon
        with computer ship and returns True'''
        if self.cannon_rect.colliderect(self.comp_rect):
            self.comp_lives.decrement_lives()
            return True

    def shoot_cannon(self,other_rect,comp_shield,lives,comp_lives,ship_rect,comp_rect):
        '''function for shooting cannon
        Parameters:
        other_rect: user shield rectangle
        comp_shield: computer shield rectangle
        lives: object of user lives
        comp_lives: object of computer lives
        ship_rect: user ship rectangle
        comp_rect: computer ship rectangle'''
        #shield_rect
        self.shield_rect=other_rect
        self.compshield_rect=comp_shield
        #lives rect
        self.lives=lives
        self.comp_lives=comp_lives
        #ship rect
        self.comp_rect=comp_rect
        self.ship_rect=ship_rect
        
        self.print_cannon()
        self.collision_with_shield()
        self.collision_with_compshield()
        
        if self.collision_with_ship():
            self.y=150
        if self.collision_with_compship():
            self.y=670
        #to make the cannon bounce back on touching sides of the screen
        if self.cannon_rect.right>=1000 or self.cannon_rect.left<=0:
            self.dx*=-1
        if  self.cannon_rect.top<=36 :
            self.dy*=-1
            
        self.x+=self.dx
        self.y+=self.dy


        

class frame_for_game:
    '''class for displaying game frame '''
    count=0
    def __init__(self,sc):
        '''class constructor
        Parameters:
        sc: screen on which frame is displayed'''
        #colors
        self.grey=pygame.Color('grey65')
        self.white=[255,255,255]
        #screen
        self.screen=sc
        #filling screen white
        self.screen.fill(self.white)
        self.count1=0
        #shield objects
        self.compshield=comp_shield(self.screen)
        self.shield=shield(self.screen)
        #life objects
        self.comp_lives=lives(sc,y=360)
        self.lives=lives(sc)
        #cannon objects
        self.cannons=[]
        for i in range (3):
            self.cannon=cannon(sc)
            self.cannons.append(self.cannon)
        for j in range(4):
            self.cannon=cannon(sc,780)
            self.cannons.append(self.cannon)
        for k in range(1):
            self.cannon=cannon(sc,500)
            self.cannons.append(self.cannon)

        #loading and setting ship
        self.user_ship=self.load_ship()
        self.comp_ship=self.load_ship()
        self.comp_ship=pygame.transform.rotate(self.comp_ship,180)
        self.ship_rect=pygame.Rect([0,750,1000,60])
        self.comp_rect=pygame.Rect([0,40,1000,60])
    
        #if user presses exit button
        self.exit=self.create_frame()
        #game will start with a count down
        Countdown.reset_count()

    def create_frame(self):
        '''this function contains the loop for displaying game screen'''
        main=True
        while main==True:
            exit_=self.mainloop()
            if exit_=='Exit':
                return 'Exit'
            self.screen.fill([255,255,255])
            
            #line ,lives,exitbutton,shield,ship
            self.createline()
            self.lives.lives_sq()
            self.lives.print_livenum()
            self.comp_lives.print_livenum()
            self.exit_button=button(7,8,100,30,'Exit',self.screen,self.white,f=30,wd_outline=4,change_c=self.grey)
            self.exit_button.drawsqbutton()
            self.shield.shield_()
            self.shoot_cannons()
            
            collide=[self.cannons[0].cannon_rect.y,self.cannons[1].cannon_rect.y,self.cannons[2].cannon_rect.y\
                     ,self.cannons[3].cannon_rect.y,self.cannons[4].cannon_rect.y,self.cannons[5].cannon_rect.y,self.cannons[6].cannon_rect.y\
                     ,self.cannons[7].cannon_rect.y]
            index=collide.index(min(collide))
            self.compshield.move_shield(self.cannons[index].cannon_rect)
            
            pygame.draw.rect(self.screen,[0,0,0],self.ship_rect)
            pygame.draw.rect(self.screen,[0,0,0],self.comp_rect)
            self.screen.blit(self.user_ship,(0,750))
            self.screen.blit(self.comp_ship,(0,40))

            Countdown(self.screen)

            if self.lives.endgame():
                self.lives.print_livenum()
                self.display_winner('COMPUTER')
                return 'Exit'
            if self.comp_lives.endgame():
                self.comp_lives.print_livenum()
                self.display_winner('PLAYER', x=310) 
                return 'Exit'
            
            
            
    def mainloop(self):
        '''function where all the event based operations are performed which
        needs to be called inside the loop'''
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                self.shield.move(event)
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEMOTION:
                    if self.exit_button.isOver(pos) :
                        self.exit_button.changesqcolor()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.isOver(pos):
                        return 'Exit'
        pygame.display.flip()
        
    def createline(self):
        '''draws the line in the game frame'''
        pygame.draw.line(self.screen,[0,0,0],[0,42],[1100,42],2)
        
    def load_ship(self):
        '''load ship image'''
        self.ship=pygame.image.load('images/ship.jpeg').convert()
        self.ship_image=pygame.transform.scale(self.ship,(1000,60))
        return self.ship_image
    
    def shoot_cannons(self):
        '''shoot cannons'''
        self.cannons[0].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        self.count1+=1
        if self.count1>150:
            self.cannons[1].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>190:
            self.cannons[2].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>250:
            self.cannons[3].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>290:
            self.cannons[4].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>330:
            self.cannons[5].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>360:
            self.cannons[6].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
        if self.count1>500:
            self.cannons[7].shoot_cannon(self.shield.shield_rect,self.compshield.shield_rect,self.lives,self.comp_lives,self.ship_rect,self.comp_rect)
       

    def display_winner(self, winner, x=250):
        '''display's winner name'''
        font1 = pygame.font.SysFont('didot.ttc', 130)
        font2 = pygame.font.SysFont('didot.ttc', 82)
        img1 = font1.render('GAME OVER', True, (0, 0, 255))  #(0, 0, 255)= BLUE
        img2 = font2.render(f'{winner} WINS', True, (0, 0, 255))  #(0, 0, 255)= BLUE
        self.screen.blit(img1, (220, 220))
        self.screen.blit(img2, (x, 330))
        pygame.display.update()
        pygame.time.wait(3000)
        







    









class comp_shield:
    '''class for computer shield'''
    def __init__(self,sc,x1=450,y1=50):
        '''class constructor
        Parameters:
        sc: screen on which computer shield should be displayed
        x1: x co-ordinate of computer shield
        y1: y co-ordinate of computer shield'''
        self.screen=sc
        self.x=x1
        self.y=y1
        self.load_image()
        self.print_shield()
        self.clock=pygame.time.Clock()
        
    def load_image(self):
        '''function to load shield image'''
        self.shield_image=pygame.image.load('images/shield.jpeg').convert()
        self.shield=pygame.transform.scale(self.shield_image,(120,95))
        self.shield=pygame.transform.rotate(self.shield,180)
        
    def print_shield(self):
        '''function to display shield image'''
        self.shield_rect=pygame.Rect([self.x,self.y,120,95])
        #every image in the game is displayed on a rectangle of the same
        #size as image because of a builtin function to check collisions between
        #rectangles.
        pygame.draw.rect(self.screen,[0,0,0],self.shield_rect)
        self.screen.blit(self.shield,(self.x,self.y))
    
    def move_shield(self,cannon_rect):
        '''function to move shield
        Parameters:
        cannon_rect: cannon rectangle'''
        self.cannon_rect=cannon_rect
        
        if self.x<self.cannon_rect.x:
            self.x+=21
        if self.x>self.cannon_rect.x:
            self.x-=21

        #for not crossing the screen
        if self.x<0:
            self.x=0
        elif self.x>=900:
            self.x=900
        self.print_shield()
        



class shield:
    '''class for performing opertions on user shield '''
    def __init__(self,sc,x1=450,y1=700):
        '''class constructor
        Parameters:
        sc: screen on which user shield should be displayed
        x1: x co-ordinate of user shield
        y1: y co-ordinate of user shield'''
        self.screen=sc
        self.x=x1
        self.y=y1
        self.load_image()
        self.clock=pygame.time.Clock()
        self.x_change=0
        
    def load_image(self):
        '''loads user shield image'''
        self.shield_image=pygame.image.load('images/shield.jpeg').convert()
        self.shield=pygame.transform.scale(self.shield_image,(120,120))
        
    def shield_(self):
        '''function to update the position of shield'''
        self.x+=self.x_change
        if self.x<0:
            self.x=0
        elif self.x>=900:
            self.x=900
       
        self.print_shield()
        self.clock.tick(40)
        
    def print_shield(self):
        '''function to display shield image'''
        self.shield_rect=pygame.Rect([self.x,self.y,120,120])
        #every image in the game is displayed on a rectangle of the same
        #size as image because of a builtin function to check collisions between
        #rectangles.
        pygame.draw.rect(self.screen,[0,0,0],self.shield_rect)
        self.screen.blit(self.shield,(self.x,self.y))
        
    def move(self,event):
        '''function which contains all the keyboard events to move point
        accordingly'''
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT :
                self.x_change=-10.5
            if event.key==pygame.K_RIGHT:
                self.x_change=10.5
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT  or  event.key==pygame.K_RIGHT:
                self.x_change=0


   



class Countdown:
    ''' Countdown starts from 3 and as it reaches 0 the game starts. '''

    count=0
    def __init__(self,screen):
        '''class constructor
        Parameters:
        screen: main game screen '''
        
        # countdown will run only at the start of every game.
        if Countdown.count==0:
            secs=3
            while secs: 
                font = pygame.font.SysFont('didot.ttc', 372)
                img = font.render(str(secs), True, (0, 0, 255))  #(0, 0, 255)= BLUE
                screen.blit(img, (420, 320))
                pygame.display.update()
                time.sleep(1) 
                secs -= 1          
                pygame.draw.rect(screen, (255, 255, 255), (420,320,520,420))  #(255, 255, 255)= WHITE

            Countdown.count+=1

    def reset_count():
        ''' This method resets variable 'count'.
            Useful: when player exits the game and comes
            to main menu.'''
        Countdown.count = 0




























        

