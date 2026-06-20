import customtkinter as ctk

class TopToolBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, height=50, corner_radius=0, **kwargs)
        
        self.btn_upload = ctk.CTkButton(self, text="Upload Image", width=120, fg_color="#007ACC", hover_color="#005C99")
        self.btn_upload.pack(side="left", padx=10, pady=10)

        self.btn_save = ctk.CTkButton(self, text="Save Export", width=120, fg_color="#238636", hover_color="#2EA043")
        self.btn_save.pack(side="left", padx=10, pady=10)

        self.btn_reset = ctk.CTkButton(self, text="Reset", width=80, fg_color="#DA3633", hover_color="#B62C29")
        self.btn_reset.pack(side="right", padx=10, pady=10)

        self.btn_redo = ctk.CTkButton(self, text="Redo", width=80, fg_color="#383B40", hover_color="#45494E")
        self.btn_redo.pack(side="right", padx=10, pady=10)

        self.btn_undo = ctk.CTkButton(self, text="Undo", width=80, fg_color="#383B40", hover_color="#45494E")
        self.btn_undo.pack(side="right", padx=10, pady=10)