import pygame
import random
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
start = False
dt = 0
target_size = 5
target_2_size = 3
score = 0
miss = 0
time = 10
headshot_timer = 0

center = (int(screen.get_width() / 2), int(screen.get_height() / 2))
target_pos = center

target_2_pos = center

pygame.display.set_caption("Aim Sim")

font = pygame.font.Font("freesansbold.ttf", 40)


miss_text = font.render(f"Missed: {miss}", True, (110, 0, 0))
score_txt = font.render(f"Score: {score}", True, (0, 110, 0))
time_txt = font.render(f"{time:.2f}", True, (110, 110, 0))

hs_text = font.render(f"HEADSHOT", True, (2, 110, 110))

score_rect = score_txt.get_rect()
score_rect.center = (105, 40)

time_rect = time_txt.get_rect()
time_rect.center = (1000, 40)

miss_rect = miss_text.get_rect()
miss_rect.center = (500, 40)

hs_rect = hs_text.get_rect()
hs_rect.center = (int(screen.get_width() / 2), 100)
while running:
    screen.fill("gray")
    # if time >= 0:
    random_cords = (random.randint(0, screen.get_width() - 80) + 40, random.randint(80, screen.get_height() - 80) + 40)

    if target_size < 40:
        target_size+= 0.4


    pygame.draw.circle(screen, "black", target_pos, target_size)
    pygame.draw.circle(screen, "red", target_pos, 5)
    if score > 4:
        pygame.draw.circle(screen, "red", target_2_pos, target_2_size)
    
        if target_2_size < 20:
            target_2_size+= 0.4

    screen.blit(time_txt, time_rect)
    screen.blit(score_txt, score_rect)
    screen.blit(miss_text, miss_rect)

    miss_text = font.render(f"Missed: {miss}", True, (110, 0, 0))
    score_txt = font.render(f"Score: {score}", True, (0, 110, 0))
    time_txt = font.render(f"{time:.2f}", True, (110, 110, 0))

    
    if headshot_timer:
        screen.blit(hs_text, hs_rect)
        hs_text.set_alpha(255 - 255 / headshot_timer)
        headshot_timer-= 1

    if start:
        time-= dt

    
    # else:
    #     screen.blit(score_txt, center)
    #     score_txt = font.render(f"Score: {score}", True, (0, 110, 0))
    #     start = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and time <=0:
        score = 0
        time = 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                dx1 = mouse_x - target_pos[0]
                dy1 = mouse_y - target_pos[1]
                dx2 = mouse_x - target_2_pos[0]
                dy2 = mouse_y - target_2_pos[1]
                distance1 = math.hypot(dx1, dy1)
                distance2 = math.hypot(dx2, dy2)
                if distance1 < target_size:
                    start = True
                    score+=1
                    if distance1 < 8:
                        score+= 9
                        headshot_timer = 35
                    target_pos = random_cords
                    target_size = 5
                elif distance2 < target_2_size:
                    score+=5
                    target_2_pos = random_cords
                    target_2_size = 5
                else:
                    miss += 1
                    


  

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()