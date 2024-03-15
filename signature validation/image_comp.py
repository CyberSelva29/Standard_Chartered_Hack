import cv2
import numpy as np
# from google.colab import files
from skimage.metrics import structural_similarity as ssim
from matplotlib import pyplot as plt

def are_signatures_equal(signature1, signature2):
    if signature1 is None or signature2 is None:
        raise ValueError("One or both signatures are None.")
    return np.array_equal(signature1, signature2)

def preprocess_image(image):
    # If the image is grayscale, convert it to BGR
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


def calculate_similarity(signature1, signature2):
    # Resize images to a common size
    height, width = min(signature1.shape[0], signature2.shape[0]), min(signature1.shape[1], signature2.shape[1])
    signature1_resized = cv2.resize(signature1, (width, height))
    signature2_resized = cv2.resize(signature2, (width, height))
    # Calculate Structural Similarity Index (SSIM)
    return ssim(signature1_resized, signature2_resized)


def compare_sign(original, verify):

    file_names = [original, verify]

    if len(file_names) != 2:
        print("Please upload exactly 2 signature images.")
    else:
        # Read uploaded images
        signatures = []
        signatures.append(cv2.imread(file_names[0]))
        signatures.append(cv2.imread(file_names[1]))

        # Preprocess the images
        preprocessed_signatures = [preprocess_image(signature) for signature in signatures]

        # Calculate similarity
        similarity = calculate_similarity(preprocessed_signatures[0], preprocessed_signatures[1])
        print("Similarity (SSIM):", similarity)


        # Display the original and preprocessed signatures
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 2, 1)
        plt.imshow(cv2.cvtColor(signatures[0], cv2.COLOR_BGR2RGB))
        plt.title('Original Signature 1')
        plt.axis('off')
        plt.subplot(2, 2, 2)
        plt.imshow(cv2.cvtColor(preprocessed_signatures[0], cv2.COLOR_BGR2RGB), cmap='gray')
        plt.title('Preprocessed Signature 1')
        plt.axis('off')
        plt.subplot(2, 2, 3)
        plt.imshow(cv2.cvtColor(signatures[1], cv2.COLOR_BGR2RGB))
        plt.title('Original Signature 2')
        plt.axis('off')
        plt.subplot(2, 2, 4)
        plt.imshow(cv2.cvtColor(preprocessed_signatures[1], cv2.COLOR_BGR2RGB), cmap='gray')
        plt.title('Preprocessed Signature 2')
        plt.axis('off')
        plt.show()
        if similarity > 0.4:
            print("signature matched")
            return True
        else:
            print("not matched")
            return False
        

# Enter the valid address of two images to compare
compare_sign("img.png", "extracted_images/img_13.jpg")
