import tkinter as tk
from tkinter import filedialog, messagebox

current_file_path = None

def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                render_markdown(file_content)
            root.title(f"Markdown Editor - {file_path}")
            current_file_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    if current_file_path:
        write_to_file(current_file_path)
    else:
        save_file_as()

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All files", "*.*")])
    if file_path:
        write_to_file(file_path)

def write_to_file(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully")
        global current_file_path
        current_file_path = file_path
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def render_markdown(content):
    text_area.delete(1.0, tk.END)
    for line in content.split('\n'):
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
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = 700, 500
center_x, center_y = int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(True, False)

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

font_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command=lambda: text_area.config(font=("Arial", 12)))

text_area = tk.Text(root, wrap='word', font=("Arial", 12))
text_area.pack(expand=1, fill='both')

text_area.tag_config('heading1', font=('Arial', 16, 'bold'))
text_area.tag_config('heading2', font=('Arial', 14, 'bold'))

root.bind('<Control-s>', lambda event: save_file())

root.mainloop()
