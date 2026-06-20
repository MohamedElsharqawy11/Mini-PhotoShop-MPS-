import customtkinter as ctk

class SidePanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=300, corner_radius=0, **kwargs)
        self.pack_propagate(False)

        self.tabs = ctk.CTkTabview(self, fg_color="#252526", segmented_button_fg_color="#1E1E1E", segmented_button_selected_color="#007ACC")
        self.tabs.pack(expand=True, fill="both", padx=10, pady=10)

        self.tabs.add("Classic")
        self.tabs.add("AI Models")

        self.scroll_classic = ctk.CTkScrollableFrame(self.tabs.tab("Classic"), fg_color="transparent")
        self.scroll_classic.pack(expand=True, fill="both")

        self._add_category_label(self.scroll_classic, "Color Adjustments")
        self.btn_gray = self._add_button(self.scroll_classic, "Grayscale")
        self.btn_brightness = self._add_button(self.scroll_classic, "Brightness / Contrast")
        self.btn_invert = self._add_button(self.scroll_classic, "Invert Colors")

        self._add_category_label(self.scroll_classic, "Blur & Smoothing")
        self.btn_gaussian = self._add_button(self.scroll_classic, "Gaussian Blur")
        self.btn_median = self._add_button(self.scroll_classic, "Median Blur")
        self.btn_bilateral = self._add_button(self.scroll_classic, "Bilateral Filter")

        self._add_category_label(self.scroll_classic, "Edge Detection")
        self.btn_canny = self._add_button(self.scroll_classic, "Canny Edge")
        self.btn_sobel = self._add_button(self.scroll_classic, "Sobel Filter")

        self.scroll_ai = ctk.CTkScrollableFrame(self.tabs.tab("AI Models"), fg_color="transparent")
        self.scroll_ai.pack(expand=True, fill="both")

        self._add_category_label(self.scroll_ai, "Segmentation")
        self.btn_remove_bg = self._add_ai_button(self.scroll_ai, "Remove Background")
        self.btn_sam = self._add_ai_button(self.scroll_ai, "Segment Anything (SAM)")

        self._add_category_label(self.scroll_ai, "Detection")
        self.btn_face = self._add_ai_button(self.scroll_ai, "Face Detection (MTCNN)")
        self.btn_yolo = self._add_ai_button(self.scroll_ai, "Object Detection (YOLO)")

    def _add_category_label(self, parent, text):
        lbl = ctk.CTkLabel(parent, text=text, text_color="#A9A9A9", font=("Arial", 12, "bold"))
        lbl.pack(anchor="w", pady=(15, 5), padx=5)

    def _add_button(self, parent, text):
        btn = ctk.CTkButton(parent, text=text, fg_color="#333333", hover_color="#444444", anchor="w")
        btn.pack(fill="x", pady=2, padx=5)
        return btn

    def _add_ai_button(self, parent, text):
        btn = ctk.CTkButton(parent, text=text, fg_color="#512BD4", hover_color="#673AB7", anchor="w")
        btn.pack(fill="x", pady=2, padx=5)
        return btn