# Automation-Scripts
Scripts for the automating of some file naming and formatting tasks

## Preconditions
* Python3 should be installed
* You should have permissions in your file system to rename files

## Usage

### Prefix Script
Open command prompt or terminal, navigate to the folder/directory where the script is located, and run `python prefix.py` or `python3 prefix.py`. This will open up a GUI that will look like the below image.

![Screenshot from 2022-04-08 22-07-51](https://user-images.githubusercontent.com/45480121/162555697-6b59c012-d9e1-448a-8339-78e2f0fcfd05.png)

First enter the string you would like to prepend to the beginning of each file name in the input text box. Then either select "Browse Files" or "Browse Folders". Both options will open up a file explorere where you can chose the file to open. "Browse Folders" will allow you to chose a folder in which all files in that folder will have the string prepended to the name, and "Browse Files" will allow you to chose a singular file to prepend the string to.

**Note**: When usingf the folder mode, be sure to actually click into the folder you want to open before cliking open in the explorer, do not just click teh folder once and then click open or else you will rename all of the files one folder to high.

For a more detailed insight and information on how to make a desktop shortcut for the program instead of running from the command prompt, please see [this](https://watch.screencastify.com/v/9sCturQTdoSnaCQqt6WV) video.

### Column Values Script
The GUI will look exactly the same as with the prefix script for the column script. It is operated the same as the prefix script aswell. See the video above for how to download, run, and make a shortcut for the column value script.
**Note**: For this script you will need to type the follwing into your command prompt in order for the script to run. `pip install pandas`. Then you can try to run the script. If the script does not run after the previous command, in the shortcut you create for it, under preferences and under general make sure you have python 3.10, or whatever version you are running selected an not just the default one called python.
