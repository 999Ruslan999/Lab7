from PIL import Image


water = "123.png"
with Image.open(water) as img_water:
    img_water.load()

wat = "123.png"
with Image.open(water) as img_bab:
    img_bab.load()
filename = "x59538.jpg"
with Image.open(filename) as img:
    img.load()


img_water = Image.open(water)

new_img = img_water.resize((img_water.width // 35, img_water.height // 35))
new_img.save("bab.png")
img.paste(new_img, (185, 250), new_img)
img.save("watermark_x59538.jpg")