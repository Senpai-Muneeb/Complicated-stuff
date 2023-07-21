#from Chat GPT

from tkinter import *

class Ball:
    def __init__(self, canvas, space_x1, space_y1, space_x2, space_y2, xvelocity, yvelocity, speed):
        self.canvas = canvas
        self.create_ball = self.canvas.create_oval(space_x1, space_y1, space_x2, space_y2)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.speed = speed

    def moveing_the_balls(self):
        coordinates = self.canvas.coords(self.create_ball)
        print(coordinates)

        
        
        if coordinates[0] <= 0 or coordinates[2] >= self.canvas.winfo_width():
            self.xvelocity *= -1
        
        if coordinates[1] <= 0 or coordinates[3] >= self.canvas.winfo_height():
            self.yvelocity *= -1

        self.canvas.move(self.create_ball, self.xvelocity, self.yvelocity)

        # Schedule the next movement
        self.canvas.after(self.speed, self.moveing_the_balls)  # Adjust the delay (in milliseconds) as needed

#-------------------------------------------------------------------------------------------------------------------------------

window = Tk()

whiteboard = Canvas(window, height=500, width=500)
whiteboard.pack()

small_ball = Ball(whiteboard, 50, 50, 100, 100, 8, 5, 30)

small_ball.moveing_the_balls()  # Start the movement of the ball

window.mainloop()
