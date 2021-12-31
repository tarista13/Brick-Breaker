"""CS 108 Final Project

This module implements a GUI controller for a Brick Breaker Game

@author: Tyler Arista (tja9)
@date: Fall, 2021
"""

from guizero import App, Drawing, PushButton, Box, Text
from random import randint
from ball import Ball
from paddle import Paddle
from brick import Bricks
from helpers import get_random_color

class BrickBreaker:
    """BrickBreaker runs a simulation game of a ball
       bouncing around, trying to collide with each brick and break them on a single canvas."""

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Brick Breaker'
        UNIT = 600
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        app.font = 'Times'
        app.text_size = 20
        
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,10,10])
        self.drawing.bg = "Black"
        self.radius = 1
        self.score = 0
        self.x_speed = 0
        self.y_speed = 0

        
        self.title = Text(box, text = "Welcome to Brick Breaker! \n Use the left and right arrow \n to move the paddle. \nPress P to Pause & R to Resume ", grid = [3,4])
        self.title.text_size = 25
        self.title.bg = 'black'
        self.title.text_color = 'Gold'
        PushButton(box, text='Start Game', grid=[3,10], align = 'right', command = lambda:[self.draw(),self.start_game(), self.construct_wall(), self.next_level()])
        self.score_text = Text(box, grid=[0, 10])
        PushButton(box, text = 'Restart', grid=[5,10], command = self.restart_game)
        self.result = Text(box, text = 'GAME OVER', grid = [3,5], visible = False)
        self.result.bg='Black'
        self.result.text_color = 'Red'
        self.result.text_size = 30
        PushButton(box, app.destroy, text='Quit', grid=[7, 10])
        self.update_score()
        
        
        #Creates Paddle and allows it to move left and right using the left and right arrows
        self.paddle = Paddle()
        app.when_key_pressed = self.commands
        
        #Creates an instance of Ball and when the user presses the start game button, the ball will start to move
        self.ball = Ball()
        
        #creates an empty list for the wall
        self.bricks = []
        
        
        app.repeat(50, self.update_score)
        app.repeat(50, self.lose)
        
        
        
    def draw(self):
        """This method will draw the ball, paddle, and bricks for the game and calls the move_frame method."""
        self.drawing.clear()
            
        for b in self.bricks:
            b.draw(self.drawing)
            
        self.leaderboard()
        self.next_level()
        self.paddle.draw(self.drawing)
        self.ball.draw(self.drawing)
        self.move_frame()
        
        
        
        
    def move_frame(self):
        """This method will move the frames for the code. Has the ball bounce off the paddle,
           have the ball move correctly around the canvas and check to see if they need to move a brick."""
        self.ball.bounce_off_paddle(self.paddle)
        self.ball.move(self.drawing)
        self.check_remove_brick(self.ball)
        self.save_speed()
            
            
    def start_game(self):
        """This method will start the game by having a random vel_x and vel_y value and taking away the title text box."""
        self.title.destroy()
        app.repeat(25, self.draw)
        self.ball = Ball(vel_x = randint(-12,12),
                         vel_y = randint(5,7))
        
        if self.ball.vel_x > -3 and self.ball.vel_x < 0:
            self.ball.vel_x = -4
        elif self.ball.vel_x < 3 and self.ball.vel_x >= 0:
            self.ball.vel_x = 4
        
        self.x_speed = self.ball.vel_x
        self.y_speed = - self.ball.vel_y
        
    def restart_game(self):
        """ This method will allow the user to restart the game when the button is pushed.
            . This button only works when the leaderboard method isn't running because I wasn't able to figure out
            how to stop the app.repeat() when the user's ball hit the botom of the canvas. This was added after Project 3 walkthorough."""
        self.result.visible = False
        self.score = 0
        self.paddle = Paddle()
        self.ball = Ball(vel_x = randint(-12,12),
                         vel_y = randint(5,7))
        self.bricks = []
        self.construct_wall()
        
        
    def construct_wall(self):
        """This method will contruct the wall by appending individual bricks to the list"""
        for i in range(4):
            for j in range(6):
                self.bricks.append(Bricks(5 + j * 100,
                                          15 + i * 30,
                                          90,
                                          25,
                                          get_random_color()))
                
    def next_level_bricks(self):
        """Draws bricks in random positions every time the score goes up 600 points. This was added after Project 3 walkthorough"""
        for b in range(24):
            b = Bricks(x = randint(25, app.width - 100),
                       y = randint(25, app.height/2),
                       color = get_random_color()
                )
            self.bricks.append(b)

            
    def commands(self, event):
        """This method will look at the different keys pressed, and if there is a corresponding key, it will execute that action. This was added after Project 3 walkthorough"""
        if event.tk_event.keysym == 'Left':
            self.paddle.move(-20, self.drawing)
        elif event.tk_event.keysym == 'Right':
            self.paddle.move(20, self.drawing)
        elif event.tk_event.keysym == 'p':
            self.ball.vel_x = 0
            self.ball.vel_y = 0
        elif event.tk_event.keysym == 'r':
            self.ball.vel_x = self.x_speed
            self.ball.vel_y = self.y_speed
        
            
    def check_remove_brick(self, ball):
        """This method will check if the ball collided with the brick, and if it did it will be removed. This was added after Project 3 walkthorough"""
        copy = self.bricks[:]
        for b in copy:
            if b.is_hit_bottom(self.ball.x, self.ball.y):
                self.ball.vel_y *= -1
                self.bricks.remove(b)
                self.x_speed = self.ball.vel_x
                self.y_speed = self.ball.vel_y 
                self.score += 25
            elif b.is_hit_top(self.ball.x, self.ball.y):
                self.ball.vel_y *= -1
                self.bricks.remove(b)
                self.y_speed = self.ball.vel_y 
                self.score += 25
            elif b.is_hit_left(self.ball.x, self.ball.y):
                self.ball.vel_x = -1
                self.ball.vel_y *= -1
                self.bricks.remove(b)
                self.y_speed = self.ball.vel_y 
                self.score += 25
            elif b.is_hit_right(self.ball.x, self.ball.y):
                self.ball.vel_x = -1
                self.ball.vel_y *= -1
                self.bricks.remove(b)
                self.y_speed = self.ball.vel_y 
                self.score += 25
                
    def save_speed(self):
        """ This method will save the x and y velocities in order to allow the ball to keep the save velocities when you pause and resume. This was added after Project 3 walkthorough"""
        if self.ball.bounce_off_wall(self.drawing):
            self.x_speed = self.ball.vel_x
            self.y_speed = self.ball.vel_y
        if self.ball.paddle_collision(self.paddle):
            self.y_speed = self.ball.vel_y * -1
        
    def update_score(self):
        """This method will update the score on the canvas. This was added after Project 3 walkthorough"""
        score = self.score
        self.score_text.value = 'Score: ' + str(score)
        
    def lose(self):
        """This method will check if the user lost. This was added after Project 3 walkthorough"""
        if self.ball.hit_bottom(self.drawing):
            self.result.visible = True
            self.ball.vel_x = 0
            self.ball.vel_y = 0
            

        
    def leaderboard(self):
        """ This method will create a txt.file with the players who played the game and print in the shell who are the top 5 scorers. This was added after Project 3 walkthorough.
            This method does work, but continues to run because of app.repeat. I am still working on find a way to fix this, but the buttons restart and quit work if this method commented out."""
        if self.ball.hit_bottom(self.drawing):
            if self.score < 100:
                score = str(self.score)
                score = '00'+ score
            elif self.score < 1000:
                score = str(self.score)
                score = '0'+score
            
            name = input("Enter your name: ")
            file = open('leaderboard.txt', 'a')
            file.write(str(score)+',' + name+'\n')
            file.close()
            
            file = open('leaderboard.txt','r')
            readfile = file.readlines()
            sortedData = sorted(readfile, reverse = True)
            
            print('Top 5 Scores!')
            print('Pos\tPoints, Name')
            
            for line in range(5):
                print(str(line + 1) +'\t'+ str(sortedData[line]))
                
            
    def next_level(self):
        """This method will check if the user moves on to the next level. This was added after Project 3 walkthorough"""
        if self.score > 0 and (self.score % 600) == 0:
                self.next_level_bricks()
                self.ball.vel_x *= 1.1
        
       

app = App()
BrickBreaker(app)
app.display()