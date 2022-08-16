#!/usr/bin/env python3
# coding: utf-8

'''
Created on August 16, 2022
@author: BalthMhs
@society: BossaMuffinConnected
'''
# Constants available in the whole app
# import .global_constants as g_const

# MVC main dependencies
from model import Model
from view import TkView

# Others
# import .lib_display as ds
# ds.printn()
import sys

class Controller:
    '''
    Classdocs
    '''
    
    def __init__(self, p_model, p_view):
        self.model = p_model
        self.view = p_view

    def start(self):
        print(">> Setup the window")
        self.view.setupWindow(self)
        print(">> Setup the first view")
        self.view.setupMainView(self)
        print(">> Start to loop")
        self.view.startMainLoop()
    
    def stopApp(self):
        self.view.destroy
        sys.exit(0)

if __name__== "__main__":
    # Main function
    joana_patch = Controller(Model(), TkView())
    joana_patch.start()