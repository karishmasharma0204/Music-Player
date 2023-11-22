from playsound import playsound
import pygame
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image

global paused
paused="false"

root = Tk()
root.title("Music Player")
root.geometry("500x300")
root.resizable(False, False)

canva = Canvas(root,width=700,height=300)
img = ImageTk.PhotoImage(Image.open("C:/Users/hp/OneDrive/Desktop/Python/music player/Copy of Back.png"))
canva.create_image(0,0,anchor=NW,image=img)
canva.pack(fill=BOTH, expand=True)

#Button Image resizing
add_image=Image.open("C:/Users/hp/OneDrive/Desktop/Python/music player/add.png")
resized = add_image.resize((40, 40), Image.LANCZOS)
add_image = ImageTk.PhotoImage(resized)

play_image=Image.open("C:/Users/hp/OneDrive/Desktop/Python/music player/Copy of pause.png")
resized = play_image.resize((40, 40), Image.LANCZOS)
play_image = ImageTk.PhotoImage(resized)

stop_image=Image.open("C:/Users/hp/OneDrive/Desktop/Python/music player/Copy of stop.png")
resized = stop_image.resize((40, 40), Image.LANCZOS)
stop_image = ImageTk.PhotoImage(resized)

pause_image=Image.open("C:/Users/hp/OneDrive/Desktop/Python/music player/Copy of pause.png")
resized = pause_image.resize((40, 40), Image.LANCZOS)
pause_image = ImageTk.PhotoImage(resized)

def addsong():
    song = filedialog.askopenfilename(initialdir="C:/Users/hp/Downloads",filetypes=(("mp3 Files","*.mp3"), ))
    song = song.replace("C:/Users/hp/Downloads/","")
    song_list.insert(END,song)

def play():
    song = song_list.get(ACTIVE)
    active_song = "C:/Users/hp/Downloads/{}"
    active_song=(active_song.format(song))
    pygame.mixer.music.load(active_song)
    pygame.mixer.music.play(loops=0)
    b2['state'] = DISABLED
    
def stop():
    pygame.mixer.music.stop()
    b2['state'] = NORMAL

def pause(): 
        #code for pause
    global paused
    if paused=="false":
        pygame.mixer.music.pause()
        b4['image'] = play_image
        paused = "true"
        return
        #code for unpause
    if paused=="true":
        pygame.mixer.music.unpause()
        print(pause)
        b4['image'] = pause_image
        paused="false"

pygame.mixer.init()

song_list = Listbox(root,width=50,height=10, bg="white")
song_list.place(x=100,y=20)

b1 = Button(text="Add new entry", width = 40, height = 40, bg="white", border=0,image=add_image, command=addsong)
b1.place(x=100,y=200)

b2 = Button(text="Play song", width = 40, height = 40, bg="white", border=0, image=play_image,command=play)
b2.place(x=185,y=200)

b3 = Button(text="stop song", width = 40, height = 40, bg="white", border=0,image=stop_image,command=stop)
b3.place(x=270,y=200)

b4 = Button(text="pause song", width = 40, height = 40, bg="white", border=0,image=pause_image,command=pause)
b4.place(x=358,y=200)

root.mainloop()