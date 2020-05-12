import pygame
from pygame.locals import *
import Eventparser
import Objects
import Niveau


class Game :

    color_fond = (133,164,169)
    color_pad = (66,66,66)
    color_border = (0,0,0)
    color_ball = (204,33,27)
    color_brick = (200,150,24)
    color_unbrickable = (210,20,40)
    border_width = 1
    id_to_kill = -1
    ended =  False


    def __init__(self, pad, surface, nom):
        self.pad = Objects.Bumpangle(2,pad[0], pad[1], pad[2], pad[3])
        self.left_border = Objects.Bumpangle(1,0, 0, self.border_width, surface[1])
        self.right_border = Objects.Bumpangle(1,surface[0] - self.border_width, 0, self.border_width, surface[1])
        self.top_border = Objects.Bumpangle(0,0,0, surface[0], self.border_width)
        self.ball = Objects.Ball((pad[0]+pad[2])-(pad[2]/2 + 5), pad[1]-10, 10, 10)
        self.niveau = Niveau.Level()
        list_of_bricks = self.niveau.create_bricks()
        self.launched = True
        self.srf_fond = pygame.display.set_mode((surface[0], surface[1]))
        self.taille_srf_fond = surface
        self.horloge = pygame.time.Clock()
        self.started = False
        self.list_to_draw = [
            (self.srf_fond, self.color_pad, self.pad),
            (self.srf_fond, self.color_border, self.left_border),
            (self.srf_fond, self.color_border, self.right_border),
            (self.srf_fond, self.color_border, self.top_border),
            (self.srf_fond, self.color_ball, self.ball)
        ]
        self.list_object_to_collide = [
            self.pad,
            self.top_border,
            self.left_border,
            self.right_border,
        ]
        i=0
        for brique in list_of_bricks:
            if brique.id == -1:
                self.list_to_draw.append((self.srf_fond, self.color_brick, brique.display_rectangle))
                for rectangle in brique.list_of_rect:
                    self.list_object_to_collide.append(rectangle)
                    rectangle.set_id(i)
                brique.display_rectangle.set_id(i)
            elif brique.id == 1:
                self.list_to_draw.append((self.srf_fond, self.color_unbrickable, brique.display_rectangle))
                for rectangle in brique.list_of_rect:
                    self.list_object_to_collide.append(rectangle)
            i+=1
        pygame.display.set_caption(nom)


    def mainloop(self):
        while self.launched:
            if self.started:
                Eventparser.events_parsing(self)
            else:
                Eventparser.events_parsing_before(self)
            self.srf_fond.fill(self.color_fond)
            for items in self.list_to_draw:
                pygame.draw.rect(items[0], items[1], items[2])
            self.horloge.tick(60)
            if self.ended:
                self.srf_fond.blit(self.txt_end[0], (self.txt_end[1][0],self.txt_end[1][1]))
            pygame.display.flip()