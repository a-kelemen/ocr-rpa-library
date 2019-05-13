#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals
import os
import unittest
from OcrProcessLibrary.ocrmodule.keywords.exception import *
from OcrProcessLibrary import OcrProcessLibrary


class TestDataKeywords(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestDataKeywords, self).__init__(*args, **kwargs)
		self.ocrLib = OcrProcessLibrary()

	def test_ocr_image_png_lowercase(self):
		"""Ocr Image"""
		img_text = self.ocrLib.ocr_image("test_files/png_test.png")
		self.assertIn("ocrprocesslibrary", img_text.lower())

	def test_ocr_image_png_uppercase(self):
		"""Ocr Image"""
		img_text = self.ocrLib.ocr_image("test_files/png_test.png")
		self.assertIn("OcrProcessLibrary", img_text)

	def test_ocr_image_jpg_lowercase(self):
		"""Ocr Image"""
		img_text = self.ocrLib.ocr_image("test_files/jpg_test.jpg")
		self.assertIn("ocrprocesslibrary", img_text.lower())

	def test_ocr_image_jpg_uppercase(self):
		"""Ocr Image"""
		img_text = self.ocrLib.ocr_image("test_files/jpg_test.jpg")
		self.assertIn("OcrProcessLibrary", img_text)

	def test_ocr_image_color(self):
		"""Ocr Image"""
		img_text = self.ocrLib.ocr_image("test_files/color_test.png")
		self.assertIn("Digital Channel", img_text)

	def test_image_to_bw(self):
		"""Image To Black And White"""
		self.ocrLib.image_to_black_and_white("test_files/color_test.png", "test_files/test_img_bw.png")
		test_dir = os.path.dirname(__file__)
		is_file = os.path.isfile(os.path.join(test_dir, 'test_files', 'test_img_bw.png'))
		self.assertTrue(is_file)

	def test_pdf_to_jpg_1(self):
		"""Convert Pdf To Image"""
		self.ocrLib.convert_pdf_to_image("test_files/pdf_test.pdf", "test_files")
		test_dir = os.path.dirname(__file__)
		is_file = os.path.isfile(os.path.join(test_dir, 'test_files', 'page_1.jpg'))
		self.assertTrue(is_file)

	def test_ocr_pdf_lowercase(self):
		"""Ocr Pdf"""
		pdf_text = self.ocrLib.ocr_pdf("test_files/pdf_test.pdf")
		self.assertIn("ocrprocesslibrary", pdf_text.lower())

	def test_ocr_pdf_uppercase(self):
		"""Ocr Pdf"""
		pdf_text = self.ocrLib.ocr_pdf("test_files/pdf_test.pdf")
		self.assertIn("OcrProcessLibrary", pdf_text)

	def test_ocr_pdf_jpg(self):
		"""Ocr Pdf"""
		with self.assertRaises(FileFormatException):
			self.ocrLib.ocr_pdf("test_files/jpg_test.jpg")

	def test_ocr_pdf_png(self):
		"""Ocr Pdf"""
		with self.assertRaises(FileFormatException):
			self.ocrLib.ocr_pdf("test_files/png_test.png")

	def test_ocr_pdf_non_existing(self):
		"""Ocr Pdf"""
		with self.assertRaises(FileNotFoundException):
			self.ocrLib.ocr_pdf("test_files/non_existing.pdf")

	@classmethod
	def tearDownClass(cls):
		test_dir = os.path.dirname(__file__)
		test_files_dir = os.path.join(test_dir, 'test_files')
		files = os.listdir(test_files_dir)
		for f in files:
			if f not in ["pdf_test.pdf", "jpg_test.jpg", "png_test.png", "color_test.png"]:
				os.remove(os.path.join(test_files_dir, f))


if __name__ == '__main__':
	unittest.main()
