import customtkinter
from PIL import Image
from simpleDetection import simpleDetection

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Window Setup
        self.geometry("800x700+550+175")
        self.title("IAgroscan | Menú Principal")
        self.wm_iconbitmap("data/scanner.ico")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        
        #Grid Configuration
        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1), weight=1)
        
        #Sidebar Configuration
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, padx=10, pady=10, rowspan=4, sticky="nswe")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        
        #Center Frame Configuration
        self.center_frame = customtkinter.CTkFrame(self, width=350, corner_radius=25)
        self.center_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=4, sticky="nswe")
        self.center_frame.grid_rowconfigure(20, weight=1)
        self.center_frame.grid_columnconfigure(10, weight=1)
        
        #Logo Setup
        logo = customtkinter.CTkImage(
            light_image=Image.open("data/iagroscan_logo.png"),
            dark_image=Image.open("data/iagroscan_logo.png"),
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
        
        #Scaling Setup
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tamaño de la Interfaz:", anchor="w")
        self.scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event, fg_color="gray25")
        self.scaling_optionemenu.grid(row=15, column=0, padx=20, pady=(10, 20))
        
        #Center Frame Components
        my_image = customtkinter.CTkImage(light_image=Image.open("data/defaultPicture.png"),
                                  dark_image=Image.open("data/defaultPicture.png"),
                                  size=(250, 250))
        
        self.detectedImage = customtkinter.CTkLabel(self.center_frame, image=my_image,width=250, height=250, text="", corner_radius=25)
        self.detectedImage.grid(row=4, column=10, padx=20, pady=(100, 10))
        
        self.labelSuggestions = customtkinter.CTkLabel(self.center_frame, text="Recomendaciones", font=customtkinter.CTkFont(family="Google Sans Regular", size=17))
        self.labelSuggestions.grid(row=5, column=10, padx=20, pady=(10,0))
        
        self.labelTextSugg = customtkinter.CTkTextbox(self.center_frame, width=450,fg_color="transparent")
        self.labelTextSugg.insert("0.0", """Para obtener mejores resultados es recomendable enfocar la enfermedad de la hoja en el centro de la imagen y usar una relación de aspecto 1:1.\n""")
        self.labelTextSugg.tag_config("justificado", justify='center', wrap='word')
        self.labelTextSugg.tag_add("justificado", "1.0", "end")
        self.labelTextSugg.grid(row=6, column=10)
        
        self.openDetection = customtkinter.CTkButton(self.center_frame, command=self.start_detection_command, width=120, text="Comenzar Detección Simple")
        self.openDetection.grid(row=6, column=10)



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def start_detection_command(self):
        
        simple_detection_window = simpleDetection()
        simple_detection_window.mainloop()
        self.destroy()
        

        
app = mainWindow()
app.mainloop()