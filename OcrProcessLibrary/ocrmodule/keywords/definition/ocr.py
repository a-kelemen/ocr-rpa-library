#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals
import os
from ..base import Base
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path
from ..exception import *


class OcrKeywords(Base):
	#https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e
	# TODO ez kell a dokumentacioba az installhoz

	def ocr_image(self, image, save):
		# TODO az rgba konverzio kulon keywordbe kell hogy legyen
		image_source = self._get_source(image)
		if not os.path.isfile(image_source):
			raise FileNotFoundException("File not found: " + str(image_source))
		im = Image.open(image_source)
		im = im.convert("RGBA")
		newimdata = []
		datas = im.getdata()

		for item in datas:
			if item[0] < 112 or item[1] < 112 or item[2] < 112:
				newimdata.append(item)
			else:
				newimdata.append((255, 255, 255))
		im.putdata(newimdata)

		im = im.filter(ImageFilter.MedianFilter())
		enhancer = ImageEnhance.Contrast(im)
		im = enhancer.enhance(2)
		im = im.convert('1')
		output_folder = self._get_output_folder(image_source)
		temp_image = os.path.join(output_folder, "temp_.jpg")
		im.save(temp_image)
		# hungarian - hun
		# english - eng
		text = pytesseract.image_to_string(Image.open(temp_image), config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6', lang='eng')
		#print(text)
		if not save:
			os.remove(temp_image)
		return "".join(text.splitlines())

	def image_to_black_and_white(self, image, bw_image):
		image_source = self._get_source(image)
		if not os.path.isfile(image_source):
			raise FileNotFoundException("File not found: " + str(image_source))
		im = Image.open(image_source)
		image_file = im.convert('1')
		if bw_image == "":
			image_file.save(image_source)
		else:
			try:
				new_source = self._get_source(bw_image)
				image_file.save(new_source)
			except Exception as e:
				#TODO exception.- lehet hogy nem is kell
				pass


	def convert_pdf_to_image(self, pdf, output_folder):
		pdf_file = self._get_source(pdf)
		pages = convert_from_path(pdf_file, 500)
		out_folder = self._get_path(output_folder)
		image_counter = 1
		files = []
		for page in pages:
			filename = "page_" + str(image_counter) + ".jpg"
			out_file = os.path.join(out_folder, filename)
			page.save(out_file, 'JPEG')
			image_counter += 1
			files.append(out_file)
		return files

	def ocr_pdf(self, pdf, save):
		pdf_file = self._get_source(pdf)
		if not os.path.isfile(pdf_file):
			raise FileNotFoundException("File not found: " + str(pdf_file))
		if os.path.splitext(pdf_file)[1].lower() != ".pdf":
			raise FileFormatException("Invalid file! File should be a pdf!")
		output_dir = self._get_output_folder(pdf_file)
		img_files = self.convert_pdf_to_image(pdf_file, output_dir)
		out_text = ""
		for img in img_files:
			img_text = self.ocr_image(img, save=False)
			out_text += img_text
			if not save:
				os.remove(img)
		return "".join(out_text.splitlines())



