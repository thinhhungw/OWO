import pyautogui
import pygetwindow as gw
import random
import time

r1 = ["owoh", "owohunt", "oh", "ohunt"]
r2 = ["owobattle", "owob", "obattle", "ob"]
r3 = ["opray", "owopray"]
r4 = ["owobuy 1", "obuy 1"]
r5 = ["owocruse <@408785106942164992>", "ocruse <@408785106942164992>"]
r6 = ["owo", "uwu"]

window_title = "Discord"
windows = [window for window in pyautogui.getAllWindows() if window_title in window.title]

if len(windows) > 0:
    ds_window = windows[0]

    for _ in range(3000):
        try:
            ds_window.activate()

            ss = random.randint(1, 23)
            sequence = [
                random.choice(r1),
                random.choice(r4),
                random.choice(r6),
                random.choice(r2),
                random.choice(r3),
                random.choice(r5)
            ]
            random.shuffle(sequence)

            for command in sequence:
                pyautogui.typewrite(command + "\n")
                time.sleep(random.randint(2, 4))

            time.sleep(random.randint(15, 20))

        except Exception as e:
            print(f"Lỗi xảy ra: {e}")
else:
    print(f"Không tìm thấy cửa sổ '{window_title}' hoặc '{window_title2}'.")
