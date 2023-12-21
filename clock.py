import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    hanTime.config(text = current_time)
    
    //to update the clock after milliseconds (after() is a method
    hanTime.after(1000,update_clock)

app = tk.Tk()
app.title("HanTime  python")

hanTime = tk.Label(app, text = "", font =("Helvetica, 48"))
hanTime.pack()

update_clock()
app.mainloop()

