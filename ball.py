"""CS 108 Final Project

This module implements a model of a ball.

@author: Tyler Arista (tja9)
@date: Fall, 2021
"""

class Ball:
    
    
    def __init__(self, x=300, y=550, vel_x=0, vel_y=0, radius=10, color="red"):
        """Instantiate the Ball object."""
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.color = color
        self.hitPaddle = False
        
    def draw(self, drawing):
        """This method will draw the particles"""
        drawing.oval(self.x - self.radius,
                     self.y - self.radius,
                     self.x + self.radius,
                     self.y + self.radius,
                     color = self.color
            )
        
    def move(self, drawing):
        """This method makes the ball move on the canvas"""
        self.x += self.vel_x
        self.y += self.vel_y
        
        if self.x + self.radius > drawing.width or self.x - self.radius < 0:
            self.vel_x = self.vel_x * -1
            
        if self.y - self.radius < 0:
            self.vel_y = self.vel_y * -1
            
    def bounce_off_wall(self, drawing):
        if self.x + self.radius > drawing.width or self.x - self.radius < 0:
            return True
        elif self.y - self.radius < 0:
            return True
        else:
            return False

    def bounce_off_paddle(self, paddle):
        """This method will have the ball bounce off the paddle if they collide"""
        if (self.x >= paddle.x and self.x <= paddle.x + paddle.width) or (self.x + self.radius >= paddle.x and self.x - self.radius <= paddle.x + paddle.width):
            if (self.y + self.radius > paddle.y) and (self.y + self.radius <= paddle.y + paddle.height):
                self.vel_y *= -1
                
    def paddle_collision(self, paddle):
        """ This method will return a boolean statement to see if the ball collided with the paddle to help store the velocity of the ball in the gui interface. This was added after Project 3 walkthorough."""
        if (self.x >= paddle.x and self.x <= paddle.x + paddle.width) or (self.x + self.radius >= paddle.x and self.x - self.radius <= paddle.x + paddle.width):
            if (self.y + self.radius > paddle.y) and (self.y + self.radius <= paddle.y + paddle.height):
                return True
            else:
                return False
                
    def bounce_off_brick(self, wall):
        """This method will have the ball bounce off the bricks if they collide. This was added after Project 3 walkthorough."""
        for b in wall:
            if (self.x >= b.x and self.x <= b.x + b.width) or (self.x + self.radius >= b.x and self.x + b.width <= b.x + b.width):
                if (self.y - self.radius < b.y + b.height) and (self.y + self.radius >= b.y):
                    self.vel_y *= -1
                    
    def hit_bottom(self, drawing):
        """ This will check if the ball hits the bottom of the canvas to see if the user lost. This was added after Project 3 walkthorough."""
        if self.y + self.radius > drawing.height:
            return True
        else:
            return False
                    