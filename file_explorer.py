import os
import tkinter as tk
from tkinter import filedialog, ttk

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        
        self.tree = ttk.Treeview(root)
        self.tree.heading("#0", text="Directory Structure", anchor='w')
        self.tree.bind("<<TreeviewOpen>>", self.on_tree_open)
        
        self.populate_tree(os.path.expanduser('~'))  # Start with home directory
        
        self.tree.pack(expand=True, fill='both')
    
