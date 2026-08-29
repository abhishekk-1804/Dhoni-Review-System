#down.. pips & rem...frm.. ps
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

#ref.. cv doc.. from ggl..

stream=cv2.VideoCapture("clip.mp4")
flag=True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(187,50,fill="red",font="Times 37 bold",text="Decision Pending")
    flag=not flag


def pending(decision):
    #1)display decision pending img..
    frame=cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image_names=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


    #2)wait for a second
    time.sleep(1)

    #3)display sponsor img...
    frame=cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image_names=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #4)wait for 2 seconds
    time.sleep(2)

    #5)display decision img.. @ last,
    if decision=='out':
        decisionImg="out.jpg"
    else:
        #frame="notout.jpg"
        decisionImg="notout.jpg"

    frame=cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image_names=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def out():
    thread=threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("Batsmen OUT.!")

def notout():
    thread=threading.Thread(target=pending, args=("not out",))
    thread.daemon=1
    thread.start()
    print("Batsmen safe.NOT OUT.!")


#Weidth & ht.. of main screen,
SET_WIDTH = 720
SET_HEIGHT=400

#GUI of kinter,
window=tkinter.Tk()
window.title("Dhoni Review System(The DRS).!!")
cv_img=cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

#Control buttons,
btn=tkinter.Button(window,text="<< Previous(fast)",width=50, command=partial(play,-25))
btn.pack()
btn=tkinter.Button(window,text="<< Previous(slow)",width=50, command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="Forward(fast) >>",width=50, command=partial(play,+25))
btn.pack()
btn=tkinter.Button(window,text="Forward(slow) >>",width=50, command=partial(play,+2))
btn.pack()
btn=tkinter.Button(window,text="OUT.!!",width=50, command=out)
btn.pack()
btn=tkinter.Button(window,text="NOT OUT.!!",width=50, command=notout)
btn.pack()


window.mainloop()
