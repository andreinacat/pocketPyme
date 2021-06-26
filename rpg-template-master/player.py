#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from pygame.transform import scale

MOVE_SPEED = 7
WIDTH = 32
HEIGHT = 52


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        # монеты
        self.coins_count = 0

        # скорость
        self.xvel = 0
        self.yvel = 0

        # прямоугольник игрока
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

        # загружаем анимации для всех направлений
        self.images = {}
        for t in ['up', 'down', 'left', 'right']:
            self.images[t] = []
            for i in range(3):
                self.images[t].append(scale(image.load(f"images/player/{t}{i}.png"), (32, 52)))

        # текущая картинки
        self.index = 0
        self.image = self.images['down'][1]

    def update(self, left, right, up, down, platforms, coins):
        # если персонаж пересекается с монеткой
        for coin in coins:
            if sprite.collide_rect(self, coin):
                coin.kill()
                self.coins_count += 1

        # изменяем скорость в зависимости от нажатых клавиш и выбираем картинку
        if up:
            self.yvel = -MOVE_SPEED
            self.image = self.images['up'][self.index]

        if down:
            self.yvel = MOVE_SPEED
            self.image = self.images['down'][self.index]

        if left:
            self.xvel = -MOVE_SPEED
            self.image = self.images['left'][self.index]

        if right:
            self.xvel = MOVE_SPEED
            self.image = self.images['right'][self.index]

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not (up or down):  # стоим, когда нет указаний идти
            self.yvel = 0

        if not (up or down or left or right):
            self.image = self.images['down'][1]
        else:
            self.index = (self.index + 1) % 3

        # проверяем перечение с объектами на карте
        self.collide(platforms)

        # передвижение
        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.rect.y += self.yvel  # переносим свои положение на xvel

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if self.xvel < 0 and self.rect.left < p.rect.right and self.rect.right > p.rect.right:
                    self.xvel = 0

                if self.xvel > 0 and self.rect.right > p.rect.left and self.rect.left < p.rect.left:
                    self.xvel = 0

                if self.yvel < 0 and self.rect.top < p.rect.bottom and self.rect.bottom > p.rect.bottom:
                    self.yvel = 0

                if self.yvel > 0 and self.rect.bottom > p.rect.top and self.rect.top < p.rect.top:
                    self.yvel = 0
