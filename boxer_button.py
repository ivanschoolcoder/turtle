from pickle import TRUE
import tkinter
import time
import random
window = tkinter.Tk()
button = tkinter.Button(window, text = "ready", width = 20, height = 10)
clickcount = 0
inbutton = False
button.pack(padx = 10, pady = 10)
button.configure(text = "ready")
time.sleep(2)
button.configure(text = "GO")
def on_click(event):
    global inbutton
    inbutton = True
def on_end(event):
    global inbutton
    inbutton = False
#    while inbutton == True:
#        clickcount = clickcount + 1
#    if clickcount >= 3000:
#        clickcount = clickcount - random.randint(100, 300)
#   print("ты держал кнопку ", str(clickcount))
def my_function() :
    global inbutton
    global clickcount
    if inbutton == True:
        clickcount = clickcount + 1  
    else:
        if clickcount >= 3000:
            clickcount = clickcount - random.randint(300, 235)  
        button.configure(text = str(clickcount))
        #print(str(clickcount))
        clickcount = 0
def schedule() :
    my_function()
    window.after( 1 , schedule)
schedule()    
button.bind("<Enter>", on_click)
button.bind("<Leave>", on_end)
window.mainloop()