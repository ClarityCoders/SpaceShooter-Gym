import math
import pygame
import random
from pygame import mixer


def hit (ojb1x, obj1y, obj2x, obj2y):
    dist = math.sqrt(math.pow(ojb1x-obj2x, 2)+math.pow(obj1y-obj2y, 2))
    if dist < 34:
        return True
    else:
        return False


def hit_pixel(object1, object2):

    offset = (int(object2.x - object1.x), int(object2.y - object1.y))
    point = object1.image_mask.overlap(object2.image_mask, offset)

    if point:
        return True
    return False


class EnemyWave():
    def __init__(self, count, spaceship):
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Enemy(self.enemy_list, spaceship))

    def check(self, screen, bullet, spaceship):
        score_tracker = 0
        for enemy in self.enemy_list:
            screen.blit(enemy.img, (int(enemy.x), int(enemy.y)))

            # Check for wall hit
            if enemy.x > 500 - enemy.img.get_rect().size[0] or enemy.x <= 0:
                # Flip direction
                enemy.velx *= -1  
                enemy.x += enemy.velx
                if enemy.x > 500:
                    enemy.x = 500
                elif enemy.x <= 0:
                    enemy.x = 0

            enemy.x += enemy.velx
            enemy.y += enemy.vely
            if enemy.y > 500:
                enemy.y = 0
                enemy.velx = random.randint(0,2)
                enemy.vely = .5
                #enemy.velx += .25
                #enemy.vely += .25
            if bullet.shoot:
                if hit_pixel(bullet, enemy):
                    bullet.shoot = False
                    score_tracker += 1
                    enemy.new_location(self.enemy_list, spaceship)
                    enemy.speed_up()
                bullet.move(screen)

            if hit_pixel(enemy, spaceship):
                return -1

        return score_tracker


class Enemy():
    img_list = [pygame.image.load("src/images/ufo.png"), 
                pygame.image.load("src/images/ufo20.png"),
                pygame.image.load("src/images/ufo40.png"),
                pygame.image.load("src/images/ufo60.png"),
                pygame.image.load("src/images/ufo80.png"),
                pygame.image.load("src/images/ufo100.png")]
    
    def __init__(self, enemy_list, spaceship):
        self.velx = random.randint(-2,2)
        self.vely = .5
        self.img = Enemy.img_list[0]
        self.image_index = 0
        self.image_mask = pygame.mask.from_surface(self.img)
        self.new_location(enemy_list, spaceship)

    def new_location(self, enemy_list, spaceship):
        new_spot = True
        while new_spot:
            new_spot = False
            self.x = random.randint(70, 500 - 70)
            self.y = random.randint(10, 150)
            for enemy in enemy_list:
                if self == enemy:
                    pass
                else:
                    #new_spot = hit(self.x, self.y, enemy.x, enemy.y)
                    if hit_pixel(self, enemy):
                        # If it hit something go back and start over
                        continue
            if hit_pixel(spaceship, self):
                continue
            else:
                break
        self.velx = random.randint(-2,2)

    def speed_up(self):
        if abs(self.velx) > 25:
            #self.vely += .5
            #self.velx += random.randint(0, 1)
            pass
        else:
            pass
            #self.velx += random.randint(1, 2)
            #self.vely += random.randint(0, 1)
        if self.image_index < len(self.img_list) - 1:
            self.image_index += 1
            self.img = self.img_list[self.image_index]
            self.image_mask = pygame.mask.from_surface(self.img)
