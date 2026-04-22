# Flatten Folder 📂

A super handy Python tool to rescue your messy folders! From a simple script to a robust file system utility. 🚀

## Versions
* 🕒 Version 1.0: The Naive Start
This was the first "fun" version designed for quick cleanup tasks. It gets the job done but moves fast and breaks things! 🏃💨

    * Approach: Single-pass walking.
    * Logic: Finds a file ➡️ Moves it immediately.
    * Best for: Small, simple folders.

* 🔥 Version 2.0: The Robust Evolution (Latest)
    * This is the "Pro" version inspired by systems-level engineering. It's safer, smarter, and much more stable. 🛡️✨

    * 🌟 Key Enhancements:
        * 🧠 Two-pass Scanning Model: Separates "thinking" from "doing". It scans the whole tree first, then executes.
        * 🛑 Atomic-like Safety: No more recursive loops! Even if the output folder is inside the source, V2 handles it gracefully.
        * ⌨️ UX Improvements: Added readline support to fix that annoying arrow-key bug in macOS terminals.
        * 🛰️ Smart Path Cleaning: Automatically strips quotes and whitespace from your drag-and-drop inputs.

        * 📐 Engineering Behind V2 (The "CPSC 213/221" Way):  

            Unlike V1, V2 decouples directory traversal from I/O operations. By creating a metadata snapshot of all files before moving them, we avoid Race Conditions where the script might scan its own output.

## 🛠️ How to Use (V2)
* １． Fire up your terminal.
* ２． Run the script:
｀｀｀bash
python flatten.py
｀｀｀
* ３． Drag your messy folder in.
* ４． Boom! 💥 Files are now safely gathered in a `FLATTENED_STASH` folder inside your directory.

## 🪄 The Magic Under the Hood
* １． Scanning Phase: Builds a complete list of file paths in memory.
* ２． Execution Phase: Moves files one by one based on the locked snapshot.
* ３． Conflict Resolution: Still keeps your files safe with smart auto-renaming!