# Flatten Folder 📂

A super handy Python tool to rescue your messy folders! From a simple script to a robust file system utility. 🚀

## Versions
* 🕒 Version 1.0: The Naive Start  
This was the first "fun" version designed for quick cleanup tasks. It gets the job done but moves fast and breaks things! 🏃💨

    * Approach:   
    Single-pass walking.
    * Logic:   
    Finds a file ➡️ Moves it immediately.
    * Best for:  
    Small, simple folders.

* 🔥 Version 2.0: The Robust Evolution (Latest)  
This is the "Pro" version inspired by systems-level engineering. It's safer, smarter, and much more stable. 🛡️✨

    🌟 Key Enhancements:  

    * 🧠 Two-pass Scanning Model:   
    Separates "thinking" from "doing". It scans the whole tree first, then executes.
    * 🛑 Atomic-like Safety:  
    No more recursive loops! Even if the output folder is inside the source, V2 handles it gracefully.
    * ⌨️ UX Improvements:  
    Added readline support to fix that annoying arrow-key bug in macOS terminals.
    * 🛰️ Smart Path Cleaning:   
    Automatically strips quotes and whitespace from your drag-and-drop inputs.

    * 📐 Engineering Behind V2 (The "CPSC 213/221" Way):  
        Unlike V1, V2 decouples directory traversal from I/O operations. By creating a metadata snapshot of all files before moving them, we avoid Race Conditions where the script might scan its own output.
* 🧹 Version 2.1: The Intelligent Cleanup (Latest)  
    The most polished version yet. After flattening, it performs a surgical cleanup of the directory tree.
    * Smart Purge:  
    Automatically removes empty subdirectories left behind.
    * Non-Destructive:     
    Uses os.rmdir to ensure only truly empty folders are deleted.
    * Post-order Traversal:   
    Deletes from leaves to root to ensure deep nesting is collapsed.

## 🛠️ How to Use (V2.1)
1. Fire up your terminal.
2. Run the script:
    ```bash
    python flatten.py
    ```
3. Drag your messy folder in.
4. Boom! 💥 Files are now safely gathered in a `FLATTENED_STASH` folder inside your directory, and all empty junk folders are gone!

## 🪄 The Magic Under the Hood
1. Scanning Phase:   
Builds a complete list of file paths in memory.
2. Execution Phase:  
Moves files one by one based on the locked snapshot.
3. Conflict Resolution:   
Still keeps your files safe with smart auto-renaming!

4. Cleanup Phase (New):   
Performs a Post-order Traversal (topdown=False) to safely remove empty parent directories without touching any files you chose to keep. 🧹