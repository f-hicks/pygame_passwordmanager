import pygame
from customButton import customButton as button 
from customButton import customButton
import loginPage

def LoginButtonCallback():
    surface = loginPage.setup()
    loginPage.main(surface)
    surface = setup()
    main(surface)

def QuitButtonCallback():
    print("Exiting")
    pygame.quit()
    exit(0)

def setup():
    pygame.init()

    win = pygame.display.set_mode((415,50))
    pygame.display.set_caption("Password Manager")
    pygame.display.set_icon(pygame.image.load("imageicon.png"))
    return win

def main(surface):
    color_dark = (31,31,31)
    color_white = (255,255,255)
    #pygame.draw.rect(surface, color_dark, [590, 315, 80 , 30])
    buttonFont = pygame.font.SysFont(None, 24)
    buttonLogin: customButton = button(
                    surface, 
                    buttonColor = color_dark, 
                    buttonTextColor = color_white, 
                    buttonText = "Login", 
                    buttonFont = buttonFont, 
                    xCoord = 0,
                    yCoord = 0,
                    width = 200,
                    height = 50,
                    onClick = LoginButtonCallback
                    )  
    
    buttonQuit: customButton = button(
                    surface, 
                    buttonColor = color_dark, 
                    buttonTextColor = color_white, 
                    buttonText = "Quit", 
                    buttonFont = buttonFont, 
                    xCoord = 215,
                    yCoord = 0,
                    width = 200,
                    height = 50,
                    onClick = QuitButtonCallback
                    )  

    run = True

    while run:
        pygame.time.delay(100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            buttonLogin.is_clicked(event)
            buttonQuit.is_clicked(event)


if __name__ == "__main__":
    win = setup()
    main(win)
    
pygame.quit()