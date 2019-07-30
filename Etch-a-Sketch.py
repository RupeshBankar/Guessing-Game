import pygame 

pygame.init()

width = 1200
height = 600
x = 10
y = 10
w = 10
h = 10
v = float(0.35)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
cyan = (0, 255, 255)
purple = (127, 0, 255)
pink = (255, 0, 255)


# i like to call my window 'win' instead of 'screen'
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Etch-a-Sketch")
win.fill((250, 250, 250))


def redraw():
    if keys[pygame.K_TAB]:
        pygame.draw.rect(win, (255, 255, 255), (x, y, w + 5, h + 5), 0)
    elif keys[pygame.K_a]:
        pygame.draw.rect(win, red, (x, y, w, h), 0)
    elif keys[pygame.K_w]:
        pygame.draw.rect(win, green, (x, y, w, h), 0)
    elif keys[pygame.K_d]:
        pygame.draw.rect(win, blue, (x, y, w, h), 0)
    elif keys[pygame.K_s]:
        pygame.draw.rect(win, yellow, (x, y, w, h), 0)
    elif keys[pygame.K_q]:
        pygame.draw.rect(win, orange, (x, y, w, h), 0)
    elif keys[pygame.K_x]:
        pygame.draw.rect(win, cyan, (x, y, w, h), 0)
    elif keys[pygame.K_e]:
        pygame.draw.rect(win, purple, (x, y, w, h), 0)
    elif keys[pygame.K_c]:
        pygame.draw.rect(win, pink, (x, y, w, h), 0)
    else:
        pygame.draw.rect(win, (0, 0, 0), (x, y, w, h), 0)
    
    pygame.display.flip()


#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > v:
        x -= v
    if keys[pygame.K_RIGHT] and x < 1200 - w:
        x += v
    if keys[pygame.K_UP] and y > v:
        y -= v
    if keys[pygame.K_DOWN] and y < 545 - h - v:
        y += v
    if keys[pygame.K_ESCAPE]:
        win.fill((250, 250, 250))
    




    redraw()  
    

