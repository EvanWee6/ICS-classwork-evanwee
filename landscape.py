# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
moon_speed_x = 0
moon_speed_y = 5

sun_speed_x = 0
sun_speed_y = 5

night_color = (26, 38, 67) 
day_color = (215, 254, 255)

sky_color = night_color
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200

moon_x = 35
moon_y = 50

sun_x = -40
sun_y = 50

stars = []

star_color = (255,255,255)

yOffset = 0

def create_stars():
    for n in range(55):
        x = random.randrange(0,WIDTH)
        y = random.randrange(0,HEIGHT)
        radius = random.randrange(1,5)
        star = [x,y,radius] 
        stars.append(star)

create_stars()

buildings = []
def create_buildings():
    for i in range(10):
        x = random.randrange(0,WIDTH)
        y = 240 
        width = random.randrange(50,150)
        height = random.randrange(20,100)
        building = [x,y,width,height] 
        buildings.append(building)
create_buildings()

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill(sky_color)  # always the first drawing command

        
    for star in stars:
        x = star[0]
        y = star[1]
        radius = star[2]

        pygame.draw.circle(screen,star_color,(x,y + yOffset),radius)


    pygame.draw.rect(screen,(45, 45, 45), (0,240,WIDTH,250)) #road

    cementRectangleX = 0
    for i in range(0,8):
        pygame.draw.rect(screen, (255,255,0), (cementRectangleX, 350, 50,20)) #rectangles on road
        cementRectangleX += 100

    #car
    pygame.draw.ellipse(screen,(0,0,0),(235,370,40,40))
    pygame.draw.ellipse(screen,(0,0,0),(360,370,40,40))
    pygame.draw.rect(screen,((59, 84, 127)),(215,330,80,50))
    pygame.draw.rect(screen,(59,84,127),(280,305,90,75)) 
    pygame.draw.rect(screen,(59,84,127),(320,330,90,50))    
    pygame.draw.rect(screen,((172, 121, 23)),(400,340,10,10))
    pygame.draw.rect(screen,((142, 142, 142)),(340,310,30,20))
    pygame.draw.rect(screen,(142,142,142),(290,310,30,20))



    # sun & moon
    pygame.draw.ellipse(screen,(226,226,226),(moon_x,moon_y,40,40))
    pygame.draw.ellipse(screen,(254, 210, 39),(sun_x,sun_y,40,40))

    moon_speed_x = 5

    moon_x += moon_speed_x
    sun_x += sun_speed_x

    if moon_x >= WIDTH + 40:
        moon_x = -40
        moon_speed_x = 0
        sun_speed_x = 5
        sky_color = day_color
        # screen.fill((215, 254, 255))
        star_color = day_color

        stars.clear()

        create_stars()
    
    if sun_x >= WIDTH + 40:
        sun_x = -40
        sun_speed_x = 0
        moon_speed_x = 5
        sky_color = night_color
        star_color = (255,255,255)

    # tower
    # pygame.draw.rect(screen,(140,140,140),(310,115,20,125))
    # pygame.draw.ellipse(screen,(170,170,170),(293,115,55,20))
    # pygame.draw.polygon(screen,(170,170,170),((315,115),(325,115),(320,50)))

    for building in buildings:
        x = building[0]
        y = building[1]
        width = building[2]
        height = building[3]

        pygame.draw.rect(screen,(144, 144, 144),(x,y-height,width,height))

    for building in buildings:
        building[0] -= 5

        if building[0] <= -100:
            building[0] += 800


# Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
