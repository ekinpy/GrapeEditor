import os
import ctypes
import keyboard
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkcode import CodeEditor

# Render High Quality
ctypes.windll.shcore.SetProcessDpiAwareness(True)

os.system("cls && title Grape Editor (v0.1) - CLI Panel (%USERNAME%)")
print("[1] Python")
print("[2] JavaScript")
print("[3] C++")
print("[4] C#")
print("[5] C")
print("[6] Java")
print("[7] Swift")
print("[8] Ruby")
print("[9] Dart")
print("[10] PHP")
print("[11] SQL")
print("[12] Kotlin")
print("[13] HTML")
print("[14] CSS")
print("[15] Lua")
print("[16] Assembly")
print("[17] Go")
print("[18] TypeScript")
print("[19] JSON")
print("[20] R")

programminglang = input("> ")

if programminglang == "1":
    programminglang = "Python"
elif programminglang == "2":
    programminglang = "JavaScript"
elif programminglang == "3":
    programminglang = "C++"
elif programminglang == "4":
    programminglang = "C#"
elif programminglang == "5":
    programminglang = "C"
elif programminglang == "6":
    programminglang = "Java"
elif programminglang == "7":
    programminglang = "Swift"
elif programminglang == "8":
    programminglang = "Ruby"
elif programminglang == "9":
    programminglang = "Dart"
elif programminglang == "10":
    programminglang = "PHP"
elif programminglang == "11":
    programminglang = "SQL"
elif programminglang == "12":
    programminglang = "Kotlin"
elif programminglang == "13":
    programminglang = "HTML"
elif programminglang == "14":
    programminglang = "CSS"
elif programminglang == "15":
    programminglang = "Lua"
elif programminglang == "16":
    programminglang = "NASM"
elif programminglang == "17":
    programminglang = "Go"
elif programminglang == "18":
    programminglang = "TypeScript"
elif programminglang == "19":
    programminglang = "JSON"
elif programminglang == "20":
    programminglang = "R"
else:
    programminglang = "Python"

root = Tk()
root.title("Grape Editor (v0.1) - " + programminglang)
root.iconbitmap(default="assets/ico.ico")
root.option_add("*tearOff", 0)

def save():
    openf = filedialog.asksaveasfile(mode = "w", defaultextension = ".py")
    if openf is None:
        return
    text = str(editor.get(1.0, END))
    openf.write(text)

def openf():
    file = filedialog.askopenfile(mode = "r", filetype = [("All files", "*.*")])
    if file is not None:
        rf = file.read()
    editor.insert(1.0, rf)

def onclose():
    if messagebox.askokcancel("Quit", "Do you want to quit? Don't forget to save."):
        root.destroy()

mmenu = Menu(root)
root.config(menu=mmenu)

fopt = Menu(mmenu, tearoff=0)
fopt.add_command(label="Open", command=openf)
fopt.add_command(label="Save", command=save)
mmenu.add_cascade(label="File", menu=fopt)

eopt = Menu(mmenu, tearoff=0)
eopt.add_command(label="Undo", command=lambda: keyboard.press("ctrl+z"))
eopt.add_command(label="Redo", command=lambda: keyboard.press("ctrl+y"))
mmenu.add_cascade(label="Edit", menu=eopt)

editor = CodeEditor(
    root,
    width=99,
    height=30,
    language=programminglang,
    background="black",
    highlighter="monokai-plus-plus",
    font="Consolas",
    autofocus=True,
    blockcursor=False,
    insertofftime=0,
    padx=10,
    pady=10,
    undo=True,
)

root.protocol("WM_DELETE_WINDOW", onclose)

if programminglang.casefold() == "python":
    editor.content = 'print("Grape Editor!")'
elif programminglang.casefold() == "javascript":
    editor.content = 'alert("Grape Editor!");'
elif programminglang.casefold() == "c++":
    editor.content = '#include <iostream>\n\nint main() {\n    std::cout << "Grape Editor!";\n    return 0;\n}'
elif programminglang.casefold() == "c#":
    editor.content = 'System.Console.WriteLine("Grape Editor!");'    
elif programminglang.casefold() == "c":
    editor.content = '#include <stdio.h>\nint main() {\n    printf("Grape Editor!");\n    return 0;\n}'
elif programminglang.casefold() == "java":
    editor.content = 'System.out.println("Grape Editor!");'
elif programminglang.casefold() == "swift":
    editor.content = 'print("Grape Editor!")'
elif programminglang.casefold() == "ruby":
    editor.content = 'puts "Grape Editor!"'

editor.pack(fill="both", expand=True)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()