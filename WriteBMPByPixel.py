imageHeader = open("image.bmp", "wb")

#---------- Fill BMP header elements
BMHeader = bytes(b'BM')
sizeInBytes = bytes([54, 16, 14, 0])
reservedBytes = bytes([0, 0, 0, 0])
offsetToImageData = bytes([54, 0, 0, 0])
sizeOfBITMAPINFOHEADERStructure = bytes([40, 0, 0, 0])
imageWidth = bytes([224, 1, 0, 0])
imageHeigth = bytes([128, 2, 0, 0])
numberOfPlanes = bytes([1, 0])
bitsPerPixel = bytes([24, 0])
compresionType = bytes([0, 0, 0, 0])
sizeOfImageInBytes = bytes([0, 16, 14, 0])
horizontalResolution = bytes([0, 0, 0, 0])
verticalResolution = bytes([0, 0, 0, 0])
numberOfColors = bytes([0, 0, 0, 0])
numberOfImportantColors = bytes([0, 0, 0, 0])

#---------- Write BMP header elements to file
imageHeader.write(BMHeader)
imageHeader.write(sizeInBytes)
imageHeader.write(reservedBytes)
imageHeader.write(offsetToImageData)
imageHeader.write(sizeOfBITMAPINFOHEADERStructure)
imageHeader.write(imageWidth)
imageHeader.write(imageHeigth)
imageHeader.write(numberOfPlanes)
imageHeader.write(bitsPerPixel)
imageHeader.write(compresionType)
imageHeader.write(sizeOfImageInBytes)
imageHeader.write(horizontalResolution)
imageHeader.write(verticalResolution)
imageHeader.write(numberOfColors)
imageHeader.write(numberOfImportantColors)

#---------- Close BMP file after write BMP header
imageHeader.close()

#---------- Fill pixels for BMP image
imagePixel = [0, 0, 0]
imageData = list(640*480)
for x in range(640*480):
	imagePixel[0] = 255
	imagePixel[1] = 128
	imagePixel[2] = 64
	imageData[x] = imagePixel

imageDataBytes = bytes(imageData)

#---------- Write pixels to BMP image
imageDataFile = open("image.bmp", "ab")
imageDataFile.write(imageDataBytes)
imageDataFile.close()
