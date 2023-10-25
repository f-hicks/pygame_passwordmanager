from pygame import font, Rect, draw, surface, init
import pygame

init()
class customButton:
    def __init__(
                 self, 
                 winSurface: surface, 
                 buttonColor: tuple = (255,255,255), 
                 buttonTextColor: tuple = (0,0,0), 
                 buttonText: str = "", 
                 buttonFont: font = font.SysFont(None, 24), 
                 xCoord: int = 0, 
                 yCoord: int = 0, 
                 height: int = 50, 
                 width: int = 50,
                 onClick = None
            ):
        self.surface: surface = winSurface
        self.buttonColor: tuple = buttonColor
        self.buttonTextColor: tuple = buttonTextColor
        self.buttonText: str = buttonText
        self.buttonFont: font = buttonFont
        self.xCoord: int = xCoord
        self.yCoord: int = yCoord
        self.width: int = width
        self.height: int = height
        self.onClick = onClick
        self.reDrawButton()
        return 

    def reDrawButton(self):
        self.button = draw.rect(self.surface, self.buttonColor, Rect((self.xCoord,self.yCoord),(self.width,self.height)))
        self.text = self.buttonFont.render(self.buttonText , True , self.buttonTextColor)
        self.surface.blit(self.text, (self.xCoord, self.yCoord))


    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.collidepoint(event.pos): # check if mouse pos collides with button
                try:
                    self.onClick()
                except TypeError:
                    pass
        
        return False


