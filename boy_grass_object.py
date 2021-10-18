from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599  # 위치 정함
        self.image = load_image('ball21x21.png')
        self.frame = 0

    def update(self):
        t = random.randint(1,5)
        self.y -= t
        if self.y<=50:
            self.y=50

        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.draw(self.x, self.y)

class Ball2:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599  # 위치 정함
        self.image = load_image('ball41x41.png')
        self.frame = 0

    def update(self):
        t = random.randint(1, 6)
        self.y -= t
        if self.y<=50:
            self.y=50

        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90  #위치 정함
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame+1)%8

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()

team = [Boy() for i in range(1,11+1)]

balls = [Ball() for i in range(1,11)]
balls2 = [Ball2() for i in range(1,11)]

running = True
# game main loop code
while running:
    handle_events()

    #game logic
    for boy in team:
        boy.update()

    for ball in balls:
        ball.update()

    for ball2 in balls2:
        ball2.update()


    #boy.update()


    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    for ball2 in balls2:
        ball2.draw()



    update_canvas()

    #delay(0.05)


# finalization code
close_canvas()