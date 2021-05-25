import pygame
from pygame import display
from pygame.constants import K_SPACE
from math import pi

pygame.init()

#creating simple window of width - 400 and height - 500
def simpleWindow():
    screen = pygame.display.set_mode((400, 500))

    flag = False

    while not flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
        pygame.display.flip()

#loading image in pygame window
def loadImage():
    white = (255, 255, 255)
    w = 700
    h = 600

    display = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Simple Image')

    img = pygame.image.load('../COWIN-Vaccine-Notifier/Resources/result.JPG')
    ok = False
    while not ok:
        display.fill(white)
        display.blit(img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ok = True
        pygame.display.update()
        pygame.display.flip()

#creating Rectangle in pygame
def createRectangle():
    display = pygame.display.set_mode((400, 300))
    ok = False

    while not ok:
        for event in pygame.event.get(): # when user press close button it will quit pygame
            if event.type == pygame.QUIT: 
                ok = True

        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(30, 50, 90, 90)) #pygame.Rect(leftPadding, topPadding, width, height)
        pygame.display.flip() #it makes change made visible in display

#display which key got pressed
def keyEvents():
    pygame.display.set_caption(u'KEY EVENTS')
    pygame.display.set_mode((400, 400))

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            keyName = pygame.key.name(event.key)
            keyName = keyName.upper()

            if event.type == pygame.KEYDOWN:
                print("{} key pressed".format(keyName))
            
            if event.type == pygame.KEYUP:
                print("{} key released".format(keyName))
# keyEvents()

#expand rectangle according to key which is pressed
def keyEventsVisualization():
    display = pygame.display.set_mode((400, 400))
    ok = True
    closePygame = False
    leftPadding = 30
    topPadding = 30

    while not closePygame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closePygame = True
            if event.type == pygame.KEYDOWN and event.type == K_SPACE:
                ok = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            topPadding -= 3
        if pressed[pygame.K_DOWN]:
            topPadding += 3
        if pressed[pygame.K_LEFT]:
            leftPadding -= 3
        if pressed[pygame.K_RIGHT]:
            leftPadding += 3

        if ok :
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)

        pygame.draw.rect(display, color, pygame.Rect(leftPadding, topPadding, 60, 60))
        pygame.display.flip()

# keyEventsVisualization()

#draw different shapes in pygame
def drawShape():
    displaySize = [400, 300]
    display = pygame.display.set_mode(displaySize)
    pygame.display.set_caption("Draw Shapes")

    ok = False
    clock =  pygame.time.Clock()

    while not ok:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ok =  True
        
        display.fill((0, 0, 0))

        pygame.draw.line(display, (0, 255, 0), [0, 0], [50, 30], 5) #line of 5 pixel wide
        pygame.draw.lines(display, (0, 255, 0), False, [[0, 80], [50, 90], [220, 30]], 5)
        pygame.draw.rect(display,(255, 0, 0), [75, 10, 50, 20], 2) #outlined rectangle
        pygame.draw.rect(display,(255, 0, 0), [150, 10, 50, 20]) #filled rectangle (solid)
        pygame.draw.ellipse(display, (0, 0, 255), [225, 10, 50, 20], 2) #outlined ellipse
        pygame.draw.ellipse(display, (0, 0, 255), [225, 50, 50, 20]) #filled ellipse (solid)
        # pygame.draw.polygon(display, (0, 255, 0), [[100, 100], [0, 200], [200, 200]], 5) #ouline
        pygame.draw.polygon(display, (0, 255, 0), [[100, 100], [0, 200], [200, 200]]) #solid
        pygame.draw.circle(display, (255, 0, 0), [60, 250], 40) #circle(surface, color, center, radius, width)
        pygame.draw.arc(display, (255, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)
        pygame.display.flip();

# drawShape()

#display texts in pygame
def textDisplay():
    display = pygame.display.set_mode((900, 480))
    ok = False
    font = pygame.font.SysFont("Times new Roman", 80)
    text = font.render("Hello, NOOBS!", True, (158, 16, 16))

    while not ok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ok = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                ok = True
        
        display.fill((255, 255, 255))
        display.blit(text, (0, 0))
        pygame.display.flip()

textDisplay()