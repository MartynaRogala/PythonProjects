from PIL import Image
im = Image.open("pole.jpg")
print("Image parameters\nMode:",im.mode)
print("Size:",im.size)
print("Width:",im.width)
print("Height:",im.height)
print("Format:",im.format)

im.thumbnail((128, 128))
im.save('pole_thumbnail.jpg', "JPEG")

im.show()