"""CS 108 Final Project

This module implements a model of bricks.

@author: Tyler Arista (tja9)
@date: Fall, 2021
"""

from helpers import distance

class Bricks:
    
    def __init__(self, x = 0, y = 0, width = 100, height = 25,color = "Gray"):
        """Instantiate the Brick object."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
        
    def draw(self, drawing):
        """This method will draw the individual bricks"""
        drawing.rectangle(self.x,
                          self.y,
                          self.x + self.width,
                          self.y + self.height,
                          self.color,
                          outline = True,
                          outline_color = 'white'
                          )
        
    def is_hit_bottom(self, x, y):
        """This method will check if the ball collided with the bottom of the brick. This was added after Project 3 walkthorough"""
        bottom_collision = distance(self.x + (self.width / 2), self.y + (self.height / 2) , x, y)
        if bottom_collision <= self.width / 2:
            return True
        else:
            return False
        
        
    def is_hit_top(self, x, y):
        """This method will check if the ball collided with the top of the brick. This was added after Project 3 walkthorough"""
        top_collision = distance(self.x + (self.width/2), self.y, x, y)
        if top_collision <= self.width/2:
            return True
        else:
            return False
        
        
    def is_hit_left(self, x, y):
        """This method will check if the ball collided with the left of the brick. This was added after Project 3 walkthorough"""
        left_collision = distance(self.x, self.y + (self.height/2), x, y)
        if left_collision <= self.height/2:
            return True
        else:
            return False
        
        
    def is_hit_right(self, x, y):
        """This method will check if the ball collided with the right of the brick. This was added after Project 3 walkthorough"""
        right_collision = distance(self.x + self.width, self.y + (self.height/2), x, y)
        if right_collision <= self.height/2:
            return True
        else:
            return False
        