'''
Created on August 16, 2022
@author: BalthMhs
@society: BossaMuffinConnected
'''
# Constants available in the whole app
# import .global_constants as g_const

# Frontend
import tkinter as tk
# from tkinter import ttk

# Others
# import .lib_display as ds

class TkView(tk.Tk):
    '''
    Classdocs
    '''
    def __init__(self):
        super().__init__()
        
    def setupWindow(self, p_controller):
        self.controller  = p_controller

        # Set the global parameters
        self.BG_CLR = 'white'
        # self.BG_CLR_1 = "#41B77F"
        # self.BG_CLR_2 = "#f2f2f2"
        # self.TXT_CLR = 'white'
        # self.GTRY = '1080x'+str(self.winfo_screenheight())
        self.MIN_WIDTH = 720
        self.MIN_HEIGHT = 720
        # self.WIDTH_BTN = 20
        # self.IPADY_CONTENT = 20
        # self.PADX_CONTENT = 10
        # self.WIDTH_CONTENT_AREA = self.MIN_WIDTH-self.WIDTH_BTN-(4*self.PADX_CONTENT)
        # self.LOGO_ICO = 'logo.ico'
        # self.BORDER = 1
        # self.CONTENT_MESSAGE = ()

        # Init local attributes
        # self.btn_choosing_day = {}
        # self.btn_choosing_day_in_app = {}
        # self.frame_by_day = {}
        # self.label_by_day = {}

        # Make the window and the frames
        self._initWindow()

    def startMainLoop(self):
        self.mainloop()
    
    def _centerWindow(self):
        self.update()
        e_width = self.winfo_width()
        e_height = self.winfo_screenheight()
        e_xoffset = (self.winfo_screenwidth() - e_width) // 2
        e_yoffset = (self.winfo_screenheight() - e_height) // 2
        e_gtry = f'{e_width}x{e_height}+{e_xoffset}+{e_yoffset}'
        self.geometry(e_gtry)
        
    # Create the navigation bar
    def _makeNavBar(self):
       pass

    # Create the app title bar
    def _makeTitlesBar(self):
       pass

    def _initWindow(self):
        # Create the main window
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self._centerWindow()
        # self._makeNavBar()
        # self._makeTitlesBar()
        # self.iconbitmap("img/icon_checked.ico")
        self.config(background=self.BG_CLR, relief='sunken')
        self.resizable(width=True, height=True)
        self._centerWindow()

    def setupMainView(self, p_controller):
        pass

