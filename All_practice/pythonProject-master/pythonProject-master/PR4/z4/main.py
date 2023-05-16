import math
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

def func(x, y):
    value = (math.sin(x * 99.3467871 + y * 11.123457654321) + x * 99.3467871 + math.cos(x *1.2349875 + y * 111.12)) * 984798.928034652752
    value %= 1
    return value, value, value

if __name__ == "__main__":
    window = tk.Tk()
    label = tk.Label(master=window)
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    window.mainloop()