__author__ = "Dimkauzh"
__version__ = "0.2.6"

import fusionengine.files.systems as sysconfig
from fusionengine.files.imports import *

class Main:
    def __init__(self):
        """A class that contains all the functions and classes. You need to initialize this class to use the engine.
        """
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        self.body = body
        self.system = sysconfig.System()
        self.rendereroptions = sysconfig.RendererOptions()
        self.shape = shape.Shapes()
        self.ui = ui.UI()
        self.fonts = fonts.Fonts()
        self.debug = debug.DebugFiles()

    def quit(self, window):
        """Quits the engine.

        Args:
            window: Your window
        """        
        sdl2.SDL_DestroyRenderer(window.renderer)
        sdl2.SDL_DestroyWindow(window.window)
        del window
        sdl2.SDL_Quit()
