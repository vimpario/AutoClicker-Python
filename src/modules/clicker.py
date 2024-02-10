import pyautogui
import keyboard
import time

def auto_click(num_clicks, interval):
    print("Start autoclicker")
    while True:
        keyboard.wait("F6")
        for _ in range(num_clicks):
            if keyboard.is_pressed("F7"):
                print("Pressed F7")
                return
            print("Clicked")
            pyautogui.click()
            time.sleep(interval)


    print("End clicking")
