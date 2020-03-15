import tkinter as tk

#initialize the tk interface
# m = master
m = tk.Tk()

tk.Label(m, text='Distance').grid(row=0)
distance = tk.Entry(m, textvariable = "dist")
distance.grid(row=0, column=1)
tk.Label(m, text='This will take: ').grid(row=1)
tk.Label(m, text='For light to travel').grid(row=2)


def callback():
    tk.Label(m, text=str(float(distance.get()) / 299792458) + " secs").grid(row=1, column=1)
      # time= distance / Speed of light [m/s]



b = tk.Button(m, text="Submit",
        command=callback)
b.grid(row=2, column=1)


m.mainloop()
