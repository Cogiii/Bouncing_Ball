from tkinter import *
import random
import time

score = 0
speed = 2

class Points:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 0, 20, fill=color)
        self.canvas_height = 400
        self.canvas_width = 500
        xpos = 0
        ypos = 0
        self.canvas.move(self.id, xpos, ypos)

    def pointhit(self, pos):
        ball_pos = self.canvas.coords(self.ball.id)
        if pos[2] >= ball_pos[0] and pos[0] <= ball_pos[2]:
            if pos[3] >= ball_pos[1] and pos[3] <= ball_pos[3]:
                return True
        return False



class Ball:
    from tkinter import PhotoImage
import random

class Ball:
    def __init__(self, canvas, color, paddle, points):
        self.canvas = canvas
        self.paddle = paddle
        self.points = points
        self.id = canvas.create_oval(0, 0, 35, 35, fill=color)
        
        # Load the original image
        self.image = PhotoImage(file='Bouncing-Ball/mapua.png')

        # Resize the image to the desired dimensions
        self.resized_image = self.image.subsample(1, 1)  # Adjust the factors for your desired size

        # Create image on canvas using the resized image
        self.image_id = canvas.create_image(263, 120, image=self.resized_image, anchor='center')

        self.canvas.move(self.id, 245, 100)
        self.canvas_height = 400
        self.canvas_width = 500
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.hit_bottom = False


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        self.canvas.move(self.image_id ,self.x, self.y)
        # returns coordinates of the ball ex.:[255.0, 29.0, 270.0, 44.0] first
        # two coordinates are top left coords and next two are bottom right
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = speed
        if pos[2] >= self.canvas_width:
            self.x = -speed
        if self.hit_paddle(pos):
            self.y = -speed
        if self.hit_points(pos):
            pass

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.rect)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                global score
                global speed 
                score = score + 1
                speed = speed+(score*0.05)

                return True
        return False

    def hit_points(self, pos):
        points_pos = self.canvas.coords(self.points.id)
        if pos[2] >= points_pos[0] and pos[0] <= points_pos[2]:
            if pos[3] >= points_pos[1] and pos[3] <= points_pos[3]:
                global score
                score = score + 50
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(100, 10, 0, 0, fill=color)
        self.canvas.move(self.rect, 200, 300)
        self.x = 0
        self.canvas_width = 500
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        if self.canvas.coords(self.rect)[0] <= 0:
            self.x = 0
        if self.canvas.coords(self.rect)[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, evt):
        if self.canvas.coords(self.rect)[0] >= 0:
            self.x = -3

    def move_right(self, evt):
        if self.canvas.coords(self.rect)[2] < self.canvas_width:
            self.x = 3


def gameover(canvas):
    global score
    canvas.create_text(250, 120, text='Game Over!', fill='red',
                       font=('Times', 15))
    canvas.create_text(250, 150, text='Score: ' + str(score), fill='red',
                       font=('Times', 15))


tk = Tk()

# adds title to the window
tk.title('Bouncing Ball')
# make the window non-resizable both horizontally and vertically
tk.resizable(0, 0)

# make the window appear on top of other windows
tk.wm_attributes("-topmost", 1)

# extra named parameters don't allow border
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.configure(bg='#272928')
canvas.pack()
paddle = Paddle(canvas, color='#a13206')
points = Points(canvas, color='red')
ball = Ball(canvas, color='#EBF2FA', paddle=paddle, points=points)

# MAIN LOOP

while 1:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        gameover(canvas)
    tk.update_idletasks()
    tk.update()
    '''
    the commands update_idletasks and update tell tkinterto
    hurry up and draw what is on the canvas.'''
    time.sleep(0.01)  # so that animation is not that fast
