from PIL import Image

# Rotating and resizing
# new = Image.open("assets\\images\\firesword_original.png").resize((8, 45), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)

# new.save("firesword.png")


# new = Image.open("assets\\images\\icesword_original.png").resize((8, 45), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)

# new.save("icesword.png")

# Making rotation gifs
# rotation = -10
# imgs = [Image.open("assets\\images\\firesword.png")]
# while rotation <= 12:
#     imgs.append(imgs[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
#     rotation += 1
# imgs[0].save("assets\\images\\firesword_attacking.gif", save_all=True, append_images=imgs[1:], optimize=False, duration=40, loop=0)

rotation = -10
imgs = [Image.open("assets\\images\\icesword.png")]
while rotation <= 12:
    imgs.append(imgs[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
    rotation += 1
imgs[0].save("assets\\images\\icesword_attacking.gif", save_all=True, append_images=imgs[1:], optimize=False, duration=40, loop=0)