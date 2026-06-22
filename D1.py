import os
import pyautogui
from datetime import datetime
import time

folder_name = "screenshots"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created!")
else:
    print(f"Folder '{folder_name}' already exists.")

for i in range(5):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder_name}/screenshot_{timestamp}.png"
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Saved: {filename}")
    
    time.sleep(2)

files = os.listdir(folder_name)
files = [f for f in files if f.startswith("screenshot_")]
files.sort()

print(f"Total screenshots: {len(files)}")

while len(files) > 23:
    oldest_file = files[0]
    os.remove(f"{folder_name}/{oldest_file}")
    print(f"Deleted oldest: {oldest_file}")
    files.pop(0)
