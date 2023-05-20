from PIL import Image, ImageFilter

filenames = ["x55271.jpg", "x59231.jpg", "x59538.jpg", "x122265.jpg", "x243391.jpg"]

for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        new_img.show()
        new_img.save("new" + file)
