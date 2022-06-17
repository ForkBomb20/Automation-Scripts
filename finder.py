from tkinter import *
import pathlib

from tkinter import filedialog
from tkinter import messagebox

import pandas as pd

encodings = ["utf-8", "iso-8859-1", "latin-1", "utf-16", "utf-32", "ascii",  "cp1252"]

# Function for opening the
# file explorer window
def browseFiles():
    if not string_entry.get():
        messagebox.showwarning("Warning", "Please enter a search terms before browsing")
    else:
        terms = string_entry.get().strip().split(",")
        terms = [term.strip() for term in terms]
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File")

        file_str = ""

        if filename == ():
            pass
        else:
            if filename.endswith(".json") or filename.endswith(".csv"):
                for encoding in encodings:
                    try:
                        file_str = open(filename, encoding=encoding).read()
                        break
                    except:
                        pass
            elif filename.endswith(".xlsx"):
                df = pd.read_excel(filename)
                file_str = df.to_string()
            else:
                messagebox.showwarning("Warning", "Please select a csv, json, or xlsx file")


        contains = []

        for term in terms:
            if term in file_str:
                contains.append(term)


        label_file_explorer.configure(text="File contains " + str(contains) + " terms")

def browseDirectories():
    if not string_entry.get():
        messagebox.showwarning("Warning", "Please enter a search terms before browsing")
    else:
        terms = string_entry.get().strip().split(",")
        terms = [term.strip() for term in terms]

        directory = filedialog.askdirectory(initialdir="/",
                                            title="Select a Directory")

        output_str = ""

        if directory == ():
            pass
        else:
            path = pathlib.Path(directory)
            for file in path.iterdir():
                if str(file).endswith(".json") or str(file).endswith(".csv"):
                    for encoding in encodings:
                        try:
                            file_str = open(str(file), encoding=encoding).read()
                            break
                        except:
                            pass

                    contains = []

                    for term in terms:
                        if term in file_str:
                            contains.append(term)

                    output_str += str(file) + " " + str(contains) + "\n"

                elif str(file).endswith(".xlsx"):
                    df = pd.read_excel(str(file))
                    file_str = df.to_string()

                    contains = []

                    for term in terms:
                        if term in file_str:
                            contains.append(term)

                    output_str += str(file) + " " + str(contains) + "\n"

                else:
                    output_str += f"{str(file)} is not a json, csv, or xlsx file\n"

            new_path = path / "matches.txt"
            new_path.touch()

            with open(new_path, "w") as f:
                f.write(output_str)

            label_file_explorer.configure(text="Folder Opened: " + directory + "\nPrefix successfully added")


# Create the root window
window = Tk()

# Set window title
window.title('Term Finder')

# Set window size
window.geometry("800x200")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Term Finder: Please enter terms separated by commas. Then brows for files or folders",
                            width=100, height=4,
                            fg="blue")

button_directory = Button(window,
                        text="Browse Folders",
                        command=browseDirectories)

button_file = Button(window,
                        text="Browse Files",
                        command=browseFiles)

string_entry = Entry(window, width=40)


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


