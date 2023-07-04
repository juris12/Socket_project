import cv2
import numpy as np
import shutil
import os

ASCII_CHARS = "@%#*+=-:. "


def get_terminal_height():
    terminal_size = shutil.get_terminal_size()
    return int(terminal_size.lines)


new_height = get_terminal_height()


def capture_image(camera):
    ret, frame = camera.read()
    if not ret:
        return "Failed to capture frame from the webcam"
    return img_to_ascii(frame)


def img_to_ascii(image):
    """
    Returns str representing given img

    propertis:
    image: cv2 img
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    scale_factor = new_height / gray_image.shape[0]
    new_width = int(gray_image.shape[1] * scale_factor)
    resized_image = cv2.resize(gray_image, (int(new_width * 2), new_height))

    # Convert the grayscale image to an array of pixel values
    pixel_values = resized_image.flatten()
    width = resized_image.shape[1]
    ascii_str = ""
    i = 0
    for pixel_value in pixel_values:
        i += 1
        if i == width:
            ascii_str += "\n"
            i = 0
        ascii_str += ASCII_CHARS[(pixel_value // 25) - 1]
    return ascii_str


if __name__ == "__main__":
    print("camera loading....")
    cap = cv2.VideoCapture(0)
    print("camera redy....")
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Failed to open the webcam")
    else:
        for _ in range(100):
            os.system("cls")
            print(capture_image(cap))
        cap.release()
