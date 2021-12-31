"""CS 108 Final Project

This module implements a model of a paddle.

@author: Tyler Arista (tja9)
@date: Fall, 2021
"""

class Paddle:
    
    
    def __init__(self, x = 250, y = 560, width = 100, height = 20, color = 'white'):
        """Instantiate the Paddle object."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10
        self.direction = 0
        
    def draw(self, drawing):
        """This method will draw the paddle"""
        drawing.rectangle(self.x,
                          self.y,
                          self.x + self.width,
                          self.y + self.height,
                          self.color,
                          outline = True,
                          outline_color = "Gold")
        
    def move(self, amount, drawing):
        """This method will allow the paddle to move left and right."""
        x = self.x + amount
        
        if x < 0 or x + self.width > drawing.width:
            self.x += 0
        else:
            self.x = x
        
        
        
        
        
        
        