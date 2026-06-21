import cv2
from customtkinter import filedialog

class ImageController:
    def __init__(self, main_window, image_state,history_manager):
        self.main_window = main_window
        self.image_state = image_state
        self.history_manager = history_manager

    def BindEvents(self):
        self.main_window.top_toolbar.btn_upload.configure(command=self.UploadImage) 
        self.main_window.top_toolbar.btn_save.configure(command=self.SaveImage)
        self.main_window.top_toolbar.btn_resetconfigure(command=self.ResetImage)
        self.main_window.top_toolbar.btn_redo.configure(command=self.Redo)


    def UploadImage(self):
        pass

    def SaveImage(self):
        pass

    def ResetImage(self):
        pass

    def Redo(self):
        image = self.history_manager.Redo()