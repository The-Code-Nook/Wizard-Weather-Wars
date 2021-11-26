from PIL import Image, ImageChops

def trim_image(im: Image):
    """https://stackoverflow.com/questions/10615901/trim-whitespace-using-pil"""
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
