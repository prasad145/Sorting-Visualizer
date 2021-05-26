import pygame
import sys
from pygame import display


pygame.init()

disp = pygame.display.set_mode((500, 400))



x = 40
y = 40

bar_width = 20
bar_height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

def draw_bars(h):
    for i in range(len(h)):
        pygame.draw.rect(disp, (0, 0, 255), pygame.Rect(x + (30 * i), y, bar_width, bar_height[i]))
        
ok = True

while ok:
    run = False
    pygame.time.delay(10)

    any_key_get_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False #close pygame window

    # if any_key_get_pressed[pygame.K_SPACE]:
    if sys.argv[1] != "":
        run = True

    if run == False:
        disp.fill((0, 0, 0))
        draw_bars(bar_height)
        pygame.display.update()
    #algorithm for bubble sort
    elif sys.argv[1].lower() == "bubblesort":
        pygame.display.set_caption("Bubble Sort")
        for i in range(len(bar_height) - 1):
            vis = False
            for j in range(len(bar_height) - i - 1):
                if bar_height[j] > bar_height[j + 1]:
                    tmp = bar_height[j]
                    bar_height[j] = bar_height[j + 1]
                    bar_height[j + 1] = tmp
                    vis = True 

                disp.fill((0, 0, 0))
                draw_bars(bar_height)
                pygame.time.delay(20)
                pygame.display.update()
            if not vis:
                break
    elif sys.argv[1].lower() == "selctionsort":
        #selection sort here


        disp.fill((0, 0, 0))
        draw_bars(bar_height)
        pygame.time.delay(10)
        pygame.display.update()
    elif sys.argv[1].lower() == "insertionsort":
        #insertion sort here
        
        
        disp.fill((0, 0, 0))
        draw_bars(bar_height)
        pygame.time.delay(10)
        pygame.display.update()
    elif sys.argv[1].lower() == "quicksort":
        #quicksort


        disp.fill((0, 0, 0))
        draw_bars(bar_height)
        pygame.time.delay(10)
        pygame.display.update()
    elif sys.argv[1].lower() == "mergesort":
        #mergesort


        disp.fill((0, 0, 0))
        draw_bars(bar_height)
        pygame.time.delay(10)
        pygame.display.update()

pygame.quit()




