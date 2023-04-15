import pygame
import time 
from student import Student

pygame.init()

# basic initialization
bounds = (1280, 720)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Wake up, pp2ease!")
clock = pygame.time.Clock()
grid = pygame.image.load(r"assets/Bg.png")
grid_rect = grid.get_rect()
font = pygame.font.Font(r"assets/dogica.ttf", 18)
lecture_failed = pygame.image.load(r"assets/fail.png")
lecture_succeed = pygame.image.load(r"assets/succeed.png")

BLUE = (70,130,180)
WHITE = (255,255,255)
BLACK = (0,0,0)

(st_x, st_y) = (120, 340) # starting point of 1st student in 1st half
(st2_x, st2_y) = (670, 340) # starting point of 1st student in 2nd half
temp = (st_x, st_y)
temp2 = (st2_x, st2_y)
(st_w, st_h) = (32, 32) # width and height of student sprite

student_sprites = pygame.sprite.Group()
awake_set = set(()) # stores all awake and half-asleep student's ids
        


for i in range(4): # putting 24 student on left side
    for j in range(6):
        temp = (temp[0] + 70, temp[1]) # student's every right neighbor is located 70px away
        id = '0' + str(i) + str(j)
        student_sprites.add(Student(temp[0], temp[1], int(id)))
        awake_set.add(int(id))
    temp = (st_x, temp[1] + 80) # and located 80 px below

for i in range(4): # second half on right
    for j in range(6):
        temp2 = (temp2[0] + 70, temp2[1])
        id = '1' + str(i) + str(j)
        student_sprites.add(Student(temp2[0], temp2[1], int(id)))
        awake_set.add(int(id))
    temp2 = (st2_x, temp2[1] + 80)


(mouse_x, mouse_y) = pygame.mouse.get_pos()
inc_speed = pygame.USEREVENT + 1
level = 1
pygame.time.set_timer(inc_speed, 20000)

T = pygame.time.get_ticks() # pygame's time continues moving on from pygame.init()
while True:
    window.blit(grid, grid_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == inc_speed:
            for entity in student_sprites:
                Student.change_speed(entity)
                print(entity.a, entity.b)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            for entity in student_sprites:
                Student.click_event(entity, mouse_x, mouse_y)
        
    # basic text
    sleeping_number = font.render(f'sleeping: {len(student_sprites) - len(awake_set)}', True, BLACK)
    level_number = font.render(f'level:{level}', True, BLACK)
    time_ellapsed = font.render(f'time: {(pygame.time.get_ticks() - T)//1000}', True, BLACK)
    window.blit(sleeping_number, (540,100))        
    window.blit(level_number, (540, 140))
    window.blit(time_ellapsed, (540, 180))
    # window.blit(bubble_text, (100,100))

    # adds/removes from awake_set according to the status of student
    for entity in student_sprites:
        window.blit(entity.image, entity.rect)
        Student.energy_drain(entity)
        if entity.status == 'asleep' and entity.id in awake_set:
            awake_set.remove(entity.id)
        elif entity.status == 'awake' and entity.id not in awake_set:
            awake_set.add(entity.id)
    

    if 48 - len(awake_set) > 24:
        window.fill((0,0,0))
        window.blit(lecture_failed, (0,0))
        pygame.display.update()
        time.sleep(3)
        for entity in student_sprites:
            entity.energy = 125
            entity.a = 9000
            entity.b = 27000
        T = pygame.time.get_ticks() # we have to substract from moving on time the time we lost to restart from 0

    pygame.display.update()
    clock.tick(30)