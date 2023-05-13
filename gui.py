import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pdf2final_list
import text2ppt
import shutil
import os

def exec(*args):
    global label,ent,window,exit_button
    exit_button.config(text='Processing...')
    try:
        intext=ent.get()
        ent.destroy()
        label.destroy()
        window.update()
        if "," in intext:
            l1=[_.strip() for _ in intext.split(",")]
        else:
            l1=[intext]
        print(l1)
        x=pdf2final_list.process(l1)
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
    exit_button.config(text='Exit')
    ent = tk.Entry(window, font=('Arial', 24, 'bold'), fg='#f2f2f2', bg='#333333', borderwidth=0, relief='groove')
    ent.grid(row=2, column=0, pady=30,sticky="news",padx=20)
    label = tk.Label(window, text='Enter comma seperated topics', font=('Arial', 12, 'bold'), fg='#333333', bg='#f2f2f2')
    label.grid(row=1, column=0, pady=20,padx=20,sticky="news")
    ent.bind('<Return>', exec)


# Create the Tkinter window
window = tk.Tk()
window.title("PDF2PPT Generator")
# window.geometry('300x')
window.configure(bg='#f2f2f2')

# make the window titlebarless
window.overrideredirect(True)
# dont launch the window in top left corner but center of the screen
window.eval('tk::PlaceWindow . center')

# Create a label asking for comma seperated topics
label = tk.Label(window, text='Enter Comma-Seperated Topics', font=('Arial', 20, 'bold'), fg='#333333', bg='#f2f2f2')
label.grid(row=1, column=0, pady=(20,5),padx=20,sticky="news")

# Create a button widget that triggers the select_file() function when clicked
ent = tk.Entry(window, font=('Arial', 24, 'bold'), fg='#f2f2f2', bg='#333333', borderwidth=0, relief='groove')
ent.grid(row=2, column=0, pady=(30,15),sticky="news",padx=20)

# Create an exit button widget
exit_button = tk.Button(window, text='Exit', command=window.quit, font=('Arial', 12, 'bold'), fg='#f2f2f2', bg='#ff3333', padx=20, pady=10, borderwidth=0, relief='groove')
exit_button.grid(row=3, column=0, pady=(20,20),padx=60,sticky="news")

# Add a hover effect to the exit button
def on_enter_exit(e):
    exit_button.config(bg='#ff5555')
def on_leave_exit(e):
    exit_button.config(bg='#ff3333')
exit_button.bind('<Enter>', on_enter_exit)
exit_button.bind('<Leave>', on_leave_exit)

ent.bind('<Return>', exec)

# Run the Tkinter event loop
window.mainloop()