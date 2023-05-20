from PIL import Image

filname = "py_machine.jpg"
with Image.open(filname) as img:
    img.load()

img.show()
width, height = img.size

format = img.format

mode = img.mode

print("Ширина: ", width)
print("Высота: ", height)
print("Формат: ", format)
print("Цветовая модель: ", mode)