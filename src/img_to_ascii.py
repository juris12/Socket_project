import cv2
import numpy as np
import shutil
import os
ASCII_CHARS = "@%#*+=-:. "


def get_terminal_height():
    terminal_size = shutil.get_terminal_size()
    return int(terminal_size.lines)

new_height = get_terminal_height()


def capture_image():
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Failed to open the webcam")
        return
    for _ in range(100):
        # Read a frame from the webcam
        ret, frame = cap.read()
        # Check if the frame was read successfully
        if not ret:
            print("Failed to capture frame from the webcam")
            return
        os.system('cls')
        print(img_to_ascii(frame))
    cap.release()
        

def img_to_ascii(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the scale factor
    scale_factor = new_height / gray_image.shape[0]

    # Calculate the new width based on the aspect ratio
    new_width = int(gray_image.shape[1] * scale_factor)

    # Resize the image
    resized_image = cv2.resize(gray_image, (int(new_width*2.5), new_height))


    # Convert the grayscale image to an array of pixel values
    pixel_values = resized_image.flatten()
    width = resized_image.shape[1]
    ascii_str = ""
    i=0
    for pixel_value in pixel_values:
        i += 1
        if i == width:
            ascii_str += '\n'
            i=0
        ascii_str += ASCII_CHARS[(pixel_value//25)-1]
    return ascii_str


capture_image()