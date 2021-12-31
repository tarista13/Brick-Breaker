"""CS 108 Final Project

This module will test the gui model of the Brick Breaker game.

@author: Tyler Arista (tja9)
@date: Fall, 2021
"""
from ball import Ball
from paddle import Paddle
from brick import Bricks
    
#If they hit the paddle
ball = Ball(250, 430, 0, 0, radius = 10)
paddle = Paddle(210, 420, 80, 20)
assert ball.paddle_collision(paddle)
    
    
#If they hit the bottom of the brick
ball.x = 250
ball.y = 250
brick = Bricks(200, 230, 100, 25)
assert brick.is_hit_bottom(ball.x, ball.y)
     
#If they hit the top of the brick
ball.x = 250
ball.y = 250
brick = Bricks(200, 225, 100, 25)
assert brick.is_hit_top(ball.x, ball.y)
    
#If they hit the left of the brick
ball.x = 190
ball.y = 238
brick = Bricks(195, 225, 100, 25)
assert brick.is_hit_left(ball.x, ball.y)
    
#If they hit the right of the brick
ball.x = 305
ball.y = 238
brick = Bricks(205,225, 100, 25)
assert brick.is_hit_right(ball.x, ball.y)