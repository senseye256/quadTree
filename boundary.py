import pygame

class boundry(object):
    def __init__(self):
        super(object).__init__()

    def intersects(self, boundry):
        pass
    
    def contains(self, x : float, y : float):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass

    def get_x(self):
        pass

    def get_y(self):
        pass

    def draw(self, screen):
        pass

class rectangle(boundry):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def intersects(self, boundry):
        if isinstance(boundry, type(self)):
            return not (self.x < boundry.x + boundry.width and self.x + self.width > boundry.x and self.y > boundry.y + boundry.height and self.y + self.height < boundry.y)

    def contains(self, x, y):
        return x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height

    def overlap(self, x, y, w, h):
        return not (x > self.x + self.width or x + w < self.x or y > self.y + self.height or y + h < self.y)
    
    def overlapBoundary(self, boundary):
        return self.overlap(boundary.get_x(), boundary.get_y(), boundary.get_width(), boundary.get_height())

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self, screen, color):
        pygame.draw.rect(screen, color,(self.x, self.y, self.width, self.height), 2)



#  todo:// make circle boundary or triangle boundary