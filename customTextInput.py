from pygame import font, Rect, draw, surface, init
import pygame

global allTextBoxes
allTextBoxes = []

init()
class customTextInput:
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
                 width: int = 50,
            ):
        
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
        allTextBoxes.append(self)
        return 

    def reDrawTextBox(self):
        self.box = draw.rect(self.surface, self.textBoxBackground, Rect((self.xCoord,self.yCoord),(self.width,self.height)))
        lines = self.wrap_text(self.text, self.textFont, self.width)
        y = self.yCoord
        for line in lines:
            text = self.textFont.render(line, True, self.textBoxForeground)
            self.surface.blit(text, (self.xCoord, y))
            y += text.get_height()   

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = [] 
        current_line = ''
        
        for word in words:
            test_line = current_line + word + ' '
            test_size = font.size(test_line)
            
            if test_size[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

        if current_line:
            lines.append(current_line)
        
        return lines

    def onEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.box.collidepoint(event.pos): # check if mouse pos collides with button
                if self.text == self.originaltext:
                    self.text = ""
                self.selected = True

                for textbox in allTextBoxes: # disable input for all the other text boxes
                    if textbox != self:
                        textbox.selected = False
        elif self.selected:
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_RETURN:
                    self.selected = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.reDrawTextBox()

        


