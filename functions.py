import pyautogui
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def capture_region(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def ocr_image(image):
    text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    return text

def monitor_numbers(target_number1, keypress1, region1, target_number2, keypress2, region2):
    while True:
        screenshot1 = capture_region(region1)
        recognized_numbers1 = ocr_image(screenshot1)

        if str(target_number1) in recognized_numbers1:
            pyautogui.press(keypress1)

        screenshot2 = capture_region(region2)
        recognized_numbers2 = ocr_image(screenshot2)

        if str(target_number2) in recognized_numbers2:
            pyautogui.press(keypress2)

def select_region():
    root = tk.Tk()
    root.withdraw()
    region = filedialog.askopenfilename()
    return region


monitoring = False

def stop_monitoring():
    global monitoring
    monitoring = False
