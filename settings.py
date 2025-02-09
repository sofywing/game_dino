import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("DINO_DINO")
pygame.display.set_icon(pygame.image.load("assets/images/player/move_left_5.png"))

clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("assets/background/level1.png"), (W, H))

platform_image = pygame.image.load("assets/background/platform.png")
