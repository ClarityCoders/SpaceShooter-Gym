import pygame
from pygame import mixer


class Bullet():

    def __init__(self):
        self.x = 250
        self.y = -100
        self.shoot = False
        self.img = pygame.image.load("src/images/laser.png")
        self.image_mask = pygame.mask.from_surface(self.img)


    def sound(self):
        pass
        # self.laser.play()

    def check_move(self, event, ship_x, ship_y):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not self.shoot:
                    self.sound()
                    self.x = ship_x + 32 - (self.img.get_rect().size[0] / 2 )
                    self.y = ship_y - self.img.get_rect().size[1]
                    self.shoot = True

    def move(self, screen):
        if self.y < 0:
            self.shoot = False
            self.y = -100
        else:
            self.y -= 3
            #screen.blit(self.img, (self.x, self.y))

    def show(self, screen):
        if self.shoot:
            screen.blit(self.img, (self.x, self.y))
