from tkinter import *
import time
from PIL import Image, ImageTk
import random
import requests
from bs4 import BeautifulSoup as bs
from weatherFunction import findWeather

'''
weatherInfo = findWeather()
city, state, temp, timings, sky, otherData = weatherInfo
tempNum = 0
if temp[1] == "°":
    tempNum = int(temp[0])
if temp[2] == "°":
    tempNum = int(temp[0:2])
if temp[3] == "°":
    tempNum = int(temp[0:3])

if tempNum < 60:
    environment = "cold"
elif tempNum > 75:
    environment = "hot"
else:
    environment = "normal"

'''
tk = Tk()
tk.title("Wizard Weather Wars")
tk.iconbitmap("assets\\images\\wizard.ico")
tk.resizable(0,0)
# Place window at topleft of screen
tk.geometry("+0+0")
# tk.wm_attributes("-topmost", 1)
# 720x1280 screen
canvas = Canvas(tk, width=1280, height=720, bd=0, highlightthickness=0)
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
        self.fillid = self.canvas.create_rectangle(0, 0, 0, 10, fill="#FF0000")
        self.outline = self.canvas.create_rectangle(0, 0, 100, 10)
        self.startingposX = startingposX
        self.startingposY = startingposY
        self.canvas.move(self.fillid, self.startingposX, self.startingposY)
        self.canvas.move(self.outline, self.startingposX, self.startingposY)
    
    def update(self, newhealth):
        newhealth = max(0, newhealth)
        x0,y0,x1,y1 = self.canvas.coords(self.fillid)
        x1 = self.startingposX + newhealth
        # x1 = newhealth
        self.canvas.coords(self.fillid, x0, y0, x1, y1)


class Weapon:
    def __init__(self, canvas, sprite, sprite_rotate, damage, facing) -> None:
        self.canvas = canvas
        self.img = Image.open(sprite)
        self.img_rotate = Image.open(sprite_rotate)
        self.file = ImageTk.PhotoImage(self.img)
        self.file_rotate = ImageTk.PhotoImage(self.img_rotate)

        if facing:
            self.id = self.canvas.create_image((100,100), image=self.file)
        else:
            self.id = self.canvas.create_image((100,100), image=self.file_rotate)

        self.rotation = 0
        self.attacking = False
        self.damage = damage

        self.animation_frames = [self.img]
        rotation = -10
        while rotation <= 12:
            self.animation_frames.append(self.animation_frames[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
            rotation += 1
        self.animation_frames = [ImageTk.PhotoImage(frame) for frame in self.animation_frames]

        self.animation_frames_reverse = [self.img_rotate]
        rotation = 10
        while rotation >= -12:
            self.animation_frames_reverse.append(self.animation_frames_reverse[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
            rotation -= 1
        self.animation_frames_reverse = [ImageTk.PhotoImage(frame) for frame in self.animation_frames_reverse]
        
        self.attacking_frame = 0
    
    def draw(self, playercoords, facing):
        if self.attacking:
            if facing:
                self.canvas.delete(self.id)
                self.id = self.canvas.create_image((playercoords[2]+10,playercoords[3]-80), image=self.animation_frames[self.attacking_frame])
                self.attacking_frame += 1
                if self.attacking_frame >= 23:
                    self.attacking_frame = 0
                    self.attacking = False
        
            else:
                self.canvas.delete(self.id)
                self.id = self.canvas.create_image((playercoords[2]-35,playercoords[3]-80), image=self.animation_frames_reverse[self.attacking_frame])
                self.attacking_frame += 1
                if self.attacking_frame >= 23:
                    self.attacking_frame = 0
                    self.attacking = False

        else:
            coords = self.canvas.coords(self.id)
            if facing:
                self.canvas.move(self.id, playercoords[2] - coords[0]+10, playercoords[3] - coords[1]-80)
            else:
                self.canvas.move(self.id, playercoords[2] - coords[0]-35, playercoords[3] - coords[1]-80)
        
    def face_left(self):
        self.attacking_frame = 0
        self.canvas.delete(self.id)
        self.id = self.canvas.create_image((0,0), image=self.file_rotate)
        self.attacking = False

    def face_right(self):
        self.attacking_frame = 0
        self.canvas.delete(self.id)
        self.id = self.canvas.create_image((0,0), image=self.file)
        self.attacking = False

    def attack(self, button):
        if not self.attacking:
            self.attacking_frame = 1
            self.attacking = True

class Environment:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.delete_countdown = -1
        self.loadingtext1 = None
        self.id = None
        self.id2 = None

        self.img = Image.open("assets\\images\\Cloud 2.png")
        self.file = ImageTk.PhotoImage(self.img)
        self.img2 = Image.open("assets\\images\\Cloud 1.png")
        self.file2 = ImageTk.PhotoImage(self.img)

    
    def draw(self):
        if self.delete_countdown > 0:
            self.delete_countdown -= 1
        elif self.delete_countdown == 0:
            self.clear()
            self.delete_countdown = -1

    def drawHot(self):
        self.clear()
        '''self.img = Image.open(sprite1).resize((100, 100), Image.ANTIALIAS)
        self.file = ImageTk.PhotoImage(self.img)
        self.id = self.canvas.create_image((100, 100), image=self.file)'''
        self.loadingtext1 = canvas.create_text(600, 200, text="Environment is now HOT!", font="Comic_Sans 20 italic bold", fill="orange")
        self.delete_countdown = 100
        canvas.configure(bg="#9acae7")
    
    def drawCold(self):
        self.clear()
        self.id = self.canvas.create_image((250, 200), image=self.file)
        self.id2 = self.canvas.create_image((900, 150), image=self.file2)

        canvas.configure(bg="#d0cccc")
        self.loadingtext1 = canvas.create_text(600, 200, text="Environment is now COLD!", font="Comic_Sans 20 italic bold", fill="blue")
        self.delete_countdown = 100
    
    def clear(self):
        self.canvas.delete(self.loadingtext1)
        self.canvas.delete(self.id)
        self.canvas.delete(self.id2)

class Player:
    def __init__(self, canvas: Canvas, Up, Left, Right, Attack, color: str, startingposX, startingposY, weapon: Weapon, healthbar: HealthBar, name: str, Power, isHot, facing, weakness, env, sprite, sprite_reverse):
        self.canvas: Canvas = canvas
        self.color: str = color
        self.Attack = Attack
        self.Up = Up
        self.Left = Left
        self.Right = Right
        self.Power = Power
        #self.id is hitbox
        self.id = self.canvas.create_rectangle(0, 0, 20, 100, outline="")
        self.img = Image.open(sprite)
        self.img_reverse = Image.open(sprite_reverse)
        self.file = ImageTk.PhotoImage(self.img)
        self.file_reverse = ImageTk.PhotoImage(self.img_reverse)
        self.canvas.move(self.id, startingposX, startingposY)
        self.acceleration_y = 0.6
        self.velocity_y = 0
        self.velocity_x = 0
        self.jump_count = 0
        self.left_stop = True
        self.right_stop = True
        self.isHot = isHot
        self.name: str = name
        # player inertia is friction
        self.player_inertia = 0.08
        self.deactivated = True
        self.weapon = weapon
        self.healthbar = healthbar
        self.enemy = None
        self.weakness = weakness
        self.env = env
        self.sprint_velocity = 7
        self.jump_height = 12

        if facing == "right":
            self.sprite = self.canvas.create_image((startingposX + 10, startingposY + 48), image=self.file)
            self.facing = True
        elif facing == "left":
            self.sprite = self.canvas.create_image((startingposX + 10, startingposY + 48), image=self.file_reverse)
            self.facing = False
        else:
            raise ValueError(f"Player facing attribute can either be, 'left', or 'right', not '{facing}'")

        self.canvas.bind_all(f"<KeyPress-{self.Up}>", self.jump)
        self.canvas.bind_all(f"<KeyPress-{self.Left}>", self.left)
        self.canvas.bind_all(f"<KeyPress-{self.Right}>", self.right)
        self.canvas.bind_all(f"<KeyRelease-{self.Left}>", self.left_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Right}>", self.right_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Attack}>", self.weapon.attack)
        #self.canvas.bind_all(f"<KeyRelease-{self.Power}>", self.powerUp)

        self.canvas.tag_raise(self.id)

        self.health = 100
        self.healthbar.update(self.health)
        # This will range from 0.1 to 1.9 depending on the weather
        self.attack_multiplier = 1
        self.defense_multiplier = 1
    
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
        self.canvas.move(self.sprite, self.velocity_x, self.velocity_y)

        self.velocity_y += self.acceleration_y
        coords = canvas.coords(self.id)

        # Check if we've hit the ground
        if coords[3] > 680:
            self.velocity_y = 0
            self.canvas.move(self.id, 0, 680-coords[3])
            self.canvas.move(self.sprite, 0, 680-coords[3])
            self.jump_count = 2
            self.player_inertia = 0.8
        
        # Check if we're at the left border
        if coords[0] <= 5:
            self.velocity_x = 0
            self.canvas.move(self.id, 5-coords[0], 0)
            self.canvas.move(self.sprite, 5-coords[0], 0)
        # Check if we're at the right border
        if coords[2] >= 1270:
            self.velocity_x = 0
            self.canvas.move(self.id, 1270-coords[2], 0)
            self.canvas.move(self.sprite, 1270-coords[2], 0)
        
        
        self.weapon.draw(canvas.coords(self.id), self.facing)
        
        # Check if we're attacked
        if self.enemy.weapon.id in self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3]) and self.enemy.weapon.attacking:
            self.damage(self.enemy.weapon.damage)
            if self.enemy.facing:
                self.velocity_x = 20
            else:
                self.velocity_x = -20

            if self.weakness == "hot":
                self.env.drawHot()
            
            elif self.weakness == "cold":
                self.env.drawCold()

            self.sprint_velocity = 4
            self.enemy.sprint_velocity = 7
            self.jump_height = 6
            self.enemy.jump_height = 12
            self.attack_multiplier = 0.5
            self.enemy.attack_multiplier = 1
            

        
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

    def damage(self, damage_amount):
        # Small attack cooldown
        damage_amount = damage_amount*self.enemy.attack_multiplier
        self.health -= damage_amount
        self.healthbar.update(self.health)
        
        if self.health <= 0:
            self.die()
    
    def die(self):
        self.canvas.create_text(600,320,fill=self.enemy.color,font="Times 50 bold",text=f"{self.enemy.name} wins!")

        self.canvas.unbind(f"<KeyPress-{self.Attack}>")
        self.canvas.unbind(f"<KeyPress-{self.Power}>")
        btn = Button(tk, text='New Game', width=40, height=5, bd='10', command=startgame)
        btn.place(x=65, y=100)
        global isdone
        isdone = True
    
    def jump(self, button):
        if self.jump_count:
            self.velocity_y = -self.jump_height
            self.jump_count -= 1
            # The friction needs to change in the air so the jump is smooth
            self.player_inertia = 0.08
    
    def left(self, button):
        self.velocity_x = -self.sprint_velocity
        self.left_stop = False
        self.deactivated = False
        old = self.facing
        self.facing = False
        if old != self.facing:
            coords = self.canvas.coords(self.sprite)
            self.canvas.delete(self.sprite)
            self.sprite = self.canvas.create_image((coords[0], coords[1]), image=self.file_reverse)
            self.weapon.face_left()
    
    def right(self, button):
        self.velocity_x = self.sprint_velocity
        self.right_stop = False
        self.deactivated = False
        old = self.facing
        self.facing = True
        if old != self.facing:
            coords = self.canvas.coords(self.sprite)
            self.canvas.delete(self.sprite)
            self.sprite = self.canvas.create_image((coords[0], coords[1]), image=self.file)
            self.weapon.face_right()


exited = False
def on_quit():
    global exited
    exited = True
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_quit)
canvas.create_text(600,50,fill="darkblue",font="Comic_Sans 40 italic bold",
                        text="WIZARD WEATHER WARS")

def startgame():
    global env
    
    isdone = False
    canvas.delete("all")
    canvas.configure(bg="skyblue")

    canvas.create_text(600, 50, fill="darkblue", font="Comic_Sans 40 italic bold",
                       text="WIZARD WEATHER WARS")

    env = Environment(canvas)

    ground = Tile(canvas, 0, 720, 1280, 680, "#008000")
    
    p1weapon = Weapon(canvas,"assets\\images\\icesword.png", "assets\\images\\icesword_rotate.png",  5, True)
    p1healthbar = HealthBar(canvas, 0, 50)
    player1 = Player(canvas, "w", "a", "d", "v", "#FF0000", 245, 100, p1weapon, p1healthbar, "Player 1", "b", True, 'right', "hot", env, "assets\\images\\icewizard.png", "assets\\images\\icewizard_reverse.png")

    p2healthbar = HealthBar(canvas, 1180, 50)
    p2weapon = Weapon(canvas, "assets\\images\\firesword.png", "assets\\images\\firesword_rotate.png", 5, False)
    player2 = Player(canvas, "Up", "Left", "Right", "k", "Green", 1035, 100, p2weapon, p2healthbar, "Player 2", "l", False, 'left', "cold", env, "assets\\images\\firewizard.png", "assets\\images\\firewizard_reverse.png")

    player1.enemy = player2
    player2.enemy = player1

    try:
        env.draw()
        while not isdone and not exited:

            player1.draw()

            player2.draw()

            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        else:
            del ground

            del p1weapon
            del p1healthbar
            del player1

            del p2weapon
            del p2healthbar
            del player2
    except KeyboardInterrupt:
        print('breh just use the x')

if __name__ == "__main__":
    startgame()
