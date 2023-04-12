import pygame
from student import Student
pygame.init()

bounds = (640, 360)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Wake up, pp2ease!")
clock = pygame.time.Clock()
grid = pygame.image.load(r"assets/grid.png")
grid_rect = grid.get_rect()

BLUE = (70,130,180)
WHITE = (255,255,255)
BLACK = (0,0,0)

(st_x, st_y) = (100, 250)
(st_w, st_h) = (32, 32) # width and height of student sprite
S1 = Student(st_x, st_y)
# student_sprites = pygame.sprite.Group()
# student_sprites.add(S1)

(mouse_x, mouse_y) = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            # reset student's energy when clicked at asleep status
            if (mouse_x <= (st_x + st_w) and mouse_y <= (st_y + st_h) and mouse_x >= (st_x - st_w) and mouse_y >= (st_y - st_h)) and  Student.get_status(S1) == 'asleep':
                Student.energy_reset(S1)
                print(f'{mouse_x, mouse_y}')
    # window.blit(grid, grid_rect)
    window.fill(BLACK)
    window.blit(S1.image, S1.rect)

    Student.energy_drain(S1)
    

    pygame.display.update()
    clock.tick(60)