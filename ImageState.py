class ImageState:
    def __init__(self):
        self.original_image = None
        self.current_image = None
        self.image_path = None

    def SetInitialImage(self, cv_array, path):
        self.original_image = cv_array.copy()
        self.current_image = cv_array.copy()
        self.image_path = path

    def UpdateImage(self, new_cv_array):
        self.current_image = new_cv_array.copy()

    def ResetToOriginal(self):
        if self.original_image is not None:
          self.current_image = self.original_image.copy()

    def GetCurrentImage(self):
        return self.current_image

    def ClearState(self):
        self.original_image = None
        self.current_image = None
        self.image_path = None
