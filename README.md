# Flatten Folder 📂

A super handy Python script to rescue your messy folders! 🚀 It digs into all those annoying subdirectories and brings every single file out into the light. Perfect for cleaning up those chaotic Canvas course downloads! 🎓

## What can it do? ✨
* 🔍 Deep Search: It goes through every layer of subfolders.
* 📦 One-Stop Shop: Moves everything into a single folder for easy access.
* 🛡️ No Overwriting: If it finds two files with the same name, it smartly adds a number so nothing gets lost!

## How to use it? 🛠️
* １. Fire up your terminal.
* ２. Run the script:
    ```bash
    python flatten.py
    ```
* ３. Drag your messy folder in when it asks.
* ４. Boom! 💥 A new folder named `[original]_flattened` will appear right next to it!

## How it works (The Magic 🪄)
This script uses a straightforward approach:
* １. It starts a directory walk using os.walk.
* ２. Every time it spots a file, it calculates the new path and moves it immediately! 🏃💨