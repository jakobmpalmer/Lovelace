import tkinter as tk

#initialize the tk interface
# m = master
m = tk.Tk()


def fahrenheit_to_celsius(F):
    return round(((F - 32) * 5/9), 3)

#setep - make entry boxes
tk.Label(m, text='temperature').grid(row=0)
temp = tk.Entry(m, textvariable = "temperature")
temp.grid(row=0, column=1)
tk.Label(m, text='Celcius').grid(row=1)


def callback():
    T = temp.get()
    try:
        T = float(T) # Try to make it a float
        print T
    except ValueError:
        print "Bad input" # Print this if the input cannot be made a float

    tk.Label(m, text=str(fahrenheit_to_celsius(T)) + " C").grid(row=1, column=1)
    print "click!"


b = tk.Button(m, text="Submit",
        command=callback)
b.grid(row=2, column=1)

#execute
m.mainloop()
