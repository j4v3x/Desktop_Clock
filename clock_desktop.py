#! /usr/bin/env python

from argparse import MetavarTypeHelpFormatter
import pygame
from time import strftime
from random import randint


class ClockDesktop:
    def __init__(self, *args, **kwargs) -> None:

        self.WIDTH = 400
        self.HEIGTH = 250
        self.fps = 10
        self.w = 0
        self.h = 0
        self.radius = 7
        self.ball_radius = 7
        self.ball_speedx = 2
        self.ball_speedy = 2
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        pygame.display.set_caption("Tiny Clock Desktop")
        pygame.display.set_icon(pygame.image.load("/Users/j4v13r/Gitrepo/Clock_Desktop/Icons/clock_ico.png"))
        self.regular_font = "/Users/J4v13r/GitRepo/Clock_Desktop/Fonts/Knack Regular Nerd Font Complete.ttf"
        self.font = "/Users/J4v13r/Gitrepo/Clock_Desktop/Fonts/katakana.ttf"
        pygame.font.init()
        self.array_colors = ["#00ac00", "#00c000", "#00d200","#00e000", "#50584c", "#00ec00", "#00f400","#00ff0e", "#ffffff", "#808080"  ]
        self.random_chars
        self.font_object
        self.give_time
        self.give_date
        self.make_ball
        self.drawing_objects

    # set font object size between 8, 28 (digital rain) 
    def font_object(self):
        return pygame.font.Font(self.font, randint(8, 28)) #18

    # build random chars arrays
    def random_chars(self) -> list:
        return [chr(randint(65, 90)) for _ in range(10)]

    def object_rect(self, w, h) -> list:
        return [pygame.Rect(w, h*x, 0, 0) for x in range(1, 10)]

    # format time
    def give_time(self) -> str:
        return strftime("%H:%M:%S")

    # format date
    def give_date(self) -> str:
        return strftime("%A %d %B %Y")

    # build ball
    def make_ball(self):
        return pygame.Rect(
            randint(1, 40), randint(1, 40), self.radius, self.radius
        )

    def drawing_objects(self) -> None:
        # font and size to time and date
<<<<<<< HEAD
        font_time = pygame.font.Font(self.regular_font, 60)
        font_date = pygame.font.Font(self.regular_font, 25)
        font_string = pygame.font.Font(self.regular_font, 12)
=======
        font_time = pygame.font.Font(self.regular_font, 45)
        font_date = pygame.font.Font(self.regular_font, 20)
        font_string = pygame.font.Font(self.regular_font, 16)
>>>>>>> f58894e11599e467fde15198d8600435e04e94a0
        self.ball = self.make_ball()
        columns = 10
        array_rect = [self.object_rect(x*20, randint(columns, 20)) for x in range(columns)]
        array_rect1 =[self.object_rect(380 - (i*20), randint(columns, 20)) for i in range(columns)]
        centinel = 0
        while True:
            speed = 4
            d = 0
            # set string
            string_ = font_string.render(
                "The Matrix has You",
                True, pygame.Color("#00ff00"))

            # set object  time
            time_now = font_time.render(
                self.give_time(), True, pygame.Color("LightGreen")
            )
            # set object date
            date_now = font_date.render(self.give_date(), True, pygame.Color("Green"))
            self.screen.fill(pygame.Color("#001400"))

            # put objets to screen
<<<<<<< HEAD
            self.screen.blit(date_now, (40, 30))
            self.screen.blit(time_now, (60, 60))
            self.screen.blit(string_, (20, 180))
=======
            self.screen.blit(date_now, (50, 30))
            self.screen.blit(time_now, (80, 60))
            self.screen.blit(string_, (90, 130))
>>>>>>> f58894e11599e467fde15198d8600435e04e94a0

            # put ball to screen
           # pygame.draw.circle(
           #     self.screen,
           #     pygame.Color("white"),
           #     (self.ball.centerx, self.ball.centery),
           #     self.radius,
           # )
           # # animation ball
           # self.ball.y += self.ball_speedy
           # self.ball.x += self.ball_speedx
           # if self.ball.y > self.HEIGTH - self.ball_radius * 2 or self.ball.y < 0:
           #     self.ball_speedy *= -1
           # if self.ball.x > self.WIDTH - self.ball_radius * 2 or self.ball.x < 0:
           #     self.ball_speedx *= -1

            #-------------------- efect rain ------------
            [pygame.draw.circle(self.screen, pygame.Color(
                self.array_colors[5]), array_rect[x][i].center, 0, 0)
                for x in range(0, len(array_rect) -1) for i in range(len(array_rect) -1)]
            [pygame.draw.circle(self.screen, pygame.Color(
                self.array_colors[5]), array_rect1[k][j].center, 0, 0) for k in range(0, len(array_rect1) -1)
                for j in range(len(array_rect1) -1)]
            for v in range(0, 9):
                f = self.font_object().render(self.random_chars()[v], True, pygame.Color(self.array_colors[d]))
                for j in range(9):
                    self.screen.blit(f , (array_rect[j][v]))# max index j 8
                    self.screen.blit(f , (array_rect1[j][v]))# max index j 8
                d += 1
            for j in array_rect:
                for x, i in enumerate(j):
                    if x == 0:
                        i.y += speed + 1
                        if i.y > centinel:
                            i.y = -speed
                    else:
                        i.y += speed
                    if x == 8:
                        centinel = i.y
                    if i.y > 300:
                        i.y = -speed
                speed += 1
            for k in array_rect1:
                for x, i in enumerate(k):
                    if x == 0:
                        i.y += speed + 1
                        if i.y > centinel:
                            i.y = -speed
                    else:
                        i.y += speed
                    if x == 8:
                        centinel = i.y
                    if i.y > 300:
                        i.y = -speed
                speed += 1


            # get exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # update display with fps
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    clock = ClockDesktop()
    clock.drawing_objects()
# EOF
