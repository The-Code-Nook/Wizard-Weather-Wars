from tkinter import *
import time
from PIL import Image, ImageTk

tk = Tk()
tk.title("Wizard Weather Wars")
tk.iconbitmap("assets\\images\\wizard.ico")
tk.resizable(0,0)
# Place window at topleft of screen
tk.geometry("+0+0")
# tk.wm_attributes("-topmost", 1)
# 720x1280 screen
canvas = Canvas(tk, width=1280, height=720, bd=0, highlightthickness=0)
canvas.configure(bg="skyblue")
canvas.pack()
tk.update()


class Tile:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        #self.canvas.move(self.id, 245, 100)


class HealthBar:
    def __init__(self, canvas, startingposX, startingposY):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 100, 10, fill="Red")
        self.canvas.move(self.id, startingposX, startingposY)
    
    def update(newhealth):
        pass


class Weapon:
    def __init__(self, canvas, sprite) -> None:
        self.canvas = canvas
        self.img = Image.open(sprite).resize((8, 45), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)
        self.file = ImageTk.PhotoImage(self.img)
        self.id = self.canvas.create_image((100,100), image=self.file)
        self.rotation = 0
        self.attacking = False

        self.animation_frames = [self.img]
        rotation = -10
        while rotation <= 12:
            self.animation_frames.append(self.animation_frames[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
            rotation += 1
        self.animation_frames = [ImageTk.PhotoImage(frame) for frame in self.animation_frames]
        
        self.attacking_frame = 0
    
    def draw(self, playercoords):
        if self.attacking:
            self.canvas.delete(self.id)
            self.id = self.canvas.create_image((playercoords[2]+3,playercoords[3]-37), image=self.animation_frames[self.attacking_frame])
            self.attacking_frame += 1
            if self.attacking_frame >= 23:
                self.attacking_frame = 0
                self.attacking = False
        else:
            coords = self.canvas.coords(self.id)
            self.canvas.move(self.id, playercoords[2] - coords[0]+3, playercoords[3] - coords[1]-37)

    
    def attack(self, button):
        if not self.attacking:
            self.attacking_frame = 1
            self.attacking = True


class Player:
    def __init__(self, canvas, Up, Left, Right, Attack, color, startingposX, startingposY, weapon: Weapon, healthbar: HealthBar):
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
        self.weapon = weapon
        self.healthbar = healthbar

        self.canvas.bind_all(f"<KeyPress-{Up}>", self.jump)
        self.canvas.bind_all(f"<KeyPress-{Left}>", self.left)
        self.canvas.bind_all(f"<KeyPress-{Right}>", self.right)
        self.canvas.bind_all(f"<KeyRelease-{Left}>", self.left_stopper)
        self.canvas.bind_all(f"<KeyRelease-{Right}>", self.right_stopper)
        self.canvas.bind_all(f"<KeyRelease-{Attack}>", self.weapon.attack)

        self.canvas.tag_raise(self.id)

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


isdone = False
def on_quit():
    global isdone
    isdone = True
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_quit)

ground = Tile(canvas, 0, 720, 1280, 680, "green")
p1weapon = Weapon(canvas, "assets\\images\\firesword.png")
p1healthbar = HealthBar(canvas, 0, 50)
player1 = Player(canvas, "w", "a", "d", "c", "Red", 245, 100, p1weapon, p1healthbar)

p2healthbar = HealthBar(canvas, 1180, 50)
p2weapon = Weapon(canvas, "assets\\images\\icesword.png")
player2 = Player(canvas, "Up", "Left", "Right", "m", "Green", 1035, 100, p2weapon, p2healthbar)

try:
    while not isdone:
        player1.draw()
        p1weapon.draw(canvas.coords(player1.id))

        player2.draw()
        p2weapon.draw(canvas.coords(player2.id))

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
except KeyboardInterrupt:
    print('breh just use the x')