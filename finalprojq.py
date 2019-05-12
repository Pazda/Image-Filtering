# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:26:04 2019

@author: Tim
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from tkinter import *
import filters
import PIL.Image, PIL.ImageTk
import scipy.misc

#setup
root = Tk()
root.wm_title( "Filters" )
root.geometry( "1000x800+100+100" )


#function library
funcs = {
    "Black and White": filters.bnw,
    "Noiser": filters.noiser,
    "Spiral": filters.spiral,
    "Scrambler": filters.scrambler,
    "Static Spook": filters.staticSpook,
    "Glass Door": filters.glassDoor,
    "Red Bubble": filters.bubble,
    "Blocks": filters.blocks,
    "Waves": filters.waves,
    "Uh Circle": filters.circ,
    "Pixellate": filters.pixellate,
    "Mirror": filters.mirror,
    "Upside Down": filters.upsideDown,
    "Sepia": filters.sepia,
    "Spiral 2": filters.hardSpiral,
    "I <3 Blues Clues": filters.blueOverlay
}

#function to retrieve ddirectory
def getDir():
    root.filename = filedialog.askopenfilename(initialdir="/",title="Select image")
    app.redraw(root.filename)

#UI
class Application:
    def __init__(self, master):
        self.img = ""
        root.filename = ""
        frame = Frame( master )
        frame.grid()
        
        self.vb = StringVar(root)
        self.vb.set("Black and White")
        self.dd = OptionMenu(root,self.vb,*list(funcs.keys()),command=self.argcheck)
        self.dd.grid(row=1)
        #self.vb.trace("w",self.argcheck)
        
        self.but1 = Button( frame, text="Upload", padx=18,pady=20, command=getDir )#, command=runner )
        self.but1.grid(row=2)
        
        self.but2 = Button( frame, text="Close",padx=20,pady=20, command=root.destroy )
        self.but2.grid(row=2,column=1)
        
        root.grid_rowconfigure(0,weight=1,minsize=400)
        root.grid_rowconfigure(3,weight=1)
        root.grid_columnconfigure(3,minsize=700,weight=1)
        #root.grid_columnconfigure(3,weight=1)
     
    def argcheck( self, funcd ):
        app.redraw( root.filename )
        
    #when a new image is selected
    def redraw(self, img, *args):
        if img == "":
            return
        f = Figure(figsize=(15,10))
        a = f.add_subplot(111)
        self.img = io.imread( img )
        self.img = funcs[self.vb.get()](self.img)
        a.imshow(self.img)
        
        canvas = FigureCanvasTkAgg( f, master=root )
        canvas.draw()
        canvas.get_tk_widget().grid(row=0,column=3,columnspan=4,rowspan=8,padx=40)
        
        #save image
        scipy.misc.imsave( 'outfile.jpg', self.img )
        root.filename = 'outfile.jpg'
        

app = Application(root)

#photo = io.imread( 'diddy kong.jpeg' )
#plt.imshow(photo)
#print("Variance: " + str(np.var(photo)))
#photo is a triple nested list
#each row of pixels is a list of pixels, which is a RGBA list
    
if __name__ == "__main__":
    #multiprocessing.freeze_support()
    root.mainloop()
