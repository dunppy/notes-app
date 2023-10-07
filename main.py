import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()

window.title("Notes App")

window.geometry("300x300")

label = tk.Label(window, text="Notes:")
label.pack()

text_box = tk.Entry(window)
text_box.pack()

def add_note():
    text_entry = text_box.get()
    
    
    
    notes_label = tk.Label(window, text=text_entry, anchor="w")
    notes_label.pack(fill="x")

    #Delete Button
    delete_button = tk.Button(notes_label, text="Delete", command=lambda label=notes_label: delete_note(label))
    delete_button.pack(side="right")

    #Edit Button
    edit_button = tk.Button(notes_label, text="Edit", command=lambda label=notes_label: edit_note(label))
    edit_button.pack(side="right")




    notes_list.append((notes_label, delete_button, edit_button))

    if len(notes_list)>max_notes:
        old_note, old_edit_button, old_delete_button = notes_list.pop()
        old_note.destroy()
        old_edit_button.destroy()
        old_delete_button.destroy()
        

    text_box.delete(0, "end")

def edit_note(notes_label):
    for i, (label, edit_button, delete_button) in enumerate(notes_list):
        if label == notes_label:
            new_text = simpledialog.askstring("Edit Note", "Edit the note:", initialvalue=label.cget("text"))
            if new_text:
                label.config(text=new_text)
            break



def delete_note(notes_label):
    for i, (label, delete_button,edit_button) in enumerate(notes_list):
        if label == notes_label:
            label.destroy()
            delete_button.destroy()
            edit_button.destroy()
            notes_list.pop(i)
            break


    
note_frame = tk.Frame(window)
note_frame.pack()

button = tk.Button( window, text ="Add Note", command=add_note)
button.pack()


notes_list = []
max_notes = 5


window.mainloop()
