import tkinter as tk
from tkinter import filedialog, messagebox
import re

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                if file_path.endswith('.md'):
                    render_markdown(file_content)
                else:
                    render_plain_text(file_content)
            root.title(f"Markdown Editor - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def quit_app():
    root.quit()

def change_font_to_arial():
    text_area.config(font=("Arial", 12))

def render_markdown(content):
    text_area.delete(1.0, tk.END)
    
    lines = content.split('\n')
    for line in lines:
        if line.startswith('## '):
            text_area.insert(tk.END, line[3:] + '\n', 'heading2')
        elif line.startswith('# '):
            text_area.insert(tk.END, line[2:] + '\n', 'heading1')
        else:
            text_area.insert(tk.END, line + '\n')
    
def render_plain_text(content):
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, content)

root = tk.Tk()
root.title("Markdown Editor")
root.iconbitmap("favicon.ico")
root.geometry("700x500+400+300")
root.minsize(1266, 700)
root.maxsize(1266, 700)
root.resizable(True, False)

# Create a toolbar frame
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a dropdown menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Add options to the file menu
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

# Add a font menu
font_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command=change_font_to_arial)

# Create a Text widget for the editor
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

# Set default font for text area
text_area.config(font=("Arial", 12))

# Define tags for markdown
text_area.tag_config('heading1', font=('Arial', 16, 'bold'))
text_area.tag_config('heading2', font=('Arial', 14, 'bold'))

root.mainloop()
