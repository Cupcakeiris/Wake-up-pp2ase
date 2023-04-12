import pygame
from random import randint

class Student(pygame.sprite.Sprite):
    def __init__(self, x, y): # (x, y) - coordinates where student is sitting
        super().__init__()
        self.status = 'awake'

        self.image = pygame.image.load(r"assets\s1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.a = 5000 # energy looses every 5 seconds
        self.b = 10000 # every 10 seconds
        self.energy_speed = randint(self.a, self.b)
        self.energy = 100 
        # everyone has 100 % energy in the beginning

        self.next_time = 0
    
    def energy_drain(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.next_time and self.energy > 0:
            self.next_time += self.energy_speed
            self.energy -= 25 # everyone looses 25 % energy according to energy_speed
        
        if self.energy > 50: # changes student's sprite and status according to how many energy left
            self.set_awake()
            self.status = 'awake'
        elif self.energy > 0:
            self.set_half_sleepy()
            self.status = 'half_sleepy'
        else:
            self.set_asleep()
            self.status = 'asleep'
        print(f'energy: {self.energy}')
    
    def energy_reset(self):
        self.energy = 125
    
    def get_status(self):
        return self.status
    
    def set_awake(self):
        self.image = pygame.image.load(r"assets\s1.png")
    
    def set_half_sleepy(self):
        self.image = pygame.image.load(r"assets\s2.png")
    
    def set_asleep(self):
        self.image = pygame.image.load(r"assets\s3.png")