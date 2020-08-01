import pygame


class Spaceship():
    def __init__(self):
        self.vel = 9
        self.x = 250
        self.y = 400
        self.move_x = 0
        self.move_y = 0
        self.img = pygame.image.load("src/images/spaceship.png")
        self.image_mask = pygame.mask.from_surface(self.img)

    def check_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.vel
            if event.key == pygame.K_RIGHT:
                self.move_x += self.vel
            if event.key == pygame.K_UP:
                self.move_y -= self.vel
            if event.key == pygame.K_DOWN:
                self.move_y += self.vel
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.move_x = 0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                self.move_y = 0

    def move(self, screen):
        width_bound = 500 - self.img.get_rect().size[0]
        height_bound = 500 - self.img.get_rect().size[1]

        if self.x + self.move_x < width_bound and self.x + self.move_x > 0:
            self.x += self.move_x
        if self.y + self.move_y < height_bound and self.y + self.move_y > 0:
            self.y += self.move_y
    
    def show(self, screen):
        screen.blit(self.img, (int(self.x),int(self.y)))