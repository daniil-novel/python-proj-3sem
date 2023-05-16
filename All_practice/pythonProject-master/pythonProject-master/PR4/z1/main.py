import math
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    frame1 = tk.Frame(master=window,width=500, height=500)
    frame1.pack()
    frame2 = tk.Frame(
        master=frame1,
        bg="black",
        width=400,
        height=400
    )
    frame2.place(x=50,y=50)
    window.mainloop()