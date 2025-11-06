import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 1080))
clock = pygame.time.Clock()
running = True

screen.fill("red")

pygame.display.flip()