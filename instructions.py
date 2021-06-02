import pygame,sys
from button import button
pygame.init()



class frame_for_instructions:
    '''class for displaying instructions frame'''
    def __init__(self,sc):
        '''class constructor
        Parameters:
        sc: screen on which frame is displayed'''
        self.white=pygame.Color('beige')
        self.grey=pygame.Color('grey65')
        self.screen=sc
        self.white=[255,255,255]
        self.exit=self.create_frame()

    def create_frame(self):
        '''this function contains theloop for displaying instruction screen'''
        self.screen.fill(self.white)
        self.createline()
        pygame.display.flip()
        main=True
        while main==True:
            self.back_button=button(7,8,100,30,'Back',self.screen,self.white,f=30,wd_outline=4,change_c=self.grey)
            self.back_button.drawsqbutton()
            exit_=self.mainloop()
            if exit_=='Exit':
                return 'Exit'
            pygame.display.flip()

    def mainloop(self):
        '''function where all the event based operations are performed which
        needs to be called inside the loop'''
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEMOTION:
                    if self.back_button.isOver(pos) :
                        self.back_button.changesqcolor()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.back_button.isOver(pos):
                        return 'Exit'
        self.print_instructions()
    def createline(self):
        '''draws the line in the instruction frame'''
        pygame.draw.line(self.screen,[0,0,0],[0,42],[1100,42],2)

    def print_instructions(self):
        '''displays instructions on the screen'''
        font=pygame.font.SysFont('calibri',37)
        text1=font.render('Instructions',1,[0,0,0],[255,255,255])
        self.screen.blit(text1,(400,250))

        font=pygame.font.SysFont('calibri',27)
        text2=font.render("Protect your ship from your opponent's cannon shots!",1,[0,0,0],[255,255,255])
        self.screen.blit(text2,(230,340))

        font=pygame.font.SysFont('calibri',27)
        text2=font.render("Use arrow keys to move left and right.",1,[0,0,0],[255,255,255])
        self.screen.blit(text2,(230,370))
        






     
    
