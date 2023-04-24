import json
jsondata = {
"data": [],
"textures": []
}
filename = input("Enter xcod name: ")
with open(filename, "rb") as fh:
	data = fh.read().hex()
	picCount = int(data[10:12], 16)
	parse = 7
	parseWidth = 8
	parseWidth2 = 9
	parseHeight = 10
	parseHeight2 = 11
	for i in range(picCount):
		fh.seek(parse)
		pixelType = fh.read(1)
		fh.seek(parseWidth)
		width1 =  fh.read(1)
		width1 = int.from_bytes(width1, byteorder="little")
		width1 *= 256
		fh.seek(parseWidth2)
		width2 =  fh.read(1)
		width2 = int.from_bytes(width2, byteorder="little")
		fh.seek(parseHeight)
		height1 =  fh.read(1)
		height1 = int.from_bytes(height1, byteorder="little")
		height1 *= 256
		fh.seek(parseHeight2)
		height2 =  fh.read(1)
		height2 = int.from_bytes(height2, byteorder="little")
		height = height1 + height2
		width = width1 + width2
		pixelType = int.from_bytes(pixelType, byteorder="little")
		texture = {
		"pixelType": pixelType,
		"width": width,
		"height": height
		}
		jsondata["textures"].append(texture)
		parse += 6
		parseHeight += 6
		parseHeight2 += 6
		parseWidth += 6
		parseWidth2 += 6
picData = {
"pictureCount": picCount
}
jsondata["data"].append(picData)
jsonfile = json.dumps(jsondata, indent=4)
filename = filename.replace(".xcod", ".json")
with open(filename, "w") as fh:
	fh.write(jsonfile)