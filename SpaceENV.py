import numpy as np
import gym
from gym import spaces
import pygame
from pygame import display, time, init
from pygame.event import pump
from pygame.surfarray import array3d
from src.Spaceship import Spaceship
from src.Bullet import Bullet
from src.Enemy import EnemyWave
import cv2


class SpaceENV(gym.Env):

  """
  Custom Environment that follows gym interface.
  Space game with random enemies. 
  """

  def __init__(self):
    pygame.init()
    super(SpaceENV, self).__init__()

    self.fps = 300
    self.fps_clock = time.Clock()
    self.WIDTH = 500
    self.HEIGHT = 500
    base_y = 500
    self.history = []
    for i in range(0, 6):
      self.history.append(np.zeros((84, 84)))
    

    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    display.set_caption('SpaceShooter Learning')
    self.screen.fill((0, 0, 0))
    n_actions = 18
    self.action_space = spaces.Discrete(n_actions)
    self.observation_space = spaces.Box(low=0, high=255, shape=(252, 84, 1), dtype=np.uint8)

  def reset(self):
    self.history_frame = np.zeros((84, 84))
    self.history_frame2 = np.zeros((84, 84))
    self.screen.fill((0, 0, 0))
    self.spaceship = Spaceship()
    self.bullet = Bullet()
    self.enemy_wave = EnemyWave(5, self.spaceship)
    self.score = 0
    image = self.pre_processing(array3d(display.get_surface()))
    #print(image.shape)
    return image

  def step(self, action):
    scoreholder = self.score
    self.screen.fill((0, 0, 0))

    pump()
    reward = -0.001
    done = False

    if action == 2 or action == 6 or action == 10 or action == 11 or action == 14 or action == 15:
        self.spaceship.move_y -= self.spaceship.vel
    if action == 3 or action == 7 or action == 12 or action == 13 or action == 16 or action == 17:
        self.spaceship.move_y += self.spaceship.vel
    if action == 5 or action == 9 or action == 11 or action == 13 or action == 15 or action == 17:
        self.spaceship.move_x -= self.spaceship.vel
    if action == 4 or action == 8 or action ==10 or action == 12 or action == 14 or action == 16:
        self.spaceship.move_x += self.spaceship.vel
    # Actions that fire bullet.
    if action == 1 or action == 6 or action == 7 or action == 8 or action == 9 or action == 14 or action == 15 or action == 16 or action == 17:
        if self.bullet.shoot == False:
            self.bullet.x = self.spaceship.x + 32 - (self.bullet.img.get_rect().size[0] / 2 )
            self.bullet.y = self.spaceship.y - self.bullet.img.get_rect().size[1]
            self.bullet.shoot = True
            reward -= 0.001
        
    self.spaceship.move(self.screen)
    self.spaceship.move_x = 0
    self.spaceship.move_y = 0

    result = self.enemy_wave.check(self.screen, self.bullet, self.spaceship)
    if result >= 0:
        reward += result
        self.score += result
    else:
        done = True
        reward = -2
        self.__init__()

    self.bullet.show(self.screen)
    self.spaceship.show(self.screen)
    image = array3d(display.get_surface())
    info = {'score': scoreholder}
    self.fps_clock.tick(self.fps)
    display.update()
    return self.pre_processing(image), reward, done, info

  def render(self):

    # Show score
    font = pygame.font.SysFont("comicsans", 40)
    showscore = font.render(f"Score: {self.score}", True, (255, 255, 255))
    self.screen.blit(showscore, (self.WIDTH - 10 - showscore.get_width(), 10))  

    # Update display
    display.update()

  def close(self):
    pass

  def pre_processing(self, image):
    image = cv2.cvtColor(cv2.resize(image, (84, 84)), cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
    #image = image[ :, :, None].astype(np.float32)
    #_, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
    image = image / 255
    
    del self.history[0]
    self.history.append(image)
    #print(type(image))
    #print(image.shape)
    image = np.concatenate((self.history[-5], self.history[-3], image), axis=0)
    #print(image.shape)
    image = np.expand_dims(image, axis=-1)
    #print(image.shape)
    return image