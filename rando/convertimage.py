from PIL import Image, ImageOps, ImageChops

# Rotating and resizing
# new = Image.open("assets\\images\\firesword_original.png").resize((16, 90), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)

# new.save("firesword.png")


# new = Image.open("assets\\images\\icesword_original.png").resize((16, 90), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)

# new.save("icesword.png")

# Making rotation gifs
# rotation = -10
# imgs = [Image.open("assets\\images\\firesword.png")]
# while rotation <= 12:
#     imgs.append(imgs[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
#     rotation += 1
# imgs[0].save("assets\\images\\firesword_attacking.gif", save_all=True, append_images=imgs[1:], optimize=False, duration=40, loop=0)

# rotation = -10
# imgs = [Image.open("assets\\images\\icesword.png")]
# while rotation <= 12:
#     imgs.append(imgs[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
#     rotation += 1
# imgs[0].save("assets\\images\\icesword_attacking.gif", save_all=True, append_images=imgs[1:], optimize=False, duration=40, loop=0)

# img = Image.open("assets\\images\\firesword.png")
# img2 = Image.open("assets\\images\\icesword.png")

# flipped = ImageOps.mirror(img)
# flipped2 = ImageOps.mirror(img2)

# flipped.save("assets\\images\\firesword_rotate.png")
# flipped2.save("assets\\images\\icesword_rotate.png")


# new = Image.open("assets\\images\\firewizard_original.png").resize((40, 116), Image.ANTIALIAS)

# new.save("assets\\images\\firewizard.png")

# new = Image.open("assets\\images\\firewizard_reverse_original.png").resize((40, 116), Image.ANTIALIAS)

# new.save("assets\\images\\firewizard_reverse.png")


# new = Image.open("assets\\images\\icewizard_original.png").resize((40, 116), Image.ANTIALIAS)

# new.save("assets\\images\\icewizard.png")

# new = Image.open("assets\\images\\icewizard_reverse_original.png").resize((40, 116), Image.ANTIALIAS)

# new.save("assets\\images\\icewizard_reverse.png")

def trim(im):
    """https://stackoverflow.com/questions/10615901/trim-whitespace-using-pil"""
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


sprite = "assets\\images\\firesword.png"
# sprite_rotate = "assets\\images\\firesword_rotate.png"

img = Image.open(sprite)

animation_frames = [img]
for rotation in range(-10,13,5):
    animation_frames.append(img.rotate(rotation, resample=Image.BICUBIC, expand=True))
    rotation += 1

for i,frame in enumerate(animation_frames):
    trim(frame).save(f"assets\\tests\\firesword_frames\\frame_{i}.png")
