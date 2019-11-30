import tkinter as tk
import os, sys, subprocess, webbrowser
from tkinter import filedialog, Text

root = tk.Tk()
root.title("Text Bunch")
apps = []

def addApp():
	children = frame.winfo_children()
	for child in children:
		child.destroy()

	filename = filedialog.askopenfile()
	apps.append(filename.name)
	for app in apps:
		label = tk.Label(frame, text=app, fg="white", bg="#111110")
		label.pack()
def runIt():
	for app in apps:
		os.system("open "+app)
def clr():
	children = frame.winfo_children()
	for child in children:
		child.destroy()
	apps.clear()
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="#263D42", bg="red", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Files", padx=10, pady=5, fg="#263D42", bg="red", command=runIt)
runApps.pack()

clrbtn = tk.Button(root, text="Clear", padx=10, pady=5, fg="#263D42", bg="red", command=clr)
clrbtn.pack()

root.mainloop()