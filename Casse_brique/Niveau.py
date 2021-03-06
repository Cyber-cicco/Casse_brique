import pygame
import Objects

class Level():
    def __init__(self):
        self.grid = (
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1),
            (0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0),
            (1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1),
            (0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0),
            (1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        )

    def create_bricks(self):
        i = 0
        j = 0
        list_of_bricks = []
        for line in self.grid:
            for item in line:
                if item == 1:
                    list_of_bricks.append(Objects.Brick((i*50, j*25)))
                elif item == 2:
                    list_of_bricks.append(Objects.Brick((i*50, j*25), id=1))
                i += 1
            i = 0
            j +=1
        return list_of_bricks

