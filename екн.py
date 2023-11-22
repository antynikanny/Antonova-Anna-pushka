
import math
import pygame
from random import choice, randint as rnd


FPS = 30
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
import math
from math import sqrt
from random import choice, randint as rnd

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
waiting_for_sleep_to_over = False


class Ball:
    def __init__(self, screen: pygame.Surface, gun):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = 450
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.birth = pygame.time.get_ticks()

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 1
        self.x += self.vx
        self.y += self.vy
        self.vy += g
        if self.x >= WIDTH - self.r or self.x <= self.r:
            if self.x > WIDTH - self.r:
                self.x = WIDTH - self.r
            if self.x < self.r:
                self.x = self.r
            self.vx *= -1
            self.vy *= 1
        if self.y >= HEIGHT - self.r:
            if self.y > HEIGHT - self.r:
                self.y = HEIGHT - self.r
            self.vy *= -1
            self.vx *= 1

        if pygame.time.get_ticks() - self.birth >= 1300:
            balls.remove(self)
            del self
        else:
            self.live = 30 - (pygame.time.get_ticks() - self.birth) // 1000

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return sqrt((obj.x - self.x)**2 + (obj.y - self.y)**2) <= obj.r + self.r

class Ball3:
    def __init__(self, screen: pygame.Surface, gun):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = 450
        self.r = 2
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.birth = pygame.time.get_ticks()

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 1
        self.x += self.vx*3
        self.y += self.vy*3
        self.vy += g
        if self.x >= WIDTH - self.r or self.x <= self.r:
            if self.x > WIDTH - self.r:
                self.x = WIDTH - self.r
            if self.x < self.r:
                self.x = self.r
            self.vx *= -1
            self.vy *= 1
        if self.y >= HEIGHT - self.r:
            if self.y > HEIGHT - self.r:
                self.y = HEIGHT - self.r
            self.vy *= -1
            self.vx *= 1

        if pygame.time.get_ticks() - self.birth >= 1300:
            balls.remove(self)
            del self
        else:
            self.live = 30 - (pygame.time.get_ticks() - self.birth) // 1000

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return sqrt((obj.x - self.x)**2 + (obj.y - self.y)**2) <= obj.r + self.r

class Gun:
    def __init__(self, screen, balls_type):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 40
        self.color = GREY
        self.balls_type = "bal1"

    def switch_balls(self):
        self.balls_type = "bal1"

    def switch_balls3(self):
        self.balls_type = "bal3"

    def fire_start(self, event):
        self.f2_on = 1

    def fire_end(self, event):
        if self.balls_type == "bal1":
            self.fire1(event)
        elif self.balls_type == "bal3":
            self.fire3(event)

    def fire1(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, gun)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
    def fire3(self, event):
        global balls, bullet
        bullet += 1
        new_ball3 = Ball3(self.screen, gun)
        new_ball3.r += 5
        self.an = math.atan2((event.pos[1]-new_ball3.y), (event.pos[0]-new_ball3.x))
        new_ball3.vx = self.f2_power * math.cos(self.an)
        new_ball3.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball3)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            d = event.pos[0]-20
            self.an = math.atan((event.pos[1]-450) / d if d != 0 else 1)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
    def moveleft(self):
            self.x -= 10
    def moveright(self):
            self.x += 10



    def draw(self):
        pygame.draw.line(screen, self.color, [self.x, 450],
                         [self.x + self.f2_power * math.cos(self.an),
                          450 + self.f2_power * math.sin(self.an)], 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY




class Target:
    def __init__(self, screen):
     self.points = 0
     self.live = 1
     self.screen = screen
     self.x = rnd(600, 780)
     self.y = rnd(300, 550)
     self.r = rnd(20, 50)
     self.vx = rnd(4,4)
     self.vy = rnd(4,4)
     self.color = RED
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(30, 50)
        self.live = 1
    def move(self):
        if self.x >= WIDTH - self.r or self.x <= self.r:
            if self.x > WIDTH - self.r:
                self.x = WIDTH - self.r
            if self.x < self.r:
                self.x = self.r
            self.vx *= -1

        if self.y >= HEIGHT - self.r:
            self.vy *= -1

        if self.y <= 0 + self.r:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

class Target_gor:
    def __init__(self, screen):
     self.points = 0
     self.live = 1
     self.screen = screen
     self.x = rnd(600, 780)
     self.y = rnd(300, 550)
     self.r = rnd(20, 50)
     self.vx = rnd(4,4)
     self.color = RED
    def new_target(self):
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(30, 50)
        self.live = 1
    def move(self):
        if self.x >= WIDTH - self.r or self.x <= self.r:
            if self.x > WIDTH - self.r:
                self.x = WIDTH - self.r
            if self.x < self.r:
                self.x = self.r
            self.vx *= -1
        self.x += self.vx
        self.y = self.y
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

class Target_vert:
    def __init__(self, screen):
     self.points = 0
     self.live = 1
     self.screen = screen
     self.x = rnd(600, 780)
     self.y = rnd(300, 550)
     self.r = rnd(30, 50)
     self.vy = rnd(4,4)
     self.color = RED
    def new_target(self):
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(30, 50)
        self.live = 1
    def move(self):
        if self.y >= HEIGHT - self.r:
            self.vy *= -1

        if self.y <= 0 + self.r:
            self.vy *= -1
        self.x = self.x
        self.y += self.vy
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
balls_type = "bal1"

clock = pygame.time.Clock()
gun = Gun(screen, balls_type)
types =[Target_gor, Target,Target_vert]
target1 = choice(types)((screen))
target2 = choice(types)((screen))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    if target1.live:
        target1.draw()
        target1.move()
    if target2.live:
        target2.draw()
        target2.move()
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        gun.moveleft()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        gun.moveright()
    if pygame.key.get_pressed()[pygame.K_1]:
        gun.switch_balls()
    if pygame.key.get_pressed()[pygame.K_2]:
        gun.switch_balls3()

    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)




    for b in balls:
        b.move()
        if b.hittest(target1):
            target1.live = 0
            target1.hit()
            target1.new_target()
            balls.remove(b)
        if b.hittest(target2):
            target2.live = 0
            target2.hit()
            target2.new_target()
            balls.remove(b)

    gun.power_up()

pygame.quit()