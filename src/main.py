import customtkinter
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("IAgroscan")
        self.wm_iconbitmap("data/Scanner.ico")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, padx=5, pady=5, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        logo = customtkinter.CTkImage(
            light_image=Image.open("data/IAgroscanP.png"),
            dark_image=Image.open("data/IAgroscanP.png"),
            size=(200, 39),
        )
        
        self.labelImg = customtkinter.CTkLabel(self.sidebar_frame, image=logo, text="")
        self.labelImg.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        my_font = customtkinter.CTkFont(family="Google Sans", size=12)
        
        self.sidebar_text = customtkinter.CTkTextbox(self.sidebar_frame, font=my_font)
        self.sidebar_text.insert("0.0", """IAgroscan es una herramienta de detección y diagnostico de enfermedades de plantas agrícolas del departamento del Meta. Esta funciona haciendo uso de algoritmos de deep learning y modelos de detección propios, que brindan rapidez y precisión en las predicciónes.\n""")
        
        self.sidebar_text.tag_config("justificado", justify='left', wrap='word')
        self.sidebar_text.tag_add("justificado", "1.0", "end")
        
        self.sidebar_text.grid(row=1, column=0, padx=0, pady=10)
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


app = App()
app.mainloop()
