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
    Body = math.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)
    Body = Body > 0.4
    Eye = math.sqrt((x - 0.7) ** 2 + (y - 0.3) ** 2)
    Eye = Eye > 0.06
    Mouth = ((x - 0.5) > - 3 * (y - 0.5)) and ((x - 0.5) > 3 * (y - 0.5))
    return (1 - Body) * Eye * (not Mouth), (1 - Body) * Eye * (not Mouth), 0

if __name__ == "__main__":
    window = tk.Tk()
    label = tk.Label(master=window)
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    window.mainloop()