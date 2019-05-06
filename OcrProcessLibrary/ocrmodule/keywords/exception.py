from __future__ import absolute_import, division, generators, print_function, unicode_literals


class OcrLibraryException(Exception):
	pass
	#ROBOT_SUPPRESS_NAME = True


class FileNotFoundException(OcrLibraryException):
	pass


class FileFormatException(OcrLibraryException):
	pass
