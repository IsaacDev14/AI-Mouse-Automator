# mouse_automator.py
import pyautogui
import time
import random

def main():
    # Set PyAutoGUI pause for safety
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True

    print("Starting MouseAutomator. Move mouse to upper-left corner to stop.")
    time.sleep(5)  # Give user time to prepare

    screen_width, screen_height = pyautogui.size()

    try:
        while True:
            # Move mouse to random position
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y, duration=0.5)

            # Random scroll
            scroll_amount = random.choice([100, -100])
            pyautogui.scroll(scroll_amount)

            print(f"Moved to ({x}, {y}) and scrolled {'up' if scroll_amount > 0 else 'down'}")
            time.sleep(10)  # Wait 10 seconds

    except pyautogui.FailSafeException:
        print("Script stopped by moving mouse to upper-left corner.")
    except KeyboardInterrupt:
        print("Script stopped by user (Ctrl+C).")

if __name__ == "__main__":
    main()