import cv2
from tkinter import filedialog
from tkinter import messagebox

class ImageController:
    def __init__(self, main_window, image_state,history_manager):
        self.main_window = main_window
        self.image_state = image_state
        self.history_manager = history_manager

    def BindEvents(self):
        self.main_window.top_toolbar.btn_upload.configure(command=self.UploadImage) 
        self.main_window.top_toolbar.btn_save.configure(command=self.SaveImage)
        self.main_window.top_toolbar.btn_reset.configure(command=self.ResetImage)
        self.main_window.top_toolbar.btn_redo.configure(command=self.Redo)
        self.main_window.top_toolbar.btn_undo.configure(command=self.Undo) 


    def UploadImage(self):
        FilePath = filedialog.askopenfilename(filetypes=[("image files","*.png *.jpg *.jpeg *.bmp")])

        if not FilePath:
            return

        image = cv2.imread(FilePath);
       
        if image is None:
            return

        #self.image_state.current_image = image ⁄‘«‰ „›Ì‘ ’Ê—… «’·ÌÂ ›Ì 
        self.image_state.SetInitialImage(image, FilePath)
        self.history_manager.ClearHistory()
        self.history_manager.SaveState(image)
        self.UpdateView()

    def SaveImage(self):
        image = self.image_state.GetCurrentImage()
        if image is None :
            return
        
        file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")])

        if not file_path:
            return

        if not cv2.imwrite(file_path,image) :
          messagebox.showerror("Error", "Failed to save image")
        else:
          messagebox.showinfo("Success", "Image saved successfully")

    def ResetImage(self):
       self.image_state.ResetToOriginal()
       self.history_manager.ClearHistory()
       self.UpdateView()

    def Redo(self):
        image = self.history_manager.Redo()
        if image is not None : 
            self.image_state.current_image = image
            self.UpdateView()
   
    def Undo(self):
        image = self.history_manager.Undo()
        if image is not None : 
            self.image_state.current_image = image
            self.UpdateView()

    def UpdateView(self):
        image = self.image_state.current_image
        if image is None :
           self.main_window.canvas.ClearCanvas()
           return

        self.main_window.canvas.DisplayImage(image)