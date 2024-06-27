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
                render_plain_text(file_content)
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

def render_plain_text(content):
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, content)
    update_line_numbers()

def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state=tk.NORMAL)
    line_number_bar.delete(1.0, tk.END)
    line_number_bar.insert(tk.END, line_numbers)
    line_number_bar.config(state=tk.DISABLED)

def get_line_numbers():
    output = ''
    row, col = text_area.index('end-1c').split('.')
    for i in range(1, int(row)):
        output += str(i) + '\n'
    if not output:
        output = '1\n'  # Display 1 when the editor is empty
    return output

root = tk.Tk()
root.title("Text Editor")
root.iconbitmap("favicon.ico")
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = 700, 500
center_x, center_y = int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(True, False)

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

# Create a frame for the text area and line numbers
frame = tk.Frame(root)
frame.pack(expand=1, fill='both')

# Create a Text widget for line numbers
line_number_bar = tk.Text(frame, width=4, padx=3, takefocus=0, border=0, background='lightgrey', state='disabled')
line_number_bar.pack(side='left', fill='y')

# Create a Text widget for the editor
text_area = tk.Text(frame, wrap='word', font=("Arial", 12))
text_area.pack(expand=1, fill='both', side='right')

# Bind events to update line numbers
text_area.bind('<KeyRelease>', update_line_numbers)
text_area.bind('<MouseWheel>', update_line_numbers)
text_area.bind('<Button-1>', update_line_numbers)
text_area.bind('<Return>', update_line_numbers)
text_area.bind('<BackSpace>', update_line_numbers)
text_area.bind('<Delete>', update_line_numbers)

root.bind('<Control-s>', lambda event: save_file())

# Initial call to update line numbers
update_line_numbers()

root.mainloop()
