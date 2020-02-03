import random
import time

f = open("originalImage.bmp", "rb")

originalImageHeader = list(f.read(54))
print(f.tell())
originalImageData = list(f.read())
f.close()
print(len(originalImageData))

originalImageHeaderBytes = bytearray(originalImageHeader)
noisyImageData = []

startTime = time.time()
for x in range(640*480):
	noise = random.randint(0,255)
	if (originalImageData[x*3+0] + noise) < 255:
		noisyImageData.append(originalImageData[x*3+0] + noise)
	else:
		noisyImageData.append(originalImageData[x*3+0])
	if (originalImageData[x*3+1] + noise) < 255:
		noisyImageData.append(originalImageData[x*3+1] + noise)
	else:
		noisyImageData.append(originalImageData[x*3+1])
	if (originalImageData[x*3+2] + noise) < 255:
		noisyImageData.append(originalImageData[x*3+2] + noise)
	else:
		noisyImageData.append(originalImageData[x*3+2])

endTime = time.time()
print("Elapsed time: ", endTime - startTime)
print(len(noisyImageData))
noisyImageDataBytes = bytearray(noisyImageData)

noisyImageFile = open("noisyImage.bmp", "wb")
noisyImageFile.write(originalImageHeaderBytes)
noisyImageFile.write(noisyImageDataBytes)
noisyImageFile.close()
