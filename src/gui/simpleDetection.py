import customtkinter
from PIL import Image

class simpleDetection(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Window Setup
        self.geometry("800x700+550+175")
        self.title("IAgroscan | Detección Simple")
        self.wm_iconbitmap("data\scanner.ico")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        
        #Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        #TopFrameLeft Frame Configuration
        self.top_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
        self.top_frame.grid_columnconfigure(5, weight=1)
        
        #TopRightLeft Frame Configuration
        self.top_right_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.top_right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")
        self.top_right_frame.grid_columnconfigure(5, weight=1)
        
        #BottomWhole Frame Configuration
        self.bottom_frame = customtkinter.CTkFrame(self, width=280, corner_radius=25)
        self.bottom_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=10 ,sticky="nswe")