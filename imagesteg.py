# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
from PIL import Image
import streamlit as st

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):

		# list of binary codes
		# of given data
		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		# Extracting 3 pixels at a time
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		# Pixel value should be made
		# odd for 1 and even for 0
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				# pix[j] -= 1

		# Eighth pixel of every set tells
		# whether to stop ot read further.
		# 0 means keep reading; 1 means thec
		# message is over.
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):

		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

# Encode data into image
def encode(img,data,name):
	# img = input("Enter image name(with extension) : ")
	# image = Image.open(img, 'r')

	# data = input("Enter data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')

	encode_enc(img, data)

	# new_img_name = input("Enter the name of new image(with extension) : ")
	return img.save(name, str(name.split(".")[1].upper()))

# Decode the data in the image
def decode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]

		# string of binary data
		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data

# Main Function
def main():
	st.markdown("# Image Steganography")
	tab1,tab2 = st.tabs(["Encode","Decode"])

	with tab1:
		st.header("Encode Image")
		img=st.file_uploader("Upload Image",type=['png','jpg','jpeg'])
		text_input = st.text_input(
        "Enter text to Encode",)
		if text_input:
			data = text_input
		img_name = st.text_input(
        "Enter the Encoded Image Name with format of the image:",)
		if img_name:
			name=img_name
		if img is not None:
			newimg=encode(img, data,name)
			st.success("Image Encoded Successfully")
			st.download_button(
				label="Download Image",
				data=newimg,
				file_name=img_name,
				mime='image/png/jpg/jpeg',
			)
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")

# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
