#! /usr/bin/env python

import pygame
from time import strftime
from random import randint


class ClockDesktop:
    def __init__(self, *args, **kwargs) -> None:

        self.WIDTH = 400
        self.HEIGTH = 250
        self.FPS = 60
        self.RADIUS = 7
        self.BALL_RADIUS = 7
        self.BALL_SPEEDX = 2
        self.BALL_SPEEDY = 2
        self.CLOCK = pygame.time.Clock()
        self.pygame = pygame
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        self.pygame.display.set_caption("Tiny Clock Desktop")
        self.pygame.display.set_icon(self.pygame.image.load("./Icons/clock_ico.png"))
        self.PATH_FONT = "./Fonts/Knack Regular Nerd Font Complete.ttf"
        self.pygame.font.init()
        self.give_time()
        self.give_date()
        self.make_ball()
        self.drawing_objects()

    # format time
    def give_time(self) -> str:
        return strftime("%H:%M:%S")

    # format date
    def give_date(self) -> str:
        return strftime("%A %B %Y")

    # build ball
    def make_ball(self) -> None:
        self.ball = pygame.Rect(
            randint(1, 40), randint(1, 40), self.RADIUS, self.RADIUS
        )
        return

    def drawing_objects(self) -> None:
        # font and size to time and date
        font_time = pygame.font.Font(self.PATH_FONT, 60)
        font_date = pygame.font.Font(self.PATH_FONT, 25)
        while True:
            # set object  time
            time_now = font_time.render(
                self.give_time(), True, pygame.Color("LightGreen")
            )
            # set object date
            date_now = font_date.render(self.give_date(), True, pygame.Color("Green"))
            self.SCREEN.fill(pygame.Color("black"))

            # put objets to screen
            self.SCREEN.blit(date_now, (40, 30))
            self.SCREEN.blit(time_now, (60, 60))

            # put ball to screen
            self.pygame.draw.circle(
                self.SCREEN,
                self.pygame.Color("white"),
                (self.ball.centerx, self.ball.centery),
                self.RADIUS,
            )
            # animation ball
            self.ball.y += self.BALL_SPEEDY
            self.ball.x += self.BALL_SPEEDX
            if self.ball.y > self.HEIGTH - self.BALL_RADIUS * 2 or self.ball.y < 0:
                self.BALL_SPEEDY *= -1
            if self.ball.x > self.WIDTH - self.BALL_RADIUS * 2 or self.ball.x < 0:
                self.BALL_SPEEDX *= -1

            # get exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # update display with fps
            pygame.display.update()
            self.CLOCK.tick(self.FPS)


if __name__ == "__main__":
    clock = ClockDesktop()
    clock.drawing_objects()
# EOF
