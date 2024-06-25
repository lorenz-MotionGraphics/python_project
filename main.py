import tkinter as tk
from tkinter import filedialog, messagebox
import re

# Variable to store the current file path
current_file_path = None

def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                if file_path.endswith('.md'):
                    render_markdown(file_content)
                else:
                    render_plain_text(file_content)
            root.title(f"Markdown Editor - {file_path}")
            current_file_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    global current_file_path
    if current_file_path:
        try:
            with open(current_file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")
    else:
        save_file_as()

def save_file_as():
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully")
            current_file_path = file_path
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
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 500
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.minsize(500, 500)
root.maxsize(500, 500)
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
file_menu.add_command(label="Save As", command=save_file_as)
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

# Bind Ctrl+S to save the file
root.bind('<Control-s>', lambda event: save_file())

root.mainloop()
