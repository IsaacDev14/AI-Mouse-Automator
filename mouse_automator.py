# mouse_automator.py
import pyautogui
import time
import random
import threading
import tkinter as tk
import config
import sys

class MouseAutomatorApp:
    def __init__(self, root):
        print("Initializing GUI...")
        self.root = root
        self.root.title("Mouse Automator")
        self.is_running = False
        self.automation_thread = None

        # Simple GUI
        self.label = tk.Label(root, text="Mouse Automator: Click Quit or move mouse to upper-left to stop.")
        self.label.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.stop_automation)
        self.quit_button.pack(pady=5)

        # Start automation
        print("Starting automation thread...")
        self.is_running = True
        self.automation_thread = threading.Thread(target=self.automate_mouse)
        self.automation_thread.daemon = True
        self.automation_thread.start()
        print("GUI and automation initialized.")

    def automate_mouse(self):
        print("Setting up PyAutoGUI...")
        try:
            pyautogui.PAUSE = 0.5
            pyautogui.FAILSAFE = True
            screen_width, screen_height = pyautogui.size()
            print(f"Screen size: {screen_width}x{screen_height}")

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
            print(f"Automation error: {e}")
            self.stop_automation()

    def stop_automation(self):
        print("Stopping automation...")
        self.is_running = False
        self.root.quit()
        print("Application stopped.")

def main():
    try:
        print("Creating Tkinter window...")
        root = tk.Tk()
        root.geometry("300x100")
        app = MouseAutomatorApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to start GUI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting MouseAutomator...")
    main()