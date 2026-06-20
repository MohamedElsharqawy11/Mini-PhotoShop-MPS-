import customtkinter as ctk
from PIL import Image, ImageDraw
import cv2

class ImageCanvas(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, text="", fg_color="#1E1E1E", corner_radius=0, **kwargs)
        self.canvas_width = 800
        self.canvas_height = 600
        
        self.checkerboard_bg = self._create_checkerboard(self.canvas_width, self.canvas_height)
        self.current_tk_image = None
        self.ClearCanvas()

    def _create_checkerboard(self, width, height, square_size=20):
        img = Image.new("RGB", (width, height), color="#333333") 
        draw = ImageDraw.Draw(img)
        for y in range(0, height, square_size):
            for x in range(0, width, square_size):
                if (x // square_size + y // square_size) % 2 == 0:
                    draw.rectangle([x, y, x + square_size, y + square_size], fill="#444444")
        return img

    def DisplayImage(self, cv_array):
        if len(cv_array.shape) == 3 and cv_array.shape[2] == 4:
            rgb_image = cv2.cvtColor(cv_array, cv2.COLOR_BGRA2RGBA)
            pil_image = Image.fromarray(rgb_image, 'RGBA')
        else:
            rgb_image = cv2.cvtColor(cv_array, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_image, 'RGB')
        
        pil_image = self.ResizeImageToFit(pil_image)
        
        final_bg = self.checkerboard_bg.copy()
        
        offset_x = (self.canvas_width - pil_image.width) // 2
        offset_y = (self.canvas_height - pil_image.height) // 2
        
        if pil_image.mode == "RGBA":
            final_bg.paste(pil_image, (offset_x, offset_y), pil_image) 
        else:
            final_bg.paste(pil_image, (offset_x, offset_y))
            
        self.current_tk_image = ctk.CTkImage(light_image=final_bg, dark_image=final_bg, size=(self.canvas_width, self.canvas_height))
        self.configure(image=self.current_tk_image)

    def ClearCanvas(self):
        bg = self.checkerboard_bg.copy()
        self.current_tk_image = ctk.CTkImage(light_image=bg, dark_image=bg, size=(self.canvas_width, self.canvas_height))
        self.configure(image=self.current_tk_image)

    def ResizeImageToFit(self, pil_image):
        pil_image.thumbnail((self.canvas_width, self.canvas_height), Image.Resampling.LANCZOS)
        return pil_image