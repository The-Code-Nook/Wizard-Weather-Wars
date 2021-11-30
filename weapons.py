from pathlib import Path
from PIL import Image, ImageTk
from utility import trim_image

WORKINGDIR = Path(__file__).parent.resolve()

class Weapon:
    """Shared class for all weapons. This handles drawing it, attacking, and more."""
    def __init__(self, canvas, sprite, sprite_rotate, animation_frames, animation_frames_reverse, damage, facing) -> None:
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

        self.animation_frames = animation_frames
        self.animation_frames_reverse = animation_frames_reverse

        self.attacking_frame = 0
    
    def draw(self, playercoords, facing):
        self.facing = facing
        if self.attacking:
            self.canvas.delete(self.id)
            if facing:
                currim: ImageTk.PhotoImage = self.animation_frames[self.attacking_frame]
                # We get these numbers because -35 on the x, then currim.width() - normalwidth (at the moment, normal width is 21, just view the image for how many pixels) to account for the image's width changing while rotating. Same idea for height
                self.id = self.canvas.create_image((playercoords[2]+currim.width()-41,playercoords[3]-8-currim.height()), image=currim)
                self.attacking_frame += 1
                if self.attacking_frame >= len(self.animation_frames):
                    self.attacking_frame = 0
                    self.attacking = False
            else:
                currim = self.animation_frames_reverse[self.attacking_frame]
                self.id = self.canvas.create_image((playercoords[2]+14-currim.width(),playercoords[3]-8-currim.height()), image=currim)
                self.attacking_frame += 1
                if self.attacking_frame >= len(self.animation_frames_reverse):
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
    
    def delete(self):
        self.canvas.delete(self.id)


class Sword(Weapon):
    """Shared class for all swords. This just simply creates the animations the same."""
    def __init__(self, canvas, sprite, sprite_rotate, damage, facing) -> None:
        self.img = Image.open(sprite)
        self.animation_frames = [self.img]
        rotations = [-10]
        while rotations[-1] <= 10:
            self.animation_frames.append(trim_image(self.img.rotate(sum(rotations), resample=Image.BICUBIC, expand=True)))
            rotations.append(rotations[-1]+1)
        self.animation_frames = [ImageTk.PhotoImage(frame) for frame in self.animation_frames]

        self.img_rotate = Image.open(sprite_rotate)
        self.animation_frames_reverse = [self.img_rotate]
        rotations = [10]
        while rotations[-1] >= -10:
            self.animation_frames_reverse.append(trim_image(self.img_rotate.rotate(sum(rotations), resample=Image.BICUBIC, expand=True)))
            rotations.append(rotations[-1]-1)
        self.animation_frames_reverse = [ImageTk.PhotoImage(frame) for frame in self.animation_frames_reverse]

        super().__init__(canvas, sprite, sprite_rotate,  self.animation_frames, self.animation_frames_reverse, damage, facing)


class FireSword(Sword):
    def __init__(self, canvas, facing, damage=15) -> None:
        super().__init__(canvas, f"{WORKINGDIR}/assets/images/firesword.png", f"{WORKINGDIR}/assets/images/firesword_rotate.png", damage, facing)


class IceSword(Sword):
    def __init__(self, canvas, facing, damage=15) -> None:
        super().__init__(canvas, f"{WORKINGDIR}/assets/images/icesword.png", f"{WORKINGDIR}/assets/images/icesword_rotate.png", damage, facing)
