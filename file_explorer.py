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
    
    def populate_tree(self, parent):
        if parent == "":
            parent = "/"
        parent_node = self.tree.insert("", "end", text=parent, open=False)
        try:
            for path in os.listdir(parent):
                full_path = os.path.join(parent, path)
                if os.path.isdir(full_path):
                    self.tree.insert(parent_node, "end", text=path, open=False)
                else:
                    self.tree.insert(parent_node, "end", text=path)
        except PermissionError:
            pass
    
    def on_tree_open(self, event):
        node = self.tree.focus()
        path = self.tree.item(node, "text")
        if self.tree.get_children(node):
            return
        self.populate_tree(path)

def main():
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
