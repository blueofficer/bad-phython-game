from tkinter import *

display_text = "test"

window = Tk() 

window.geometry("420x420")
window.title("video game")
window.config(background="black")

label = Label(window,text=f"{display_text}",
              font=('Arial',20,'bold'),
              fg='#03fc03' , #text color
              bg='black')    #background color

label.place(x=0,y=0)

window.mainloop() #place window on screen