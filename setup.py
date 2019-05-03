import setuptools

setuptools.setup(name='ocrprocesslibrary',
      version='0.1',
      description='Library for ocr automation.',
      url='',
      author='Andras Kelemen',
      author_email='kelemenandras11@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(exclude=['OcrProcessLibrary.tests']),

      install_requires=[
        'robotframework',
        'pytesseract',
        'pdf2image'
      ],
      test_suite="tests",
      tests_require=['nose'],
      zip_safe=False
      )