*** Settings ***
Library                      OcrProcessLibrary

*** Test Cases ***
Ocr Image Jpg
    [Tags]                   Ocr Image
    ${text}=                 Ocr Image  test_files/jpg_test.jpg
    Should Not Be Empty      ${text}

Ocr Image Png
    [Tags]                   Ocr Image
    ${text}=                 Ocr Image  test_files/png_test.png
    ${in}=                   Evaluate  "OcrProcessLibrary" in "${text}"
    Should Be True           ${in}

Ocr Pdf
    [Tags]                   Ocr Pdf
    ${text}=                 Ocr Pdf  test_files/pdf_test.pdf
    ${in}=                   Evaluate  "OcrProcessLibrary" in "".join("${text}".splitlines())
    Should Be True           ${in}

