from pygame import *
import random

init()

width = 500
height = 500
window = display.set_mode((width, height))
display.set_caption("Snake")

screen = display.get_surface()
