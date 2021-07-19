import tkinter as tk

def namePage():
    wind=tk.Tk()
    wind.title("GAME")
    label = tk.Label(wind, text="THE GAME OF \n CHANCES")
    label.grid(row=1, column=1,columnspan=2, padx=10, pady=10)
    nameVar=tk.StringVar()
    name_label = tk.Label(wind, text="Enter yor name: ")
    name_label.grid(row=2, column=1, padx=10, pady=10)
    name = tk.Entry(wind,textvariable = nameVar)
    name.grid(row=2, column=2, padx=10, pady=10)
    click = tk.Button(wind, text="Enter", command=lambda: next())
    click.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
    def next():
        if name.get() == '':
            labe = tk.Label(wind, text="please enter a name")
            labe.grid(row=6, column=1)
        else:
            writeName(nameVar.get())
            labe = ''
            wind.destroy()
    wind.mainloop()
    return
    
def writeName(name):
    f=open("name.txt","w")
    f.write(name)
    f.close()

    
