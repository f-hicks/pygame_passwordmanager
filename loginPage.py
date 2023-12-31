import pygame
from customButton import customButton as button 
from customTextInput import customTextInput as textbox
import showAllPage
import main

def SubmitButtonCallback():
    with open("logincred.csv", "a") as f:
        f.write(f"{usernameTextArea.text},{passwordTextArea.text}\n")
    global run
    run = False

def ShowAllButtonCallback():
    surface = showAllPage.setup()
    showAllPage.main(surface)



def setup():
    pygame.init()

    win = pygame.display.set_mode((445,145))
    pygame.display.set_caption("Password Manager")
    return win

def main(surface):
    color_dark = (31,31,31)
    color_white = (255,255,255)
    buttonFont = pygame.font.SysFont(None, 24)

    global passwordTextArea # can't be bothered to pass it through several different functions
    global usernameTextArea

    usernameTextArea = textbox(
                    surface,
                    textBoxBackground = color_dark,
                    textBoxForeground = color_white,
                    text = "username",
                    textFont = buttonFont,
                    xCoord = 15,
                    yCoord = 15,
                    width = 200,
                    height = 50
                )
    
    passwordTextArea = textbox(
                    surface,
                    textBoxBackground = color_dark,
                    textBoxForeground = color_white,
                    text = "password",
                    textFont = buttonFont,
                    xCoord = 230,
                    yCoord = 15,
                    width = 200,
                    height = 50
                )

    buttonSubmit = button(
                    surface, 
                    buttonColor = color_dark, 
                    buttonTextColor = color_white, 
                    buttonText = "Login", 
                    buttonFont = buttonFont, 
                    xCoord = 15,
                    yCoord = 65+15,
                    width = 200,
                    height = 50,
                    onClick = SubmitButtonCallback
                )  
    buttonShowAll = button(
                    surface, 
                    buttonColor = color_dark, 
                    buttonTextColor = color_white, 
                    buttonText = "Show All", 
                    buttonFont = buttonFont, 
                    xCoord = 230,
                    yCoord = 65+15,
                    width = 200,
                    height = 50,
                    onClick = ShowAllButtonCallback
                ) 
    
    global run
    run = True
    while run:
        pygame.time.delay(100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            buttonSubmit.is_clicked(event)
            buttonShowAll.is_clicked(event)
            usernameTextArea.onEvent(event)
            passwordTextArea.onEvent(event)

if __name__ == "__main__":
    global surface
    surface = setup()
    main(surface)

pygame.quit()