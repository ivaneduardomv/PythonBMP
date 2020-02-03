import random

f = open("image.bmp", "rb")

imageHeader = list(f.read(54))
f.close()

imageHeaderBytes = bytearray(imageHeader)
imageData = []

for x in range(32*32):
	redPixel = random.randint(0, 255)
	greenPixel = random.randint(0, 255)
	bluePixel = random.randint(0, 255)
	imageData.append(redPixel)
	imageData.append(greenPixel*0)
	imageData.append(bluePixel*0)

imageDataBytes = bytearray(imageData)
imageFile = open("newImage.bmp", "wb")
imageFile.write(imageHeaderBytes)
imageFile.write(imageDataBytes)
imageFile.close()
