import os
import subprocess
from tkinter import *
from tkinter.ttk import *

root = Tk()
destination = ""
url = ""
lab = ""

def dwn():
    res = entry.get('1.0', END).strip()
    print(res)
    with open('output.txt', 'w') as f:
        p1 = subprocess.run(['youtube-dl', '-f',str(137), url], stdout=f, shell=1, text=1)
    with open('output.txt', 'r') as f:
        for i in f:
            prog = i
    
    lab.config(text=prog)
    
    return

def setUrl():
    # dod
    global url,lab
    url = entry.get('1.0', END).strip()
    entry.delete('1.0', END)
    with open('output.txt', 'w') as f:
        p1 = subprocess.run(['youtube-dl', '-F', url], stdout=f, shell=1, text=1)
    # if the returncode is not 0 then some error occured
    if p1.returncode != 0:
        print(p1.stderr)
        exit()

    op = []
    with open('output.txt', 'r') as f:
        for i in f:
            if i:
                op.append(i.strip())
    s = "The available resolutions for the given video : \n\n"
    for i in op:
        print(i)
        if '240' in i and '240p' not in s:
            s += '240p'+"\n\n"
        if '640' in i and '360p' not in s:
            s += '360p'+"\n\n"
        if '854' in i and '480p' not in s:
            s += '480p'+"\n\n"
        if '1280' in i and '720p' not in s:
            s += '720p'+"\n\n"
        if '1920' in i and '1080p' not in s:
            s += '1080p'+"\n\n"

    newWindow = Toplevel(root)
    newWindow.title("Resolution")
    lab = Label(newWindow, text=s)
    lab.pack()
    label.config(text="Enter a resolution")
    button.config(text="Download", command=dwn)
    root.update()


def setLocation():
    global destination
    destination = entry.get('1.0', END).strip()
    entry.delete('1.0', END)
    os.chdir(destination)
    label.config(text="Enter the url of the video")
    button.config(text="Check it out!!", command=setUrl)
    root.update()


root.geometry("670x300")
label = Label(root, text="Enter the destination")
entry = Text(root, height=3, width=50, borderwidth=7)
button = Button(root, text="Set as Download location", command=setLocation)

label.pack(padx=20, pady=20)
entry.pack(padx=20, pady=20)
button.pack(padx=20, pady=20)

# make sure that you're running the python code in the same directory
# where you want your videos to be downloaded

# please enter the full destination
#destination = input("Enter the destination : ").strip()
# changing the destination

# copy the url from the browser and enter it here
#url = input("Enter the url : ").strip()

# creating a 'youtube-dl.conf' file
# youtube-dl needs this file to download
#open('youtube-dl.conf', 'w')


root.mainloop()
