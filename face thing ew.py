import pygame as p 
p.init()

(width, height) = (500, 500)
backgroundColour = (153, 186, 222)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKIN = (224, 172, 105)

win = p.display.set_mode((width, height))
p.display.set_caption('TRIAL 1')
win.fill(backgroundColour)



p.draw.circle(win, SKIN, (250, 250), 150, 150)


p.draw.circle(win, WHITE, (200, 250), 30, 30)
p.draw.circle(win, BLACK, (200, 250), 10, 10)
p.draw.circle(win, WHITE, (300, 250), 30, 30)
p.draw.circle(win, BLACK, (300, 250), 10, 10)

p.draw.circle(win, BLACK, (250, 330), 40, 40)
p.draw.circle(win, RED, (250, 330), 42, 3)

p.draw.line(win, BLACK, (150, 200), (220, 200), 7)
p.draw.line(win, BLACK, (250, 192), (320, 200), 7)

p.display.flip()


run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
