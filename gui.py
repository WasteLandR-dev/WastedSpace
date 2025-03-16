import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from builder import scan_directory

def browse_directory(entry):
    path = tkinter.filedialog.askdirectory()
    if path:
        entry.delete(0, "end")
        entry.insert(0, path)

def resize_treeview(event):
    new_width = event.width
    treeview.column("#0", width=new_width - 100)
    treeview.column("size", width=100)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Disk Usage Analyzer")
    
    # Configure theme and styles
    style = ttk.Style(root)
    style.theme_use('clam')
    
    # Custom styling
    style.configure('.', background='#333333', foreground='white')
    style.configure('TLabel', background='#333333', foreground='white', font=('Segoe UI', 10))
    style.configure('TEntry', fieldbackground='#454545', foreground='white', borderwidth=0)
    style.configure('TButton', background='#4CAF50', foreground='white', font=('Segoe UI', 10), padding=6)
    style.map('TButton', background=[('active', '#45a049'), ('pressed', '#398439')])
    style.configure('Treeview', background='#454545', foreground='white', fieldbackground='#454545', borderwidth=0)
    style.configure('Treeview.Heading', background='#2C2C2C', foreground='white', font=('Segoe UI', 10, 'bold'))
    style.map('Treeview', background=[('selected', '#4CAF50')], foreground=[('selected', 'white')])

    # Configure grid layout
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Widgets
    path_label = ttk.Label(root, text="Directory path:")
    path_entry = ttk.Entry(root, width=50)
    browse_button = ttk.Button(root, text="Browse", command=lambda: browse_directory(path_entry))
    scan_button = ttk.Button(root, text="Scan", command=lambda: scan_directory(path_entry.get(), treeview, status_label))
    status_label = ttk.Label(root, text="", style='TLabel')
    
    # Treeview setup
    treeview = ttk.Treeview(root, columns=("size",))  # Remove show='headings'
    treeview.heading("#0", text="Name", anchor='w')
    treeview.heading("size", text="Size", anchor='e')
    treeview.column("#0", width=300, anchor='w')  # Explicit width for Name column
    treeview.column("size", width=100, anchor='e')

    # Grid layout
    path_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
    path_entry.grid(row=0, column=1, padx=5, pady=10, sticky='ew')
    browse_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')
    scan_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='ew')
    status_label.grid(row=2, column=0, columnspan=3, pady=5)
    treeview.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

    root.mainloop()