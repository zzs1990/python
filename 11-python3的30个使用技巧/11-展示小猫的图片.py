# -*- coding: utf-8 -*-
from PIL import Image
print(f"{'-'*16}展示小猫的图片{'-'*16}")

image = Image.open("kittens.jpg")
image.show()
print(image.format, image.size, image.mode)

print(f"{'-'*16}展示小猫的图片{'-'*16}")
