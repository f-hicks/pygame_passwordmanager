from pygame import font, Rect, draw, surface, init
import pygame

class customTextBox:
    def __init__(
                self, 
                winSurface: surface, 
                textBoxBackground: tuple = (255,255,255), 
                textBoxForeground: tuple = (0,0,0), 
                text: str = "", 
                textFont: font = font.SysFont(None, 24), 
                xCoord: int = 0, 
                yCoord: int = 0, 
                height: int = 50, 
                width: int = 50,) -> None:
        
        self.surface: surface = winSurface
        self.textBoxBackground: tuple = textBoxBackground
        self.textBoxForeground: tuple = textBoxForeground
        self.text: str = text
        self.originaltext: str = text
        self.textFont: font = textFont
        self.xCoord: int = xCoord
        self.yCoord: int = yCoord
        self.width: int = width
        self.height: int = height
        self.selected: bool = False
        self.reDrawTextBox()
        return 
    
    def reDrawTextBox(self):
        self.box = draw.rect(self.surface, self.textBoxBackground, Rect((self.xCoord,self.yCoord),(self.width,self.height)))
        text = self.textFont.render(self.text, True, self.textBoxForeground)
        self.surface.blit(text, (self.xCoord, self.yCoord))

    