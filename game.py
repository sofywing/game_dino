import pygame
from odjects import*
from levels import*

pygame.init()

level1_objects, key, box = draw_level(level1)

player = Player(50, H-90, 40, 50, 10, player_images)
door = MapObject(-300, -300, 50, 70, portal_image)

level1_objects.add(player)
level1_objects.add(door)

"""КНОПКИ ДЛЯ МЕНЮ"""
btn_play = Button(470, 250, 350, 100, (204, 102, 0), "PLAY", 60, (0, 0, 0))
btn_instructions = Button(470, 400, 350, 100, (204, 102, 0), "INSTRUCTIONS", 60, (0, 0, 0))
btn_back = Button(470, 550, 350, 100, (204, 102, 0), "BACK TO", 60, (0, 0, 0))
btn_exit = Button(470, 550, 350, 100, (204, 102, 0), "EXIT", 60, (0, 0, 0))

mode = "menu"

game = True
finish = False
while game:
    key_pressed = pygame.key.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if mode == "menu":
        window.blit(bg, (0, 0))
        window.blit(game_name, (500, 50))

        btn_play.draw(120, 30)
        btn_instructions.draw(15, 30)
        btn_exit.draw(120, 40)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if btn_play.rect.collidepoint(x, y):
                    mode = game
    if mode == "game":
        if not finish:
            window.blit(bg, (0, 0))
            for obj in level1_objects:
                window.blit(obj.image, camera.apply(obj))
            camera.update(player)
            
            player.update(platforms)

            if pygame.sprite.spritecollide(player, coins, True):
                coins_count += 1
            
            window.blit(pygame.transform.scale(coin_image, (50, 50)), (10, 10))
            coins_txt = font1.render(f":{coins_count}", True, (128,0,0))
            window.blit(coins_txt, (60, 12))

            if pygame.sprite.collide_rect(player, key):
                window.blit(get_key_txt, (W//2 - 400, 50))
                if key_pressed[pygame.K_z]:
                    is_key = True
                    key.rect.x = -200
            if pygame.sprite.collide_rect(player, box) and is_key:
                window.blit(open_box_txt, (W//2 - 400, 50))
                if key_pressed[pygame.K_f]:
                    coins_count += 20
                    box.rect.x = -300
                    
            if pygame.sprite.collide_rect(player,box) and not is_key:
                window.blit(find_key_txt, (W//2 - 400, 50))
                
            if door:
                if coins_count > 1:
                    door.rect.x = 1000
                    door.rect.y = 500

                if pygame.sprite.collide_rect(player, door):
                    for obj in level1_objects:
                        obj.kill()
                    for platform in platforms:
                        platform.kill()

                    del door
                    door = None
                    level1_objects, key, boox = draw_level(level2)
                    player.rect.x = 50
                    player.rect.y = H - 90
                    level1_objects.add(player)

        if player.rect.y > 800:
            finish = True


    pygame.display.update()
    clock.tick(FPS)
