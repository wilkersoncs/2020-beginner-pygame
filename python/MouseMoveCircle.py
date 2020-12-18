import pygame, sys
from pygame.constants import QUIT
pygame.init()
screen = pygame.display.set_mode((640, 240))
posx=100
posy=100
circle=pygame.image.load('ocircle.bmp')

while True:
  screen.blit(circle,(posx, posy))
  pygame.display.update()
  posx=pygame.mouse.get_pos()[0]
  posy=pygame.mouse.get_pos()[1]

  for event in pygame.event.get():
          print(event)

          if event.type == QUIT:
            pygame.quit()
            sys.exit(0)



    