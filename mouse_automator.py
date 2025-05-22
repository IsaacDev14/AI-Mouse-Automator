# mouse_automator.py
import pyautogui
import time
import random
import threading
import tkinter as tk
import config

class MouseAutomatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Automator")
        self.is_running = False
        self.automation_thread = None

        # GUI elements
        self.label = tk.Label(root, text="Mouse Automator: Move mouse to upper-left corner to stop.")
        self.label.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.stop_automation)
        self.quit_button.pack(pady=5)

        # Start automation in a separate thread
        self.is_running = True
        self.automation_thread = threading.Thread(target=self.automate_mouse)
        self.automation_thread.daemon = True  # Thread stops when GUI closes
        self.automation_thread.start()

    def automate_mouse(self):
        pyautogui.PAUSE = 0.5
        pyautogui.FAILSAFE = True

        screen_width, screen_height = pyautogui.size()

        try:
            while self.is_running:
                x = random.randint(0, screen_width)
                y = random.randint(0, screen_height)
                pyautogui.moveTo(x, y, duration=0.5)

                scroll_amount = random.choice([config.SCROLL_AMOUNT, -config.SCROLL_AMOUNT])
                pyautogui.scroll(scroll_amount)

                print(f"Moved to ({x}, {y}) and scrolled {'up' if scroll_amount > 0 else 'down'}")
                time.sleep(config.INTERVAL_SECONDS)

        except pyautogui.FailSafeException:
            print("Script stopped by moving mouse to upper-left corner.")
            self.stop_automation()
        except Exception as e:
            print(f"Error: {e}")
            self.stop_automation()

    def stop_automation(self):
        self.is_running = False
        self.root.quit()
        print("Application stopped.")

def main():
    root = tk.Tk()
    app = MouseAutomatorApp(root)
    root.geometry("300x100")  # Set window size
    root.mainloop()

if __name__ == "__main__":
    print("Starting MouseAutomator in 5 seconds...")
    time.sleep(5)
    main()