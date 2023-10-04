from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = random.randint(0, 7)  # Increment frame in a cyclic manner
        self.x += random.randint(1,7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball_big:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')
        self.speed= random.randint(1,5)

    def update(self):
        self.frame = 0
        self.y -= self.speed


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 41, 41, self.x, self.y)


class Ball_small:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(1, 5)

    def update(self):
        self.frame = 0
        self.y -= self.speed


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 21, 21, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global boy
    global ball1
    global ball2
    global team
    global ball_big, ball_small
    # global world
    running = True
    world = []
    grass = Grass()
    boy = Boy()
    ball1 = Ball_big()
    ball2 = Ball_small()
    team = [Boy() for i in range(11)]
    ball_big = [Ball_big() for i in range(10)]
    ball_small = [Ball_small() for i in range(10)]
    # ball= ball1+ ball2
    # world += team
    # world += ball


def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball1 in ball_big:
        ball1.update()
        if ball1.y <= grass.image.h:
            ball1.y = grass.image.h
    for ball2 in ball_small:
        ball2.update()
        if ball2.y <= grass.image.h:
            ball2.y = grass.image.h


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball1 in ball_big:
        ball1.draw()
    for ball2 in ball_small:
        ball2.draw()
    update_canvas()


open_canvas()
reset_world()
running = True

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)

close_canvas()
