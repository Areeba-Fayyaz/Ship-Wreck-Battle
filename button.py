import pygame
pygame.init()
class button:
    '''This is a class for making button'''

    def __init__(self,x1,y1,w,h,t,sc,c=[255,0,0],f=60,fs='comicsans',wd_outline=10,change_c=[0,0,255]):
        '''class constructor
        Parameters:
        x1(int or float): x position of button
        y1(int or float): y position of button
        w(int or float): width of the button
        h(int or float): height of the button
        t(str): text on the button
        sc: screen on which the button is displayed
        c: color of the  button
        f(int or float): font size  of the text on the button
        fs(str): font style of the text on the button
        wd_outline(str or float): width of the button's outline
        change_c: color of the button when cursor is on the button'''
        
        self.x=x1
        self.y=y1
        self.width=w
        self.height=h
        self.text=t
        self.Screen=sc
        self.color=c
        self.ch_color=change_c
        self.fontsize=f
        self.fontstyle=fs
        self.width_of_outline=wd_outline
        
    def drawbutton(self):
        '''This function draw button in ellipse shape'''
        self.RED=[255,0,0]
        self.BLACK=[0,0,0]
        self.BLUE=[0,0,255]
        pygame.draw.ellipse(self.Screen,self.color,[self.x,self.y,self.width,self.height])
        self.outline()
        self.write_text()
        
    def drawsqbutton(self):
        '''This function draw button in square shape'''
        pygame.draw.rect(self.Screen,self.color,[self.x,self.y,self.width,self.height])
        self.sq_outline()
        self.write_text()
        
    def sq_outline(self):
        '''for making button prettier this  function makes square
        button's outline'''
        pygame.draw.rect(self.Screen,[0,0,0],[self.x,self.y,self.width,self.height],self.width_of_outline)

    def outline(self):
        '''for making button prettier this  function makes ellipse
        button's outline'''
        pygame.draw.ellipse(self.Screen,self.BLACK,[self.x,self.y,self.width,self.height],self.width_of_outline)

    def write_text(self):
        '''It writes text on the button'''
        font=pygame.font.SysFont(self.fontstyle,self.fontsize)
        Text=font.render(self.text,1,(0,0,0))
        self.Screen.blit(Text,(self.x+(self.width/2-Text.get_width()/2),self.y+(self.height/2-Text.get_height()/2)))

    def isOver(self, pos):
        '''this function checks whether the position of cursor is
        outside the button(returns False) or on the button(returns True).
        Parameters:
        pos: pos is the mouse position or a tuple of (x,y) coordinates'''
        
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.height:
                return True
        return False
    
    def changesqcolor(self):
        '''it changes the color of the square button'''
        self.color=self.ch_color
        self.drawsqbutton()
        
    def changecolor(self):
        '''it changes the color of the ellipse shape button'''
        self.color=self.ch_color
        self.drawbutton()
       
