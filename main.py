from tkinter import *
import time



tk = Tk()
tk.title("Wizard Weather Wars")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
# 720x1280 screen
canvas = Canvas(tk, width=1280, height=720, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


class Tile:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        #self.canvas.move(self.id, 245, 100)
    

class Player:
    def __init__(self, canvas, Up, Left, Right, color, startingposX, startingposY):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 10, 50, fill=color)
        self.canvas.move(self.id, startingposX, startingposY)
        self.acceleration_y = 0.6
        self.velocity_y = 0
        self.velocity_x = 0
        self.jump_count = 0
        self.left_stop = True
        self.right_stop = True
        # player inertia is friction
        self.player_inertia = 0.08
        self.deactivated = True

        self.canvas.bind_all(f"<KeyPress-{Up}>", self.jump)
        self.canvas.bind_all(f"<KeyPress-{Left}>", self.left)
        self.canvas.bind_all(f"<KeyPress-{Right}>", self.right)
        self.canvas.bind_all(f"<KeyRelease-{Left}>", self.left_stopper)
        self.canvas.bind_all(f"<KeyRelease-{Right}>", self.right_stopper)

    def left_stopper(self, button):
        self.left_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True
    
    def right_stopper(self, button):
        self.right_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True

    def draw(self):
        self.canvas.move(self.id, self.velocity_x, self.velocity_y)
        self.velocity_y += self.acceleration_y
        coords = canvas.coords(self.id)
        if coords[3] > 680:
            self.velocity_y = 0
            self.canvas.move(self.id, 0, 680-coords[3])
            self.jump_count = 2
            self.player_inertia = 0.3
        
        if coords[2] < 10:
            self.velocity_x = 0
            self.canvas.move(self.id, 10-coords[2], 0)
        elif coords[2] > 1271:
            self.velocity_x = 0
            self.canvas.move(self.id, 1271-coords[2], 0)
        
        # Slowly adding drift so it's more natural
        if self.deactivated:
            if self.velocity_x < 0:
                self.velocity_x += self.player_inertia
                if self.velocity_x > 0:
                    self.velocity_x = 0
            elif self.velocity_x > 0:
                self.velocity_x -= self.player_inertia
                if self.velocity_x < 0:
                    self.velocity_x = 0
        
    
    def jump(self, button):
        if self.jump_count:
            self.velocity_y = -12
            self.jump_count -= 1
            # The friction needs to change in the air so the jump is smooth
            self.player_inertia = 0.08
    
    def left(self, button):
        self.velocity_x = -7
        self.left_stop = False
        self.deactivated = False
    
    def right(self, button):
        self.velocity_x = 7
        self.right_stop = False
        self.deactivated = False


ground = Tile(canvas, 0, 720, 1280, 680, "green")
player1 = Player(canvas, "w", "a", "d", "Red", 245, 100)
player2 = Player(canvas, "Up", "Left", "Right", "Green", 1035, 100)
while True:
    player1.draw()
    player2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
