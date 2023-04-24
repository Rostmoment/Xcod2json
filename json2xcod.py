import json, binascii
multiple = 256
file = input("Enter json name: ")
with open(file) as fh:
    jsondata = json.load(fh)
piccount = jsondata["data"][0]["pictureCount"]
if piccount == 1:
	skip = "01"
elif piccount > 1:
	skip = "1C"
piccount = hex(piccount)
piccount = piccount.replace("0x", "")
if len(piccount) == 1:
	piccount = "0" + piccount
file = file.replace(".json", ".xcod")
with open(file, "wb") as fh:
	fh.write(binascii.unhexlify("58434F4400" + piccount))
textures = jsondata['textures']
for texture in textures:
	with open(file, 'rb') as fh:
		xcod = fh.read().hex()
	pixelType = texture["pixelType"]
	if len(str(pixelType)) == 1:
		pixelType = "0" + str(pixelType)
	pixelType = str(pixelType)
	height = texture["height"]
	width = texture["width"]
	width1 = (width // multiple) * multiple
	width2 = width - width1
	height1 = (height // multiple) * multiple
	height2 = height - height
	width1 = width1 / 256
	height1 = height1 / 256
	width1, height1 = int(width1), int(height1)
	width1, width2, height1, height2 = hex(width1), hex(width2), hex(height1), hex(height2)
	xcod, width1, width2, height1, height2 = str(xcod), str(width1), str(width2), str(height1), str(height2)
	width1, width2, height1, height2 = width1.replace("0x", ""), width2.replace("0x", ""), height1.replace("0x", ""), height2.replace("0x", "")
	if len(width1) == 1:
		width1 = "0" + width1
	if len(width2) == 1:
		width2 = "0" + width2
	if len(height1) == 1:
		height1 = "0" + height1
	if len(height2) == 1:
		height2 = "0" + height2
	data = skip + pixelType + width1 + width2 + height1 + height2
	xcoddata = xcod + data
	with open(file, "wb") as fh:
		fh.write(binascii.unhexlify(xcoddata))