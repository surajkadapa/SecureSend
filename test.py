from tkinter import *
   
def add_buttons():
    # Add buttons
    for i in range(10):
        Button(main, text=str(i)).pack()

    # search for "Add Buttons" Button object and change text and function 
    for child in main.winfo_children():
        if child.cget('text') == 'Add Buttons':
             child.config(text='Delete all buttons')
             child.config(command=delete_buttons)


def delete_buttons():
    # search for buttons and delete all except the 'Delete' Button
    for child in main.winfo_children():
        if child.winfo_class() == 'Button':
            if child.cget('text') == 'Delete all buttons':
                # change "Delete" button text and function
                child.config(text='Add Buttons')
                child.config(command=add_buttons)
            else:
                child.destroy()

main = Tk()
Button(main,text='Add Buttons', command=add_buttons).pack()
main.mainloop()