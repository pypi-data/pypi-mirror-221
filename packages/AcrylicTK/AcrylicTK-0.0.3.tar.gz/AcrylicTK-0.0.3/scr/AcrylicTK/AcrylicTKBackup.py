from tkinter import *
from ctypes import windll
from BlurWindow import GlobalBlur

AppBG = None
App = None
acrylic = '#010101'


class transparency:
    '''
    This widget will add a transparent spot.
    '''
    ts = None
    def __init__(self, master:Misc, width, hieght):
        self.msr = master
        self.wd:int = width
        self.ht:int = hieght
        global ts
        ts = Frame(self.msr, width=self.wd, height=self.ht, bg="#010101") 
    def place(self, x:int = 0, y:int = 0):
        ts.place(x=x, y=y)
        

#the class to make the window
class ATK():
    '''
    This will create a tkinter window that 
    will have transparency/acrylic support.
    Make the window like you would with a normal tkinter
    window. it will look like this:\n
    root = ATK()\n
    To add widgets or use tkinter functions 
    you will have to acess the atk varible
    that is in the ATK class:\n
    root.atk.mainloop()
    '''
    Dm:bool = None
    def __init__(self, darkMode:bool = False):
        self.Dm:bool = darkMode
    global App
    global AppBG
    
    
    px = 100
    py = 100
    w = 400
    h = 500
    Bg = "#eeeeee"
    Ac = False 
    def config(self, windowPosX:int=None, windowPosY:int=None, windowWidth:int=None, windowHieght:int=None, bg:str=None, acrylic:bool=None):
        global px
        global py
        global w
        global h
        global Bg
        global Ac
        
        px = windowPosX
        py = windowPosY
        w = windowWidth
        h = windowHieght
        Bg = bg
        Ac = acrylic
        self.update()
        print(str(Ac) + ' ' + str(acrylic))

    
    #create the background for the app.
    #the app where all the widgets will
    #be is a top level window that will
    #move, resize, and minimize/maximize with
    #this window.
    
    appBG = Tk()
    AppBG = appBG
    #this geometry method wont
    #change anything yet
    #Dont change this one
    #change the one after this one
    appBG.geometry('0x0+0+0')
    appBG.config(bg='#000000')
    appBG.update()
    #make the background blury.
    
    hWND = windll.user32.GetParent(appBG.winfo_id())
    GlobalBlur(hWND, '#010101', Ac, Dm)

    def updateBlur(self):
        hWND = windll.user32.GetParent(AppBG.winfo_id())
        GlobalBlur(hWND, '#010101', Ac, self.Dm)

    #change the geometry here
    #I dont know why but I
    #have to change it here or
    #if dark mode is enabled and
    #I dont do this it does wierd things
    #SO CHANGE IT HERE!
    appBG.geometry(str(w) + 'x' + str(h) + '+' + str(px) + '+' + str(py))
    
    appBG.update()

    #make the toplevel app window where all the widgets will go.
    app = Toplevel(appBG, background=Bg)
    App = app
    #set the geometry to the sane as the background
    #window dont change this at all
    app.geometry(str(appBG.winfo_width()+0) + 'x' + str(appBG.winfo_height()) + '+' + str(appBG.winfo_x()+8) + '+' + str(appBG.winfo_y()+31))
    #remove the title bar for the app window
    app.overrideredirect(True)
    app.update()

    #move the app window with the background window.
    def PairWindows(x):
        global App
        global AppBG
        App.geometry(str(AppBG.winfo_width()+0) + 'x' + str(AppBG.winfo_height()) + '+' + str(AppBG.winfo_x()+8) + '+' + str(AppBG.winfo_y()+31))
        App.update()
    #this handles when the window is un minimized
    def OnMouseEnter(x):
        global App
        App.wm_attributes('-topmost', True)
        App.wm_attributes('-topmost', False)
    def OnMouseExit(x):
        global App
        App.wm_attributes('-topmost', False)

    def Show(x):
        App.wm_deiconify()
    def Hide(x):
        App.wm_withdraw()
        
    def update(self):
        App.update()
        AppBG.update()
        self.updateBlur()
        AppBG.geometry(str(w) + 'x' + str(h) + '+' + str(px) + '+' + str(py))
        App.config(bg=Bg)



    atk = App

    #bind the functions
    app.attributes('-transparentcolor', '#010101')
    appBG.bind("<Configure>", PairWindows)
    appBG.bind("<Enter>", OnMouseEnter)
    appBG.bind("<Leave>", OnMouseExit)
    appBG.bind("<Map>", Show)
    appBG.bind("<Unmap>", Hide)
    