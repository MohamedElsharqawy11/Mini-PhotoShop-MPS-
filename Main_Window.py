import customtkinter as ctk
from Canvas import ImageCanvas
from tool_bar import TopToolBar
from side_panel import SidePanel

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mini PhotoShop (MPS) - AI Edition")
        self.geometry("1280x800")
        self.configure(fg_color="#252526") 

        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0) 

        self.top_toolbar = TopToolBar(self, fg_color="#1E1E1E")
        self.top_toolbar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.canvas_frame = ctk.CTkFrame(self, fg_color="#252526", corner_radius=0)
        self.canvas_frame.grid(row=1, column=0, sticky="nsew")
        self.canvas_frame.pack_propagate(False)
        
        self.canvas = ImageCanvas(self.canvas_frame)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.side_panel = SidePanel(self, fg_color="#1E1E1E", border_width=1, border_color="#333333")
        self.side_panel.grid(row=1, column=1, sticky="ns")

        self.status_bar = ctk.CTkLabel(self, text=" Ready", fg_color="#007ACC", text_color="white", anchor="w", padx=10, height=25)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")