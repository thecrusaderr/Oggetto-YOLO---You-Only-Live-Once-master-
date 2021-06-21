from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import ImgInput
import Try1

def select_image():
    path = filedialog.askopenfilename() 
    #opens dialog box to browse your pc for selecting image to perform object detection
    ImgInput.image(path)
def video():
    Try1.video()    
    #calls video() function from Try1.py file
window=Tk()
window["bg"] = "white"
window.title("OGGETTO")
window.geometry("1800x1070")

text1 = Text(window, height=20, width=36)
photo=PhotoImage(file='LOGO.png')
text1.image_create(END, image=photo)
text1.insert(END,'\n')
text1.pack(side=TOP)
#changing format of text and sizing

btn1 = Button(window, text="Click here to select an image from the PC", command=select_image,height=1,width=60) #button 
btn1['font']=36
btn1.pack(side="left",fill="both", expand="no", padx="60", pady="200")

btn2 = Button(window, text="Click here for real-time detection", command=video,height=1, width=60) #button
btn2['font']=36
btn2.pack(side="right", fill="both", expand="no", padx="60", pady="200")
window.mainloop()
