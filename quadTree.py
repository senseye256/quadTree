import math
import pygame
import random
from boundary import rectangle
from entity import entity

class quadTree(object):
    def __init__(self, boundry, depth):
        super().__init__()
        self.boundary = boundry 
        self.depth = depth
        self.entities = []
        self.upLeft = None
        self.upRight = None
        self.downLeft = None
        self.downRight = None
    
    def subdevide(self):
        hw = self.boundary.get_width() / 2
        hh = self.boundary.get_height() / 2
        self.upLeft = quadTree(rectangle(self.boundary.get_x(), self.boundary.get_y(), hw, hh), self.depth)
        self.upRight = quadTree(rectangle(self.boundary.get_x()+hw, self.boundary.get_y(), hw, hh), self.depth)
        self.downLeft = quadTree(rectangle(self.boundary.get_x(), self.boundary.get_y() + hh, hw, hh), self.depth)
        self.downRight = quadTree(rectangle(self.boundary.get_x()+hw, self.boundary.get_y() + hh, hw, hh), self.depth) 
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.boundary.x + 1, self.boundary.y + 1, self.boundary.width - 1, self.boundary.height - 1), 2)
        if self.upLeft:
            self.upLeft.draw(screen)
            self.upRight.draw(screen)
            self.downLeft.draw(screen)
            self.downRight.draw(screen)

    def insert(self, entt : entity):
        if not self.boundary.contains(entt.x, entt.y):
            return False
        if len(self.entities) <= self.depth:
            self.entities.append(entt)
            return True
        if not self.upLeft:
            self.subdevide()

        if self.upLeft.insert(entt): return True
        if self.upRight.insert(entt): return True
        if self.downLeft.insert(entt): return True
        if self.downRight.insert(entt): return True
        return False

    def query(self, boundary):
        result = []
        if not self.boundary.overlapBoundary(boundary):
            return result
        for entt in self.entities:
            if boundary.contains(entt.x, entt.y):
                result.append(entt)

        if not self.upLeft:
            return result

        result.extend(self.upLeft.query(boundary))
        result.extend(self.upRight.query(boundary))
        result.extend(self.downLeft.query(boundary))
        result.extend(self.downRight.query(boundary))
        return result

#todo refactor this, and add dynamic tree        