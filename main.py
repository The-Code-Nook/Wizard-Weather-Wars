import time
from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk
from weapons import *
from mainmenu import MainMenu

WORKINGDIR = Path(__file__).parent.resolve()

tk = Tk()
tk.title("Wizard Weather Wars")
tk.iconbitmap(f"{WORKINGDIR}/assets/images/wizard.ico")
tk.resizable(0,0)
tk.grid_propagate(False)
tk.geometry("1280x720+0+0")

class Tile:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


class HealthBar:
    def __init__(self, canvas: Canvas, startingposX: int, startingposY: int):
        self.canvas: Canvas = canvas
        self.fillid = self.canvas.create_rectangle(0, 0, 0, 10, fill="#FF0000")
        self.outline = self.canvas.create_rectangle(0, 0, 100, 10)
        self.startingposX: int = startingposX
        self.startingposY: int = startingposY
        self.canvas.move(self.fillid, self.startingposX, self.startingposY)
        self.canvas.move(self.outline, self.startingposX, self.startingposY)
    
    def update(self, newhealth):
        newhealth = max(0, newhealth)
        x0,y0,x1,y1 = self.canvas.coords(self.fillid)
        x1 = self.startingposX + newhealth
        # x1 = newhealth
        self.canvas.coords(self.fillid, x0, y0, x1, y1)
    
    def delete(self):
        self.canvas.delete(self.fillid)
        self.canvas.delete(self.outline)


class Environment:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.loadingtext1 = None
        self.id = None
        self.id2 = None
        self.hot = None

        self.img = Image.open(f"{WORKINGDIR}/assets/images/Cloud 2.png")
        self.file = ImageTk.PhotoImage(self.img)
        self.img2 = Image.open(f"{WORKINGDIR}/assets/images/Cloud 1.png")
        self.file2 = ImageTk.PhotoImage(self.img)
    
    def drawHot(self):
        self.clear()
        self.hot = True
        self.loadingtext1 = self.canvas.create_text(600, 200, text="Environment is now HOT!", font="Comic_Sans 20 italic bold", fill="orange")
        self.canvas.configure(bg="#9acae7")
    
    def drawCold(self):
        self.clear()
        self.hot = False
        self.id = self.canvas.create_image((250, 200), image=self.file)
        self.id2 = self.canvas.create_image((900, 150), image=self.file2)

        self.canvas.configure(bg="#d0cccc")
        self.loadingtext1 = self.canvas.create_text(600, 200, text="Environment is now COLD!", font="Comic_Sans 20 italic bold", fill="blue")
    
    def clear(self):
        self.canvas.delete(self.loadingtext1)
        self.canvas.delete(self.id)
        self.canvas.delete(self.id2)
        self.canvas.configure(bg="skyblue")

class Player:
    def __init__(self, canvas: Canvas, Up, Left, Right, Attack, color: str, startingposX, startingposY, name: str, Power, isHot, facing, weakness, env: Environment, sprite, sprite_reverse, weapon: Weapon=None, healthbar: HealthBar=None):
        self.canvas: Canvas = canvas
        self.color: str = color
        self.Attack = Attack
        self.Up = Up
        self.Left = Left
        self.Right = Right
        self.Power = Power

        self.hitbox = self.canvas.create_rectangle(0, 0, 20, 100, outline="")
        self.img = Image.open(sprite)
        self.img_reverse = Image.open(sprite_reverse)
        self.file = ImageTk.PhotoImage(self.img)
        self.file_reverse = ImageTk.PhotoImage(self.img_reverse)
        self.canvas.move(self.hitbox, startingposX, startingposY)
        self.acceleration_y: float = 0.6
        self.velocity_y = 0
        self.velocity_x = 0
        self.jump_count: int = 0
        self.left_stop: bool = True
        self.right_stop: bool = True
        self.isHot: bool = isHot
        self.name: str = name
        # player inertia is friction
        self.player_inertia = 0.08
        self.deactivated = True
        self.weapon = weapon
        self.healthbar = healthbar
        self.enemy = None
        self.weakness = weakness
        self.env: Environment = env
        self.sprint_velocity = 7
        self.jump_height = 12
        self.dead = False
        self.nametag = self.canvas.create_text(startingposX+8, startingposY-25, font="Times 10", text=self.name)
        self.hitboxes_enabled = False
        self.attacked = False

        if facing == "right":
            self.sprite = self.canvas.create_image((startingposX + 10, startingposY + 48), image=self.file)
            self.facing = True
        elif facing == "left":
            self.sprite = self.canvas.create_image((startingposX + 10, startingposY + 48), image=self.file_reverse)
            self.facing = False
        else:
            raise ValueError(f"Player facing attribute can either be, 'left', or 'right', not '{facing}'")
        
        self.health = 100
        # This will range from 0.1 to 1.9 depending on the weather
        self.attack_multiplier = 1

        if self.weapon is not None:
            self.set_bindings()
        if self.healthbar is not None:
            self.healthbar.update()

    def set_bindings(self):
        self.canvas.bind_all(f"<KeyPress-{self.Up}>", self.jump)
        self.canvas.bind_all(f"<KeyPress-{self.Left}>", self.left)
        self.canvas.bind_all(f"<KeyPress-{self.Right}>", self.right)
        self.canvas.bind_all(f"<KeyRelease-{self.Left}>", self.left_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Right}>", self.right_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Attack}>", self.weapon.attack)
        try:
            self.canvas.bind_all(f"<KeyPress-{self.Up.swapcase()}>", self.jump)
        except:
            pass
        try:
            self.canvas.bind_all(f"<KeyPress-{self.Left.swapcase()}>", self.left)
        except:
            pass
        try:
            self.canvas.bind_all(f"<KeyPress-{self.Right.swapcase()}>", self.right)
        except:
            pass
        try:
            self.canvas.bind_all(f"<KeyRelease-{self.Left.swapcase()}>", self.left_stopper)
        except:
            pass
        try:
            self.canvas.bind_all(f"<KeyRelease-{self.Right.swapcase()}>", self.right_stopper)
        except:
            pass
        try:
            self.canvas.bind_all(f"<KeyRelease-{self.Attack.swapcase()}>", self.weapon.attack)
        except:
            pass
        #self.canvas.bind_all(f"<KeyRelease-{self.Power}>", self.powerUp)
    
    def left_stopper(self, button):
        self.left_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True
    
    def right_stopper(self, button):
        self.right_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True

    def move(self,x,y):
        self.canvas.move(self.hitbox, x, y)
        self.canvas.move(self.sprite, x, y)
        self.canvas.move(self.nametag, x, y)

    def draw(self):
        self.move(self.velocity_x, self.velocity_y)

        self.velocity_y += self.acceleration_y
        coords = self.canvas.coords(self.hitbox)

        # Check if we've hit the ground
        if coords[3] > 680:
            self.velocity_y = 0
            self.move(0, 680-coords[3])
            self.jump_count = 2
            self.player_inertia = 0.8
        
        # Check if we're at the left border
        if coords[0] <= 5:
            self.velocity_x = 0
            self.move(5-coords[0], 0)
        # Check if we're at the right border
        if coords[2] >= 1270:
            self.velocity_x = 0
            self.move(1270-coords[2], 0)        
        
        self.weapon.draw(self.canvas.coords(self.hitbox), self.facing)
        
        # Check if we're attacked
        if (not self.attacked) and (self.enemy.weapon.id in self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])) and (self.enemy.weapon.attacking):
            self.attacked = True
            self.damage(self.enemy.weapon.damage)
            if self.enemy.facing:
                self.velocity_x = 20
            else:
                self.velocity_x = -20

            if self.weakness == "hot" and not self.env.hot:
                self.env.drawHot()
            
            elif self.weakness == "cold" and (self.env.hot or self.env.hot is None):
                self.env.drawCold()

            self.sprint_velocity = 4
            self.enemy.sprint_velocity = 7
            self.jump_height = 8
            self.enemy.jump_height = 12
            self.attack_multiplier = 0.75
            self.enemy.attack_multiplier = 1
        elif self.attacked and not self.enemy.weapon.attacking:
            self.attacked = False
        
        # Slowly adding drift so moving is more natural
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
        if self.dead: return

        damage_amount = damage_amount*self.enemy.attack_multiplier
        self.health -= damage_amount
        self.healthbar.update(self.health)
        
        if self.health <= 0:
            self.die()
    
    def die(self):

        self.dead = True
        self.canvas.unbind_all(f"<KeyRelease-{self.Attack}>")
        self.canvas.unbind_all(f"<KeyRelease-{self.enemy.Attack}>")
        wintext = self.canvas.create_text(600,320,fill=self.enemy.color,font="Times 50 bold",text=f"{self.enemy.name} wins!")
        tk.after(500, lambda: initialize_local2p_game(self.canvas, self.env, wintext))
        self.env.clear()

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
    
    def delete(self):
        self.canvas.delete(self.hitbox)
        self.canvas.delete(self.sprite)
        self.canvas.delete(self.nametag)
    
    def toggle_hitboxes(self):
        if self.hitboxes_enabled:
            self.hitboxes_enabled = False
            self.canvas.itemconfigure(self.hitbox, outline="")
        else:
            self.hitboxes_enabled = True
            self.canvas.itemconfigure(self.hitbox, outline="red")


exited = False
def on_quit():
    global exited
    exited = True
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_quit)

def initialize_local2p_game(canvas, env=None, wintext=None, gamestart=False):
    global player1
    global player2

    if not gamestart:
        canvas.delete(wintext)
        player1["healthbar"].delete()
        player1["weapon"].delete()
        player1["player"].delete()

        player2["healthbar"].delete()
        player2["weapon"].delete()
        player2["player"].delete()
    else:
        canvas.create_text(600, 50, fill="darkblue", font="Comic_Sans 40 italic bold", text="WIZARD WEATHER WARS")
        ground = Tile(canvas, 0, 720, 1280, 680, "#008000")


    env = Environment(canvas)
    env.clear()

    player1 = {
        "healthbar": HealthBar(canvas, 0, 50),
        "weapon": IceSword(canvas, True),
        "player": Player(canvas, "w", "a", "d", "v", "#FF0000", 245, 100, "Player 1", "b", True, 'right', "hot", env, f"{WORKINGDIR}/assets/images/icewizard.png", f"{WORKINGDIR}/assets/images/icewizard_reverse.png")
    }
    player1["healthbar"].update(player1["player"].health)
    player1["player"].healthbar = player1["healthbar"]
    player1["player"].weapon = player1["weapon"]
    player1["player"].set_bindings()

    player2 = {
        "healthbar": HealthBar(canvas, 1180, 50),
        "weapon": FireSword(canvas, False),
        "player": Player(canvas, "Up", "Left", "Right", "k", "Green", 1035, 100, "Player 2", "l", False, 'left', "cold", env, f"{WORKINGDIR}/assets/images/firewizard.png", f"{WORKINGDIR}/assets/images/firewizard_reverse.png")
    }
    player2["healthbar"].update(player2["player"].health)
    player2["player"].healthbar = player2["healthbar"]
    player2["player"].weapon = player2["weapon"]
    player2["player"].set_bindings()

    player1["player"].enemy = player2["player"]
    player2["player"].enemy = player1["player"]
    
    canvas.bind_all("<KeyPress-F3>", lambda button, player1=player1, player2=player2: showdebug(player1, player2))


def showdebug(*players):
    # This simply exists because I was noticing weird behavior at the map border, so this was simply to help me by toggling hitboxes
    for player in players: player["player"].toggle_hitboxes()

def start_game(local: bool, playercount: int):
    global game_started
    game_started = True
    canvas = Canvas(tk, width=1280, height=720, bd=0, highlightthickness=0)
    canvas.configure(bg="skyblue")
    canvas.pack()
    tk.update()

    if local == True and playercount == 2:
        initialize_local2p_game(canvas, gamestart=True)

game_started = False
menu = MainMenu(tk, lambda: start_game(True, 2))

try:
    while not exited:
        if game_started:
            player1["player"].draw()
            tk.update()
            if exited: break

            player2["player"].draw()
        tk.update()
        time.sleep(0.005)
except KeyboardInterrupt:
    pass
