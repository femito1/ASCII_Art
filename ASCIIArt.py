from PIL import Image, ImageDraw, ImageFont

start_image = Image.open("G:/My Drive/More Python/AI_Lab/data/yuta.png")

greyImage = start_image.convert("L")

pixelWidth = 128
pixelHeight = 64

resizedImage = greyImage.resize((pixelWidth, pixelHeight), resample=Image.Resampling.BILINEAR)

pixels = resizedImage.load()

print(pixels)

characters = "@#W$9876543210?!abc;:=-,._ "


def grey_to_char(num):
    return characters[int(num / 255 * len(characters) - 1)]


i = grey_to_char(2)
print(i)

ascii = ""

for y in range(0, resizedImage.height):
    for x in range(0, resizedImage.width):
        pixel = pixels[x, y]
        ascii += grey_to_char(pixel)
    ascii += "\n"

print(ascii)

img = Image.new(
    "L", (13 * pixelWidth, pixelHeight * 20), 255
)

draw = ImageDraw.Draw(img)
draw.text((0, 0), ascii, 0, font=ImageFont.truetype("courier.ttf", 24))
img.resize((500, 500)).show()