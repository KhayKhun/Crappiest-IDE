import tkinter as tk
from tkinter import filedialog

def exitWrapper():
    exit(None)

def saveAndRunWrapper():
    saveAndRun(None)

def openFileWrapper():
    openFile(None)

def exit(event):
    window.destroy()

def saveAndRun(event):
    content = text_area.get("1.0", "end-1c") 

    save_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML File", "*.html")],
            title='Save file to'
        )
        
    if save_path:
        with open(save_path, "w") as html_file:
            html_file.write(content)

        import webbrowser
        webbrowser.open(f'file://{save_path}', new=2)

def openFile(event):
    file_path = filedialog.askopenfilename(
        defaultextension=".html",
        filetypes=[("HTML File", "*.html"),("Text file", "*.txt")],
        title='Open HTML File'
    )
    if file_path:
        with open(file_path,"r") as f:
            content = f.read()
            print(content)
            text_area.delete(1.0,"end")
            text_area.insert(1.0,content)

window = tk.Tk()
window.title("HTML Editor")
icon = tk.PhotoImage(file='html.png')
window.iconphoto(True,icon)

menubar = tk.Menu(window)
fileMenu = tk.Menu(menubar,tearoff=0)

menubar.add_cascade(label='File',menu=fileMenu)
runIcon = tk.PhotoImage(file='run.png')
print(runIcon)
menubar.add_command(label='Run',command=saveAndRunWrapper)

fileMenu.add_command(label="Open (Ctrl+O)",command=openFileWrapper)
fileMenu.add_command(label="Save and Run (Ctrl+S)",command=saveAndRunWrapper)
fileMenu.add_separator()
fileMenu.add_command(label="Exit (Ctrl+E)",command=exitWrapper)

text_area = tk.Text(window, height=20, width=80)
text_area.pack(padx=10, pady=10)
text_area.insert(1.0,'<!Doctype html>\n\n<header title="Demo">\n</header>\n\n<body>\n\n</body>')

btn = tk.Button(window, text="Save and Run HTML (Ctrl+S)",image=runIcon,compound='right' ,command=saveAndRunWrapper)
btn.pack()

window.config(menu=menubar)
window.bind("<Control-s>",saveAndRun)
window.bind("<Control-o>",openFile)
window.bind("<Control-e>",exit)
window.mainloop()

