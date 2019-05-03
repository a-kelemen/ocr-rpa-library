#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, print_function, unicode_literals

from .ocrmodule.keywords.definition.ocr import OcrKeywords



def keyword(name=None):
	#TODO ebbe az kell, hogy lefuttassa a keywordot, es ha sikres, akkor kiir valamit hogy sikeres hogy legyen
	#valami haszna
	if callable(name):
		return keyword()(name)

	def _method_wrapper(func):
		func.robot_name = name
		return func
	return _method_wrapper


class OcrProcessLibrary(object):
	__version__ = '0.1.0'

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = __version__

	def __init__(self):
		self.ocr = OcrKeywords()

	@keyword(name="Ocr Image")
	def ocr_image(self, image_source, save=False):
		"""
		Returns the text of the given image.

		Works correctly only with English text.

		If the optional ``save`` argument is given and True, temp image will be saved to the output folder.

		If the optional ``save`` argument is not given, temp image file will be removed.

		Examples:
		| ${text}= | `Ocr Image` |           | image_file.jpg | # returns the text of _image_file.jpg_     |
		| ${text}= | `Ocr Image` | save=True | image_file.jpg | # output folder will contain the temp file |

		Fails if the given file isn't an image.
		"""
		return self.ocr.ocr_image(image_source, save)

	@keyword(name="Image To Black And White")
	def image_to_black_and_white(self, image_source, new_source=""):
		"""
		Converts the given image to black and white.

		Examples:
		| `Image To Black And White` | color.jpg | folder/out_file.jpg | # creates a b&w image from _color.jpg_ |
		"""
		return self.ocr.image_to_black_and_white(image_source, new_source)

	@keyword(name="Convert Pdf To Image")
	def convert_pdf_to_image(self, image_source, output_dir):
		"""
		Converts the given pdf to jpg.

		Output file name format will be: page_<page_nr>.jpg

		Examples:
		| `Convert Pdf To Image` | test.pdf  | out_folder | # creates images (jpg) from _test.pdf_ |
		| `Convert Pdf To Image` | color.jpg | out_folder | # fails                                |

		Fails if the given file isn't pdf.
		"""
		return self.ocr.convert_pdf_to_image(image_source, output_dir)

	@keyword(name="Ocr Pdf")
	def ocr_pdf(self, pdf_source, save=False):
		"""
		Returns the text of the given pdf.

		Works correctly only with English text.

		If the optional ``save`` argument is given and True, temp images will be saved to the output folder.

		If the optional ``save`` argument is not given, temp image files will be removed.

		Examples:
		| ${text}= | `Ocr Pdf` |           | pdf_file.pdf | # returns the text of _pdf_file.pdf_       |
		| ${text}= | `Ocr Pdf` | save=True | pdf_file.pdf | # output folder will contain the temp file |

		Fails if the given file isn't a pdf.
		"""
		return self.ocr.ocr_pdf(pdf_source, save)



