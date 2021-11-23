from PIL import Image, ImageOps

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


new = Image.open("assets\\images\\firewizard_original.png").resize((40, 116), Image.ANTIALIAS)

new.save("assets\\images\\firewizard.png")

new = Image.open("assets\\images\\firewizard_reverse_original.png").resize((40, 116), Image.ANTIALIAS)

new.save("assets\\images\\firewizard_reverse.png")


new = Image.open("assets\\images\\icewizard_original.png").resize((40, 116), Image.ANTIALIAS)

new.save("assets\\images\\icewizard.png")

new = Image.open("assets\\images\\icewizard_reverse_original.png").resize((40, 116), Image.ANTIALIAS)

new.save("assets\\images\\icewizard_reverse.png")
