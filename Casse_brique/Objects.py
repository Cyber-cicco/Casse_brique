import pygame


def absolute(val):
    if val < 0:
        return val * -1
    else:
        return val

class Ball (pygame.Rect):

    id = -1

    def __init__(self, *args, **kwargs):
        pygame.Rect.__init__(self, *args, **kwargs)
        self.speed = 6
        self.mem_x0 = self.x
        self.mem_y0 = self.y
        self.mem_x1 = self.x
        self.mem_y1 = self.y + self.speed


    def change_motion(self, xy):
        self.motion_x = xy[0]
        self.motion_y = xy[1]


    def movement_memory(self, xy):
        self.mem_x0 = self.mem_x1
        self.mem_y0 = self.mem_y1
        self.mem_x1 = xy[0]
        self.mem_y1 = xy[1] 


    def trajectory(self, item):
        if item.bump == 0:
            return (self.mem_x1 - self.mem_x0, self.mem_y0 - self.mem_y1)
        elif item.bump == 1:
            return (self.mem_x0 - self.mem_x1, self.mem_y1 - self.mem_y0)
        else:
            ball_speed = int((((self.x + self.width/2) - (item.x + item.width/2))/(item.width/2))*self.speed)
            return (ball_speed, -(self.speed - (absolute(ball_speed/2))))


class Bumpangle(pygame.Rect):

    id = -1

    def __init__(self, bump, *args, **kwargs):
        pygame.Rect.__init__(self, *args, **kwargs)
        self.bump = bump
    
    def set_id(self, newid):
        self.id = newid

class Brick():

    brick_height = 25
    brick_width = 50
    line_width = 5

    def __init__(self, xy, id=-1):
        self.rect_top = Bumpangle(0,xy[0], xy[1], self.brick_width - 2, self.line_width)
        self.rect_left = Bumpangle(1,xy[0], xy[1], self.line_width, self.brick_height - 2)
        self.rect_bot = Bumpangle(0,xy[0], xy[1] + self.brick_height,self.brick_width - 2, self.line_width)
        self.rect_right = Bumpangle(1,xy[0] + self.brick_width, xy[1], self.line_width, self.brick_height - 2)
        self.list_of_rect = (self.rect_top, self.rect_bot, self.rect_left, self.rect_right)
        self.display_rectangle = Bumpangle(0,xy[0], xy[1], self.brick_width, self.brick_height)
        self.id = id