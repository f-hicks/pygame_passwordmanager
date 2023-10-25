import pygame
from customButton import customButton as button 
from customTextInput import customTextInput as textbox

def SubmitButtonCallback():
    print("Submitted")
    print(f"Username = {usernameTextArea.text}")
    print(f"Password = {passwordTextArea.text}")
    with open("logincred.csv", "a") as f:
        f.write(f"{usernameTextArea.text},{passwordTextArea.text}\n")
    exit(0)



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
                    xCoord = ((415/2)-200/2)+15,
                    yCoord = 65+15,
                    width = 200,
                    height = 50,
                    onClick = SubmitButtonCallback
                )  
    run = True

    while run:
        pygame.time.delay(100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            buttonSubmit.is_clicked(event)
            usernameTextArea.onEvent(event)
            passwordTextArea.onEvent(event)

if __name__ == "__main__":
    surface = setup()
    main(surface)

pygame.quit()