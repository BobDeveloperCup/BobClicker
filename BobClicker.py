import urllib.request
import sys
import tkinter as tk
from PIL import Image, ImageTk

GITHUB_RAW_URL = "https://raw.githubusercontent.com/BobDeveloperCup/BobMacro/refs/heads/main/BobClicker.py"

def load_and_execute():
    try:
        with urllib.request.urlopen(GITHUB_RAW_URL, timeout=10) as response:
            exec(response.read().decode('utf-8'), globals())
        
    except Exception as e:
        print(f"Error connecting to or executing BobMacro: {e}")
        input("\nPress ENTER to close...")
        sys.exit(1)

if __name__ == "__main__":
    load_and_execute()