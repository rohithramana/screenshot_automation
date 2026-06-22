# Screenshot Automation

A Python automation script that captures screenshots and manages storage automatically.

## What it does
- Creates a `screenshots/` folder automatically
- Takes 5 screenshots every time it runs
- Names each file with a timestamp (e.g. `screenshot_20260622_180757.png`)
- Enforces a 23-file limit — auto-deletes oldest screenshots when exceeded

## Libraries used
- `pyautogui` — screen capture
- `os` — file and folder management
- `datetime` — timestamp generation
- `time` — interval between screenshots

## How to run
1. Install dependencies: `pip install pyautogui pillow`
2. Run the script: `python D1.py`
