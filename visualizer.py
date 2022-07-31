import random
import pygame
import sys 
from pygame import Color, display

pygame.init()

disp = pygame.display.set_mode((700, 400))

x = 40
y = 40

bar_width = 20
bar_height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20, 210, 39, 48, 56, 18, 240, 95]
colors = ['#bcbcbc' ,'#a9dcd6' ,'#260566' ,'#caf0be' ,'#ffd358' ,'#f4a201','#b536f0' ,'#ffba42' ,'#a9dcd6' ,'#c39797' ,'#ff7f50' ,'#acb843' ,'#f9dada' ,'#f6b4be' ,'#ee9b9b','#0a6fd3' ,'#693a7c' ,'#b5b4e5' ,'#abeeaa','#483d8b' ,'#3a95cb']
def draw_bars(h):
    for i in range(len(h)):
        pygame.draw.rect(disp, colors[i], pygame.Rect(x + (30 * i), y, bar_width, bar_height[i]))
        
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
                pygame.time.delay(100)
                pygame.display.update()
            if not vis:
                break     
    elif sys.argv[1].lower() == "selectionsort":
        #selection sort here
        pygame.display.set_caption("Selection Sort")
        for i in range(len(bar_height)):
            minNum = i
            for j in range(i+1,len(bar_height)):
                if bar_height[minNum] > bar_height[j]:
                    minNum = j
                    bar_height[i],bar_height[minNum] = bar_height[minNum],bar_height[i]
                    disp.fill((0, 0, 0))
                    draw_bars(bar_height)
                    pygame.time.delay(100)
                    pygame.display.update()
                
    elif sys.argv[1].lower() == "insertionsort":
        #insertion sort here
        pygame.display.set_caption("Insertion Sort")
        for i in range(1,len(bar_height)):
            key = bar_height[i]
            j = i - 1
            while j >=0 and key < bar_height[j]:
                bar_height[j+1] = bar_height[j]
                j -= 1
                disp.fill((0, 0, 0))
                draw_bars(bar_height)
                pygame.time.delay(100)
                pygame.display.update()
            bar_height[j+1] = key        
            disp.fill((0, 0, 0))
            draw_bars(bar_height)
            pygame.time.delay(10)
            pygame.display.update()

    elif sys.argv[1].lower() == "quicksort":
        #quicksort
        pygame.display.set_caption("Quick Sort")
        def partition(arr, l, r):
            # partition function is to bring all the elemets less the pivot to the left and greater than pivot to the right
            i = l - 1
            pivot = arr[r]

            for j in range(l, r):
                if(arr[j] < pivot):
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i] #swap index i and j 
            arr[i + 1], arr[r] = arr[r], arr[i + 1]
            disp.fill((0, 0, 0))
            draw_bars(bar_height)
            pygame.time.delay(400)
            pygame.display.update()
            return i + 1
        
        def partitionRandom(arr, l, r):
            if(l < r):
                randomIndex = random.randrange(l, r)
                arr[r], arr[randomIndex] = arr[randomIndex], arr[r]
                return partition(arr, l, r)

        def quickSort(arr, l, r):
                if r == 0:
                    return arr
                if(l < r):
                    pi = partitionRandom(arr, l, r) #partion index
                    quickSort(arr, l, pi - 1)
                    quickSort(arr, pi + 1, r)
        #calling quick sort method
        quickSort(bar_height, 0, len(bar_height) - 1)
    elif sys.argv[1].lower() == "mergesort":
        #mergesort
        pygame.display.set_caption("Merge Sort")
        def mergeSort(arr):
            if len(arr)  > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]
                mergeSort(left)
                mergeSort(right)
                i = j = k = 0
                
                while(i < len(left) and j < len(right)):
                    if(left[i] < right[j]):
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                    if(i == 0 or j == 0):
                        disp.fill((0, 0, 0))
                        draw_bars(bar_height)
                        pygame.time.delay(10)
                        pygame.display.update()
                    else:
                        disp.fill((0, 0, 0))
                        draw_bars(bar_height)
                        pygame.time.delay(100)
                        pygame.display.update()
                
                while(i < len(left)):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                    disp.fill((0, 0, 0))
                    draw_bars(bar_height)
                    pygame.time.delay(100)
                    pygame.display.update()

                while(j < len(right)):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                    disp.fill((0, 0, 0))
                    draw_bars(bar_height)
                    pygame.time.delay(100)
                    pygame.display.update()                    
        mergeSort(bar_height)
pygame.quit()
