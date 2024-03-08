import cv2
import easyocr


def read_and_process_image(image_path):
    # Read the image
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print(f"Error: Unable to read the image at {image_path}")
        return None

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    blurred_image = cv2.medianBlur(grayscale_image, 5)  # You can adjust the kernel size (5 in this case)

    return original_image, grayscale_image, blurred_image

# Example usage:
image_path = "path/to/your/image.jpg"
original, grayscale, blurred = read_and_process_image(image_path)

# Display the images (optional)
cv2.imshow("Original Image", original)
cv2.imshow("Grayscale Image", grayscale)
cv2.imshow("Blurred Image", blurred)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()


# -----------------------

def extract_text_from_image(image_path, language='en'):
    # Create an EasyOCR reader instance
    reader = easyocr.Reader([language])

    # Read text from the image
    result = reader.readtext(image_path)

    # Extract and print the text
    extracted_text = ""
    for detection in result:
        text = detection[1]
        extracted_text += text + " "

    return extracted_text.strip()

# Example usage:
image_path = "path/to/your/image.jpg"
extracted_text = extract_text_from_image(image_path)

# Display the extracted text in the console
print("Extracted Text:")
print(extracted_text)
