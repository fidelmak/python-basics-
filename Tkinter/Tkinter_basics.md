##  Basic Tkinter 




### 1. Basic Tkinter Window:

```python
import tkinter as tk

root = tk.Tk()
root.title("My Tkinter Window")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
```

### 2. Buttons and Event Handling:

```python
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Tkinter Buttons")

label = tk.Label(root, text="Click the Button!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
```

### 3. Entry Widget:

```python
import tkinter as tk

def on_submit():
    result_label.config(text=f"Hello, {entry.get()}!")

root = tk.Tk()
root.title("Entry Widget Example")

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
```

### 4. Checkboxes:

```python
import tkinter as tk

def on_checkbox_change():
    result_label.config(text=f"Checkbox State: {var.get()}")

root = tk.Tk()
root.title("Checkbox Example")

var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=var, command=on_checkbox_change)
checkbox.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
```

### 5. Radiobuttons:

```python
import tkinter as tk

def on_radio_change():
    result_label.config(text=f"Selected Option: {var.get()}")

root = tk.Tk()
root.title("Radiobutton Example")

var = tk.StringVar()

radio_button1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=on_radio_change)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=on_radio_change)

radio_button1.pack()
radio_button2.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
```

### 6. Listbox:

```python
import tkinter as tk

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    result_label.config(text=f"Selected Item: {selected_item}")

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")

listbox.pack()

result_label = tk.Label(root, text="")
result_label.pack()

listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
```

### 7. Menus:

```python
import tkinter as tk

def on_menu_click():
    result_label.config(text=f"Menu Option: {clicked.get()}")

root = tk.Tk()
root.title("Menu Example")

menu_options = ["Option 1", "Option 2", "Option 3"]

clicked = tk.StringVar()
clicked.set(menu_options[0])

menu = tk.OptionMenu(root, clicked, *menu_options)
menu.pack()

result_label = tk.Label(root, text="")
result_label.pack()

menu_button = tk.Button(root, text="Select Option", command=on_menu_click)
menu_button.pack()

root.mainloop()
```

### 8. Frames:

```python
import tkinter as tk

root = tk.Tk()
root.title("Frames Example")

frame1 = tk.Frame(root, borderwidth=2, relief="solid")
frame1.pack(side="left")

frame2 = tk.Frame(root, borderwidth=2, relief="solid")
frame2.pack(side="right")

label1 = tk.Label(frame1, text="Frame 1")
label1.pack()

label2 = tk.Label(frame2, text="Frame 2")
label2.pack()

root.mainloop()
```
