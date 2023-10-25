import pygame
from customButton import customButton as button 
from customTextBox import customTextBox as textbox

def setup():
    pygame.init()

    win = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Password Manager")
    return win


def main(surface):
    color_dark = (31,31,31)
    color_white = (255,255,255)
    buttonFont = pygame.font.SysFont(None, 24)

    with open("logincred.csv","r") as f:
        y = 0
        for line in list(f.readlines())[1:]: # iterate through all the username and passwords, skipping the table row.
            username = line.split(',')[0]
            password = line.split(',')[1].strip('\n')
            textbox(
                surface,
                textBoxBackground = color_dark,
                textBoxForeground = color_white,
                text = f"{username}  |  {password}",
                textFont = buttonFont,
                xCoord = 0,
                yCoord = y,
                height = 50,
                width = 800
            )
            y += 65

    global run
    run = True
    while run:
        pygame.time.delay(100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    surface = setup()
    main(surface)

