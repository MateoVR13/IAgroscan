import customtkinter
from PIL import Image
from simpleDetection import simpleDetection
from tkinter import filedialog
from ultralytics import YOLO
import time, os


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x230+550+175")
        self.title("IAgroscan | Batch Detection")
        self.wm_iconbitmap("data/scanner.ico")

        self.label_deteccion = customtkinter.CTkLabel(self, text="Detección en Lote Exitosa!", font=customtkinter.CTkFont(family="Google Sans Medium", size=17))
        self.label_deteccion.pack(padx=20, pady=20)
        
        self.label_deteccion2 = customtkinter.CTkLabel(self, text="Detecciones Guardadas en: ", font=customtkinter.CTkFont(family="Google Sans Medium", size=15))
        self.label_deteccion2.pack(padx=20, pady=20)
        
        self.label_ruta = customtkinter.CTkLabel(self, text=rutaCarpeta, font=customtkinter.CTkFont(family="JetBrains Mono", size=12))
        self.label_ruta.pack(padx=20, pady=20)



class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
       
        self.geometry("800x700+550+175")
        self.title("IAgroscan | Menú Principal")
        self.wm_iconbitmap("data/scanner.ico")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        

        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1), weight=1)
        

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, padx=10, pady=10, rowspan=4, sticky="nswe")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        

        self.center_frame = customtkinter.CTkFrame(self, width=350, corner_radius=25)
        self.center_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=4, sticky="nswe")
        self.center_frame.grid_rowconfigure(20, weight=1)
        self.center_frame.grid_columnconfigure(10, weight=1)
        

        logo = customtkinter.CTkImage(
            light_image=Image.open("data/iagroscan_logo.png"),
            dark_image=Image.open("data/iagroscan_logo.png"),
            size=(200, 39),
        )
        self.labelImg = customtkinter.CTkLabel(self.sidebar_frame, image=logo, text="")
        self.labelImg.grid(row=1, column=0, padx=20, pady=(20, 10))


        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_image, text="Detección Simple",fg_color="gray25")
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_batch, text="Detección en Lote",fg_color="gray25")
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Informes",fg_color="gray25")
        # self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
        # self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Estadísticas",fg_color="gray25")
        # self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tamaño de la Interfaz:", anchor="w")
        self.scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event, fg_color="gray25")
        self.scaling_optionemenu.grid(row=15, column=0, padx=20, pady=(10, 20))
        

        my_image = customtkinter.CTkImage(light_image=Image.open("data/defaultPicture.png"),
                                  dark_image=Image.open("data/defaultPicture.png"),
                                  size=(250, 250))
        
        self.detectedImage = customtkinter.CTkLabel(self.center_frame, image=my_image,width=250, height=250, text="", corner_radius=25)
        self.detectedImage.grid(row=4, column=10, padx=20, pady=(100, 10))
        
        self.labelSuggestions = customtkinter.CTkLabel(self.center_frame, text="Recomendación", font=customtkinter.CTkFont(family="Google Sans Medium", size=17))
        self.labelSuggestions.grid(row=5, column=10, padx=20, pady=(10,0))
        
        self.labelTextSugg = customtkinter.CTkTextbox(self.center_frame, width=450,fg_color="transparent")
        self.labelTextSugg.insert("0.0", """Para obtener mejores resultados es recomendable enfocar la enfermedad de la hoja en el centro de la imagen y usar una relación de aspecto 1:1.\n""")
        self.labelTextSugg.tag_config("justificado", justify='center', wrap='word')
        self.labelTextSugg.tag_add("justificado", "1.0", "end")
        self.labelTextSugg.grid(row=6, column=10)
        
        self.openDetection = customtkinter.CTkButton(self.center_frame, command=self.select_image, width=120, text="Comenzar Detección Simple")
        self.openDetection.grid(row=6, column=10)

        self.toplevel_window = None


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
        
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()
        
    def select_image(self):
    
        file_path = filedialog.askopenfilename()
        
        model = YOLO('models/modelV2.pt')
        results = model(file_path)


        for result in results:
            result.show() 
            result.save(filename='result.jpg')
        

    def select_batch(self):
        folder_path = filedialog.askdirectory()
        
        model = YOLO('models/modelV3.pt')
        results = model(folder_path)

        for i, result in enumerate(results):

            timestamp = int(time.time() * 1000)
            result_filename = os.path.join(folder_path, f'result_{timestamp}_{i}.jpg')
            result.save(filename=result_filename)
            
        global rutaCarpeta
        rutaCarpeta = str(folder_path)    
        self.open_toplevel()

        # dialog = customtkinter.CTkInputDialog(text="Las imágenes se han guardado en la ruta:", title="Detección el Lote Exitosa!")

        
app = mainWindow()
app.mainloop()