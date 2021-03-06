import sys
import os
import pygame
pygame.init()

window = pygame.display.set_mode((800, 670))
info = pygame.image.load('name.png')  # Картинка с названием игры
screen = pygame.image.load('starsky.jpg')  # Картинка заднего фона
# Отображение названия игры в шапке окна
pygame.display.set_caption('ASTROWARS')

lifes = 5  # Начальное количество возможных ошибок

pygame.font.init()
lifes_f = pygame.font.SysFont('Times new roman', 32)  
end = pygame.font.SysFont('Times new roman', 80)
again = pygame.font.SysFont('Times new roman', 40)

# Кнопки в окне меню
punkts = [(350, 260, u'Play', (11, 0, 77), (250, 250, 30), 0),
          (350, 300, u'Rules', (11, 0, 77), (250, 250, 30), 1),
          (350, 340, u'Score', (11, 0, 77), (250, 250, 30), 2),
          (350, 380, u'Exit', (11, 0, 77), (250, 250, 30), 3)]


class Menu:
    """
    Класс, отвечающий за создание меню и работу с ним
    """
    def __init__(self, punkts=None): 
        """
        Функция отвечает за считывание кнопок 
        """
        if punkts is None:
            punkts = [400, 350, u'Punkt', (250, 250, 30),
                      (250, 30, 250)]
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        """
        Функция отвечает за расположение кнопок в игровом окне
        :param poverhnost:
        :param font:
        :param num_punkt:
        :return:
        """
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 150))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 150))

    def menu(self):
        """
        Функция отвечает за взаимодействие с меню
        :return:
        """
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen = pygame.image.load('starsky.jpg')
            info = pygame.image.load('name.png')

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
            window.blit(screen, (0, 150))
            window.blit(info, (70, 0))
            pygame.display.flip()


if __name__ == "__main__":
    print("This module is not for direct call!")
