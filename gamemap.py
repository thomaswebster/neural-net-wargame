import constants

class Map(object):
    def __init__(self, dims):
        self.data = [[0]*dims[0] for i in range(dims[1])]

    def draw(self, pos, tilesize):
        pygame.draw.rect(screen, (255,255,255), [0,0,100,100])
