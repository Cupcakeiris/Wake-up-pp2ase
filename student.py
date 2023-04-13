import pygame
from random import randint
pygame.init()

fx = pygame.mixer.Sound(r"assets/fx.mp3")

class Student(pygame.sprite.Sprite):
    def __init__(self, x, y, id): # (x, y) - coordinates where student is sitting
        super().__init__()
        self.status = 'awake'
        self.id = id
        self.image = pygame.image.load(r"assets\s1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32

        self.a = 2000 # energy looses every 5 seconds
        self.b = 5000 # every 10 seconds
        self.energy_speed = randint(self.a, self.b)
        self.energy = 125 
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
        # print(f'energy: {self.energy}')

    def click_event(self, m_x, m_y):
            # reset student's energy when clicked at asleep status
        if (m_x <= (self.x + self.w) and m_y <= (self.y + self.h) and m_x >= (self.x - self.w) and m_y >= (self.y - self.h)) and self.status == 'asleep':
            self.energy = 125
            print(f'{m_x, m_y}')
            fx.play()
        

            
        
    def get_status(self):
        return self.status
    def get_id(self):
        return self.id
    
    def change_speed(self):
        if self.a > 0 and self.b > 0:
            self.a -= 500
            self.b -=500

    def set_awake(self):
        self.image = pygame.image.load(r"assets\s1.png")
    
    def set_half_sleepy(self):
        self.image = pygame.image.load(r"assets\s2.png")
    
    def set_asleep(self):
        self.image = pygame.image.load(r"assets\s3.png")