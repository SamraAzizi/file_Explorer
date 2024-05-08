
# File Explorer

## Overview

This Python code provides a simple file explorer GUI built using Tkinter. It allows users to navigate through directories and view their contents.

## Features

- Navigate through directories
- View files and folders within each directory
- Click on folders to expand and view their contents
- Populates the tree view dynamically

## Usage

1. Run the `main()` function in a Python environment.
2. The file explorer GUI will open.
3. Navigate through directories by clicking on folders.
4. Files and subfolders within each directory will be displayed dynamically.

## Code Explanation

### `on_tree_open(self, event)`

This method is triggered when a user clicks on a folder in the tree view. It retrieves the path of the clicked node and populates the tree with its contents.

### `main()`

The `main()` function initializes the Tkinter application and creates an instance of the `FileExplorer` class, which represents the file explorer GUI. It then starts the main event loop using `root.mainloop()`.

## Dependencies

- Python 3.x
- Tkinter (standard Python library)

## License

This code is licensed under the MIT License. See the LICENSE file
