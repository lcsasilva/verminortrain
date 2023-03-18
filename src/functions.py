import cv2
import pytesseract
from PIL import Image
import keyboard

monitoring = False

def start_monitoring(region1, target_number1, key1, region2, target_number2, key2):
    global monitoring
    monitoring = True

    while monitoring:
        # Implementação da lógica de monitoramento para a região 1
        img1 = Image.open(region1)
        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        number1 = pytesseract.image_to_string(img1_gray, config='--psm 6 outputbase digits')

        if target_number1 in number1:
            keyboard.press(key1)
            keyboard.release(key1)

        # Implementação da lógica de monitoramento para a região 2
        img2 = Image.open(region2)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        number2 = pytesseract.image_to_string(img2_gray, config='--psm 6 outputbase digits')

        if target_number2 in number2:
            keyboard.press(key2)
            keyboard.release(key2)

def stop_monitoring():
    global monitoring
    monitoring = False




"""def get_digits(img):
    digits = []
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)

        if aspect_ratio > 0.2 and aspect_ratio < 1.2:
            if h > 20:
                roi = img[y:y + h, x:x + w]
                _, roi = cv2.threshold(roi, 128, 255, cv2.THRESH_BINARY_INV)
                roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
                roi = roi / 255.0

                roi = roi.reshape(-1, 28, 28, 1)
                pred_array = model.predict(roi)
                digit_class = np.argmax(pred_array)

                digits.append(digit_class)

    return digits"""

