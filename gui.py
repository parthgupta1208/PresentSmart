import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pdf2final_list
import text2ppt
import shutil
import os

def select_file():
    global button,window,exit_button
    button.config(text='Processing...')
    exit_button.destroy()
    file_path = filedialog.askopenfilename(
        initialdir='/', title='Select a file', filetypes=[('PDF files', '*.pdf')])
    try:
        with open(file_path, 'rb') as file:
            print({file_path})
    except:
        messagebox.showerror("ERROR","Cannot Open File")
    else:
        try:
            x = pdf2final_list.process(file_path)
            print("\n\n", x)
            text2ppt.presentate(x)
            file_path = filedialog.asksaveasfilename(defaultextension='.pptx',
                                                    filetypes=[('PowerPoint files', '*.pptx'),
                                                                ('All files', '*.*')])
            shutil.copy("PPT.pptx",file_path)
            messagebox.showinfo("SUCCESS", "File Saved Successfully")
            os.startfile(file_path)
        except Exception as e:
            messagebox.showerror("ERROR", e)
    button.config(text='Select a PDF to Proceed With')
    exit_button = tk.Button(window, text='Exit', command=window.quit, font=('Arial', 12, 'bold'), fg='#f2f2f2', bg='#ff3333', padx=20, pady=10, borderwidth=0, relief='groove')
    exit_button.grid(row=2, column=0, pady=20,padx=60,sticky="news")


# Create the Tkinter window
window = tk.Tk()
window.title("PDF2PPT Generator")
# window.geometry('300x')
window.configure(bg='#f2f2f2')

# Set the window to always be on top
window.attributes('-topmost', 1)
# make the window titlebarless
window.overrideredirect(True)
# dont launch the window in top left corner but center of the screen
window.eval('tk::PlaceWindow . center')

# Create a button widget that triggers the select_file() function when clicked
button = tk.Button(window, text='Select a PDF to Proceed With', command=select_file, font=('Arial', 12, 'bold'), fg='#f2f2f2', bg='#333333', padx=20, pady=10, borderwidth=0, relief='groove')
button.grid(row=1, column=0, pady=30,sticky="news",padx=20)

# Create an exit button widget
exit_button = tk.Button(window, text='Exit', command=window.quit, font=('Arial', 12, 'bold'), fg='#f2f2f2', bg='#ff3333', padx=20, pady=10, borderwidth=0, relief='groove')
exit_button.grid(row=2, column=0, pady=20,padx=60,sticky="news")

# Add a hover effect to the exit button
def on_enter_exit(e):
    exit_button.config(bg='#ff5555')
def on_leave_exit(e):
    exit_button.config(bg='#ff3333')
exit_button.bind('<Enter>', on_enter_exit)
exit_button.bind('<Leave>', on_leave_exit)
button.config(bg='#333333', fg='#f2f2f2')

# Add a hover effect to the button
def on_enter(e):
    button.config(bg='#555555')
def on_leave(e):
    button.config(bg='#333333')
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)

# Run the Tkinter event loop
window.mainloop()