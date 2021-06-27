import pygame
from pygame import *
from game_platform import *
from player import Player


WIN_WIDTH = 800  # ancho ventana
WIN_HEIGHT = 640  # alto de ventana
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # setea las dimensiones del display
BACKGROUND_COLOR = "#004400"


# configuracion de
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def main():
    init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("RPG")
    my_image = pygame.image.load("/home/andreacat/pocketPyme/rpg-template-master/images/pngs/cosoporfa.png").convert_alpha()
    
    bg = Ground(0, 0)
    timer = pygame.time.Clock()
    hero = Player(155, 155)
    left = right = up = down = False
    
    coins_count = 0

    bandera = True
    entities = pygame.sprite.Group()  # Все объекты
    platforms = pygame.sprite.Group()  # то, во что мы будем врезаться или опираться
    coins = pygame.sprite.Group()  # монеты
    
    # добавляем в фон в список объектов для рисования
    entities.add(bg)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 27)

    # карта
    level = [
        "---------------------------",
        "-    s               s    -",
        "-      c  s     i       ---",
        "-    s                   c-",
        "-                         -",
        "-      c           s      -",
        "--                     c  -",
        "-  s       s              -",
        "-                         -",
        "-         s     e         -",
        "--                        -",
        "-       c       c         -",
        "-  a                      -",
        "-            s            -",
        "-                    c    -",
        "-                         -",
        "-                         -",
        "-                         -",
        "-  c o                    -",
        "-                         -",
        "-           c             -",
        "-                         -",
        "---------------------------"]

    # добавляем объекты с карты в список
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.add(pf)
            if col == "s":
                entities.add(Stone(x, y))
            if col == "w":
                water = Water(x, y)
                entities.add(water)
                platforms.add(water)
            if col == "c":
                coin = Coin(x, y)
                entities.add(coin)
                coins.add(coin)
            if col == "e":
                ed1 = edi1(x,y)
                entities.add(ed1)
                platforms.add(edi1(x, y))
            if col == "a":
                ed2 = edi2(x,y)
                entities.add(ed2)
                platforms.add(edi2(x, y))
            if col == "i":
                ed3 = edi3(x,y)
                entities.add(ed3)
                platforms.add(edi3(x, y))
            if col == "o":
                ed4 = edi4(x,y)
                entities.add(ed4)
                platforms.add(edi4(x, y))
            #if col == "b":
            #    bd = board(x,y)
            #    entities.add(bd)
            #    bd.image.set_alpha(255)
                

                

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    # добавляем персонажа
    entities.add(hero)

    # настройка камеры
    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while True:  # Основной цикл программы
        timer.tick(30)

        for e in pygame.event.get():  # Обрабатываем события

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False

            if e.type == QUIT:
                raise SystemExit("QUIT")
            
            if e.type == KEYDOWN and e.key == K_SPACE:
                if bandera==False:
                    bandera=True
                elif bandera==True:
                    bandera=False

        # обновляем камеру относительно героя
        camera.update(hero)
        my_image.set_alpha(0)
        
        # обновляем позицию персонажа
        

        # рисуем все объекты на карте с учетом смещения камеры
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        # рисуем надпись
        textsurface = myfont.render(f'Coins: {hero.coins_count}', False, (255, 255, 255))
        textsurface2 = myfont.render(f'{hero.mensaje}', False, (255, 255, 255))
        textsurface2.set_alpha(0)

        hero.update(left, right, up, down, platforms, coins ,ed1 ,ed2 ,ed3 ,ed4, my_image ,textsurface2, bandera)
        screen.blit(textsurface, (20, 20))
        screen.blit(textsurface2, (240,500))
        screen.blit(my_image,(200,460))

        
        pygame.display.update()
        


if __name__ == "__main__":
    main()
