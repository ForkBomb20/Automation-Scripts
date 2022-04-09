from tkinter import *
import os
import pathlib

from tkinter import filedialog
from tkinter import messagebox


# Function for opening the
# file explorer window
def browseFiles():
    if not string_entry.get():
        messagebox.showwarning("Warning", "Please enter a prefix before browsing")
    else:
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File")
        if filename == ():
            pass
        else:
            path = pathlib.Path(filename)
            os.rename(path, str(path.parents[0]) + "/" + string_entry.get() + path.name)
            label_file_explorer.configure(text="File Opened: " + filename + "\nPrefix successfully added")

def browseDirectories():
    if not string_entry.get():
        messagebox.showwarning("Warning", "Please enter a prefix before browsing")
    else:
        directory = filedialog.askdirectory(initialdir="/",
                                            title="Select a Directory")

        if directory == ():
            pass
        else:
            path = pathlib.Path(directory)
            for file in path.iterdir():
                os.rename(file, str(path) + "/" + string_entry.get() + file.name)

            label_file_explorer.configure(text="Folder Opened: " + directory + "\nPrefix successfully added")


# Create the root window
window = Tk()

# Set window title
window.title('File Prefixer')

# Set window size
window.geometry("800x200")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File Prefixer",
                            width=100, height=4,
                            fg="blue")

button_directory = Button(window,
                        text="Browse Folders",
                        command=browseDirectories)

button_file = Button(window,
                        text="Browse Files",
                        command=browseFiles)

string_entry = Entry(window, width=20)


button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_directory.grid(column=1, row=3)
button_file.grid(column=1, row=2)

string_entry.grid(column=1, row=4)

button_exit.grid(column=1, row=5)

# Let the window wait for any events
window.mainloop()


