from PIL import Image, ImageFilter

filname = "py_machine.jpg"
with Image.open(filname) as img:
    img.load()

new_img = img.resize((img.width // 3, img.height // 3))

new_img.save("resized_py_machine.jpg")
new_img = img.rotate(180)
new_img.save("rotate_py_machine.jpg")
new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
new_img.save("flip_py_machine.jpg")