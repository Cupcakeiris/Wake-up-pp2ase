import pygame
from student import Student

pygame.init()


bounds = (1280, 720)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Wake up, pp2ease!")
clock = pygame.time.Clock()
grid = pygame.image.load(r"assets/grid.png")
grid_rect = grid.get_rect()
bubble_text = pygame.image.load(r"assets/bubble.png")

font = pygame.font.Font(r"assets\dogicapixel.ttf")


BLUE = (70,130,180)
WHITE = (255,255,255)
BLACK = (0,0,0)

(st_x, st_y) = (100, 300)
(st2_x, st2_y) = (600, 300)
temp = (st_x, st_y)
temp2 = (st2_x, st2_y)
(st_w, st_h) = (32, 32) # width and height of student sprite

student_sprites = pygame.sprite.Group()
awake_set = set(())

for i in range(4):
    for j in range(6):
        temp = (temp[0] + 70, temp[1])
        id = '0' + str(i) + str(j)
        student_sprites.add(Student(temp[0], temp[1], int(id)))
        awake_set.add(int(id))
    temp = (st_x, temp[1] + 100)

for i in range(4):
    for j in range(6):
        temp2 = (temp2[0] + 70, temp2[1])
        id = '1' + str(i) + str(j)
        student_sprites.add(Student(temp2[0], temp2[1], int(id)))
        awake_set.add(int(id))
    temp2 = (st2_x, temp2[1] + 100)


(mouse_x, mouse_y) = pygame.mouse.get_pos()

next_level = pygame.USEREVENT + 1

pygame.time.set_timer(next_level, 5000)


while True:

    

    (b_x, b_y) = (1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == next_level:
            for entity in student_sprites:
                Student.change_speed(entity)
                print(entity.a, entity.b)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            for entity in student_sprites:
                Student.click_event(entity, mouse_x, mouse_y)
                (b_x, b_y) = (50, 50)
        
            

    # window.blit(grid, grid_rect)
    window.fill(BLACK)
    window.blit(bubble_text, (b_x, b_y))

    # window.blit(bubble_text, (100,100))
    for entity in student_sprites:
        window.blit(entity.image, entity.rect)
        Student.energy_drain(entity)
        if entity.status == 'asleep' and entity.id in awake_set:
            awake_set.remove(entity.id)
        elif entity.status == 'awake' and entity.id not in awake_set:
            awake_set.add(entity.id)
    
    print(len(awake_set))

    pygame.display.update()
    clock.tick(60)