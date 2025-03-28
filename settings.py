import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
coins_count = 0
is_key = False

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("DINO_DINO")
pygame.display.set_icon(pygame.image.load("assets/images/player/move_left_5.png"))

clock = pygame.time.Clock()

""""ГРУПИ СПРАЙТІВ"""
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

"""КАРТИНКИ СПРАЙТІВ"""
bg = pygame.transform.scale(pygame.image.load("assets/background/bg1.jpg"), (W, H))
bg2 = pygame.transform.scale(pygame.image.load("assets/background/bg2.jpg"), (W, H))

platform_image = pygame.image.load("assets/background/platform.png")
platform_image2 = pygame.image.load("assets/background/platform2.png")

player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]
coin_image = pygame.image.load("assets/images/coin/coin1.png")
portal_image = pygame.image.load("assets/door/door1.png")
key_image = pygame.image.load("assets/key/key1.png")
box_image = pygame.image.load("assets/box/box1.png")
"""ШРИФТИ"""
pygame.font.init()
font1 = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.SysFont(None, 120, bold=True)


"""ТЕКСТИ"""
find_key_txt = font2.render("Знайди ключ", True, (102, 0, 0))
open_box_txt = font2.render("Натисни f, щоб відкрити", True, (102, 0, 0))
get_key_txt = font2.render("Натисни z, щоб підібрати", True, (102, 0, 0))
game_name = font3.render("Dinoss", True, (166, 67, 0))

"""МУЗИКА"""
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/music_fon.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

