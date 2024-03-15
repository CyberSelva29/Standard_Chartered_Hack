import pytesseract
from pytesseract import Output
import cv2


def Text_recog(img_path):
    # Read image to extract text from image
    img = cv2.imread(img_path)
    # Resize the image if required
    img = cv2.resize(img, (250,60))
    # Convert image to grey scale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Converting grey image to binary image by Thresholding
    thresh_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # configuring parameters for tesseract
    custom_config = r'--oem 3 --psm 11'

    # Get all OCR output information from pytesseract
    ocr_output_details = pytesseract.image_to_data(thresh_img, output_type = Output.DICT, config=custom_config, lang='eng')
    return ocr_output_details['text']
