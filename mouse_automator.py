# mouse_automator.py
import pyautogui
import time
import random
import config

def main():
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True

    print("Starting MouseAutomator. Move mouse to upper-left corner to stop.")
    time.sleep(5)

    screen_width, screen_height = pyautogui.size()

    try:
        while True:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y, duration=0.5)

            scroll_amount = random.choice([config.SCROLL_AMOUNT, -config.SCROLL_AMOUNT])
            pyautogui.scroll(scroll_amount)

            print(f"Moved to ({x}, {y}) and scrolled {'up' if scroll_amount > 0 else 'down'}")
            time.sleep(config.INTERVAL_SECONDS)

    except pyautogui.FailSafeException:
        print("Script stopped by moving mouse to upper-left corner.")
    except KeyboardInterrupt:
        print("Script stopped by user (Ctrl+C).")

if __name__ == "__main__":
    main()