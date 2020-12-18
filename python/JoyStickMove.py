import pygame, sys
from pygame.constants import QUIT
pygame.init()
screen = pygame.display.set_mode((640, 240))
pyjoy = pygame.joystick.Joystick(0)
pyjoy.init()
posx=posy=100
WHITE = (255, 255, 255)
circle=pygame.image.load('ocircle.bmp')

while True:
  screen.fill(WHITE)
  screen.blit(circle,(posx, posy))
  pygame.display.update()

  for event in pygame.event.get():
          print(event)

          if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

          if pyjoy.get_axis(0) > .1:
            posx += 10
          if pyjoy.get_axis(0) < -.1:
            posx -= 10
          if pyjoy.get_axis(1) > .1:
            posy += 10
          if pyjoy.get_axis(1) < -.1:
            posy -= 10


    