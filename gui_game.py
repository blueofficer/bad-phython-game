from tkinter import *

display_text = "test"

window = Tk() 

window.geometry("420x420")
window.title("video game")
window.config(background="black")

game_text = Label(window,text=f"{display_text}",
              font=('Arial',20,'bold'),
              fg='#03fc03' , #text color
              bg='black')    #background color

player_entry = Entry(window)

player_entry.place(x=0,y=100)
game_text.place(x=0,y=0)

window.mainloop() #place window on screen