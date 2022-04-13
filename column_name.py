import pandas as pd
from tkinter import *
import pathlib

from tkinter import filedialog
from tkinter import messagebox


# Function for opening the
# file explorer window
def browseFiles():
    # if not string_entry.get():
    #     messagebox.showwarning("Warning", "Please enter a prefix before browsing")
    # else:
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File")
    if filename == ():
        pass
    else:
        if filename.endswith(".csv"):
            df = pd.read_csv(filename)
            df[df.columns[0]] = filename.split("/")[-1].split(".")[0]
            df.to_csv(filename, index=False)
            label_file_explorer.configure(text="File Opened: " + filename + "\nRow values set")
        else:
            messagebox.showwarning("Warning", "Please select a csv file")


def browseDirectories():
    # if not string_entry.get():
    #     messagebox.showwarning("Warning", "Please enter a prefix before browsing")
    # else:
    directory = filedialog.askdirectory(initialdir="/",
                                        title="Select a Directory")

    if directory == ():
        pass

    else:
        path = pathlib.Path(directory)
        # Check if all files are csv files if not raise warning
        for file in path.iterdir():
            if file.suffix != ".csv":
                messagebox.showwarning("Warning", "Please select only csv files")
                return
        # If all files are csv files then set the prefix
        for file in path.iterdir():
            df = pd.read_csv(file)
            df[df.columns[0]] = file.name.split(".")[0]
            df.to_csv(file, index=False)
        label_file_explorer.configure(text="Directory Opened: " + directory + "\nRow values set")


# Create the root window
window = Tk()

# Set window title
window.title('Column Values')

# Set window size
window.geometry("800x200")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Column Values",
                            width=100, height=4,
                            fg="blue")

button_directory = Button(window,
                        text="Browse Folders",
                        command=browseDirectories)

button_file = Button(window,
                        text="Browse Files",
                        command=browseFiles)

# string_entry = Entry(window, width=20)


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

# string_entry.grid(column=1, row=4)

button_exit.grid(column=1, row=5)

# Let the window wait for any events
window.mainloop()
