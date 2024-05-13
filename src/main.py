import customtkinter
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Window Setup
        self.geometry("1200x700")
        self.title("IAgroscan")
        self.wm_iconbitmap("data/Scanner.ico")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        
        #Grid Configuration
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #Sidebar Configuration
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, padx=10, pady=10, rowspan=4, sticky="nswe")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        
        #Logo Setup
        logo = customtkinter.CTkImage(
            light_image=Image.open("data/IAgroscanP.png"),
            dark_image=Image.open("data/IAgroscanP.png"),
            size=(200, 39),
        )
        self.labelImg = customtkinter.CTkLabel(self.sidebar_frame, image=logo, text="")
        self.labelImg.grid(row=1, column=0, padx=20, pady=(20, 10))

        #Sidebar Components
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Detección Simple",fg_color="gray25")
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Detección en Lote",fg_color="gray25")
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Informes",fg_color="gray25")
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Estadísticas",fg_color="gray25")
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=15, column=0, padx=20, pady=(10, 20))



        # Create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=400)
        # self.textbox.insert("0.0", """IAgroscan es una herramienta de detección y diagnostico de enfermedades de plantas agrícolas del departamento del Meta. Esta funciona haciendo uso de algoritmos de deep learning y modelos de detección propios, que brindan rapidez y precisión en las predicciónes.\n""")
        # self.textbox.tag_config("justificado", justify='left', wrap='word')
        # self.textbox.tag_add("justificado", "1.0", "end")
        self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        
            

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
