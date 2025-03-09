from settings import*


class MapObject(pygame.sprite.Sprite): #клас обєктів мапи
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(pygame.sprite.Sprite): #клас для всіх спрайтів
    def __init__(self, x, y, width, height, speed, images):
        super().__init__()
        self.width = width
        self.height = height
        self.images = images #список з картінками
        self.anim_count = 0 #номеранімації
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite): #клас для гравця
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)

        self.action = "idle" #поточня дія гравця  
        self.animations = {   # всі номери анімацій в залежності від дій
            'idle': list(range(4)),
            'right': list(range(4, 10)),
            'left': list(range(10, 17))
        }

        self.is_jump = False
        self.jump_count = 20

        self.fall = 0
        self.graviti = 2
        self.on_ground = False

    def update(self, platforms): #оновлення гравця
        print(self.is_jump)
        frames = self.animations[self.action] #номери анімацій гравця в залежності від дій
        self.anim_count += 1 #перемикаємо анімацію
        if self.anim_count >= len(frames) - 1:
            self.anim_count = 0 #обнуляємо номер анімації коли вони закінчились
        self.image = pygame.transform.scale(self.images[frames[self.anim_count]], (self.width, self.height))

        self.fall += self.graviti
        self.rect.y += self.fall
        hit_platforms = pygame.sprite.spritecollide(self, platforms, False)
        if hit_platforms:
            for platform in hit_platforms:
                if self.fall > 0 and self.rect.bottom > platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.fall = 0
                    self.on_ground = True
        else:
            self.on_ground = False


        keys_presed = pygame.key.get_pressed() 
        if keys_presed[pygame.K_a]: #рух в ліво
            self.action = "left"
            self.rect.x -= self.speed
        elif keys_presed[pygame.K_d]: #рух в право
            self.action = "right"
            self.rect.x += self.speed
        else:
            self.action = "idle" #без руху
       
        if not self.is_jump:
            if keys_presed[pygame.K_SPACE]:
                if self.on_ground:
                    self.is_jump = True
                    self.fall -= self.jump_count
        else:
            self.is_jump = not self.on_ground

                


