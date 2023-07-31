
from tkinter import *
import subprocess
from PIL import Image

def button_clicked():
    file1 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/prng-service.txt","w+")
    file1.write("run")
    file1.close()
    file2 = open("/Users/jonnawaage/Documents/GitHub/CS361/A2/image-service.txt", "r")
    contents = file2.read()
    if (contents < '0011.png') :
        image_path = "/Users/jonnawaage/Documents/GitHub/CS361/A2/" + contents
        img = Image.open(image_path)
        img.show
        Label(root, text=image_path).pack()
    file2.close

root = Tk()
Button(root, text="Get Image", command=button_clicked).pack()
root.mainloop()
