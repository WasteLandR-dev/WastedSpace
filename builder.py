from pathlib import Path
import sys

class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def sort_children(self):
        self.children.sort(key=lambda x: x.size, reverse=True)

def build_tree(path):
    node = Node(str(path))
    if path.is_symlink():
        node.size = path.stat().st_size
    else:
        if path.is_file():
            node.size = path.stat().st_size
        elif path.is_dir():
            for item in path.iterdir():
                child = build_tree(item)
                node.add_child(child)
                node.size += child.size
    return node

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def print_tree(node, depth=0):
    print(' ' * depth + node.name + ": " + format_size(node.size))
    node.sort_children()
    for child in node.children:
        print_tree(child, depth + 1)

def sort_tree(node):
    node.sort_children()
    for child in node.children:
        sort_tree(child)

def populate_treeview(treeview, node, parent_item=""):
    item_id = treeview.insert(parent_item, "end", text=node.name, values=(format_size(node.size),))
    for child in node.children:
        populate_treeview(treeview, child, item_id)



def scan_directory(path_str, treeview, status_label):
    status_label.config(text="Scanning...")
    try:
        path = Path(path_str)
        if not path.exists():
            status_label.config(text="Path does not exist.")
            return
        root_node = build_tree(path)
        sort_tree(root_node)
        treeview.delete(*treeview.get_children())
        populate_treeview(treeview, root_node)
        status_label.config(text="Scan complete.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python disk_usage.py <path>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Path {path} does not exist.")
        sys.exit(1)
    root_node = build_tree(path)
    sort_tree(root_node)
    print_tree(root_node)