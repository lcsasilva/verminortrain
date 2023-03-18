import tkinter as tk
from tkinter import filedialog
from functions import find_image_on_screen, monitor_numbers

def browse_image(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

def start_monitoring(region1, target_number1, key1, region2, target_number2, key2):
    global monitoring
    monitoring = True

    def monitor_numbers(region, target_number, key):
        global monitoring
        while monitoring:
            screenshot = capture_region(region)
            recognized_numbers = ocr_image(screenshot)

            if str(target_number) in recognized_numbers:
                pyautogui.press(key)

    thread1 = threading.Thread(target=monitor_numbers, args=(region1, target_number1, key1))
    thread2 = threading.Thread(target=monitor_numbers, args=(region2, target_number2, key2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

