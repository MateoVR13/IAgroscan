import customtkinter
from PIL import Image
from tkinter import filedialog
from ultralytics import YOLO
import os, time

model = YOLO('models/modelV3.pt')

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x230+600+200")
        self.title("IAgroscan | Batch Detection")
        self.wm_iconbitmap("data/imgs/Scanner.ico")

        self.label_deteccion = customtkinter.CTkLabel(self, text="Detección en Lote Exitosa!", font=customtkinter.CTkFont(family="Google Sans Medium", size=17))
        self.label_deteccion.pack(padx=20, pady=20)
        
        self.label_deteccion2 = customtkinter.CTkLabel(self, text="Detecciones Guardadas en: ", font=customtkinter.CTkFont(family="Google Sans Medium", size=15))
        self.label_deteccion2.pack(padx=20, pady=20)
        
        self.label_ruta = customtkinter.CTkLabel(self, text=rutaCarpeta, font=customtkinter.CTkFont(family="JetBrains Mono", size=12))
        self.label_ruta.pack(padx=20, pady=20)
        
        self.attributes('-topmost', True)
        self.lift()

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x700+550+175")
        customtkinter.set_appearance_mode("light")
        self.title("IAgroscan | Menú Principal")
        self.wm_iconbitmap("data/imgs/Scanner.ico")
        self.after(0, lambda:self.state('zoomed'))

        customtkinter.set_default_color_theme("blue")
        
        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, fg_color="sea green", corner_radius=25)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nswe")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        
        self.center_frame = customtkinter.CTkFrame(self, width=350, corner_radius=25)
        self.center_frame.grid(row=0, column=1, padx=(0,10), pady=10, rowspan=4, sticky="nswe")
        self.center_frame.grid_rowconfigure(20, weight=1)
        self.center_frame.grid_columnconfigure(10, weight=1)
        
        logo = customtkinter.CTkImage(
            light_image=Image.open("data/imgs/Scanner2.png"),
            dark_image=Image.open("data/imgs/Scanner2.png"),
            size=(200, 200),
        )
        
        self.labelImg = customtkinter.CTkLabel(self.sidebar_frame, image=logo, text="")
        self.labelImg.grid(row=1, column=0, padx=20, pady=(20, 10))
        
        img = Image.open("data/icons/scannerw.png")
        img2 = Image.open("data/icons/scannerg.png")
        
        img3 = Image.open("data/icons/cellsw.png")
        img4 = Image.open("data/icons/cellsg.png")
        
        img5 = Image.open("data/icons/bar_chartw.png")
        img6 = Image.open("data/icons/bar_chartg.png")
        
        img7 = Image.open("data/icons/reportw.png")
        img8 = Image.open("data/icons/reportg.png")
        

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_image, 
                                                        text="Detección Simple", fg_color="transparent",
                                                        height=60, text_color="white",
                                                        corner_radius=15, anchor="w",
                                                        font=("Google Sans Medium", 18),
                                                        image= customtkinter.CTkImage(dark_image=img, light_image=img))
        

        def on_hover(event):
            self.sidebar_button_1.configure(text_color="sea green")
            self.sidebar_button_1.configure(fg_color="white")
            self.sidebar_button_1.configure(image= customtkinter.CTkImage(dark_image=img2, light_image=img2))
            
        def off_hover(event):
            self.sidebar_button_1.configure(text_color="white")
            self.sidebar_button_1.configure(fg_color="transparent")
            self.sidebar_button_1.configure(image= customtkinter.CTkImage(dark_image=img, light_image=img))
            

        self.sidebar_button_1.bind("<Enter>", on_hover)
        self.sidebar_button_1.bind("<Leave>", off_hover)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_batch,
                                                        text="Detección en Lote", fg_color="transparent",
                                                        height=60, text_color="white",
                                                        corner_radius=15, anchor="w",
                                                        font=("Google Sans Medium", 18),
                                                        image= customtkinter.CTkImage(dark_image=img, light_image=img))
        
        def on_hover(event):
            self.sidebar_button_2.configure(text_color="sea green")
            self.sidebar_button_2.configure(fg_color="white")
            self.sidebar_button_2.configure(image= customtkinter.CTkImage(dark_image=img2, light_image=img2))
            
        def off_hover(event):
            self.sidebar_button_2.configure(text_color="white")
            self.sidebar_button_2.configure(fg_color="transparent")
            self.sidebar_button_2.configure(image= customtkinter.CTkImage(dark_image=img, light_image=img))
            
        self.sidebar_button_2.bind("<Enter>", on_hover)
        self.sidebar_button_2.bind("<Leave>", off_hover)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_batch,
                                                        text="Registros", fg_color="transparent",
                                                        height=60, text_color="white",
                                                        corner_radius=15, anchor="w",
                                                        font=("Google Sans Medium", 18),
                                                        image= customtkinter.CTkImage(dark_image=img3, light_image=img3))
        
        def on_hover(event):
            self.sidebar_button_3.configure(text_color="sea green")
            self.sidebar_button_3.configure(fg_color="white")
            self.sidebar_button_3.configure(image= customtkinter.CTkImage(dark_image=img4, light_image=img4))
            
        def off_hover(event):
            self.sidebar_button_3.configure(text_color="white")
            self.sidebar_button_3.configure(fg_color="transparent")
            self.sidebar_button_3.configure(image= customtkinter.CTkImage(dark_image=img3, light_image=img3))
            
        self.sidebar_button_3.bind("<Enter>", on_hover)
        self.sidebar_button_3.bind("<Leave>", off_hover)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.select_batch,
                                                        text="Gráficos", fg_color="transparent",
                                                        height=60, text_color="white",
                                                        corner_radius=15, anchor="w",
                                                        font=("Google Sans Medium", 18),
                                                        image= customtkinter.CTkImage(dark_image=img5, light_image=img5))
        
        def on_hover(event):
            self.sidebar_button_4.configure(text_color="sea green")
            self.sidebar_button_4.configure(fg_color="white")
            self.sidebar_button_4.configure(image= customtkinter.CTkImage(dark_image=img6, light_image=img6))
            
        def off_hover(event):
            self.sidebar_button_4.configure(text_color="white")
            self.sidebar_button_4.configure(fg_color="transparent")
            self.sidebar_button_4.configure(image= customtkinter.CTkImage(dark_image=img5, light_image=img5))
            
        self.sidebar_button_4.bind("<Enter>", on_hover)
        self.sidebar_button_4.bind("<Leave>", off_hover)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()
        
    def select_image(self):
    
        file_path = filedialog.askopenfilename()
        
        model = YOLO('models/modelV3.pt')
        results = model(file_path)

        for result in results:
            result.show() 
            result.save(filename='result.jpg')
            
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

    def select_batch(self):
        
        folder_path = filedialog.askdirectory()
        results = model(folder_path)
        num_images_detected = len(results)
        print(f"Número de imágenes detectadas: {num_images_detected}")

        for i, result in enumerate(results):
            timestamp = int(time.time() * 1000)
            result_filename = os.path.join(folder_path, f'result_{timestamp}_{i}.jpg')
            result.save(filename=result_filename)
            
            for detection in result.boxes:
                class_id = int(detection.cls)
                
                if class_id == 0:
                    print("Clase 0 detectada: Acción correspondiente")
                elif class_id == 1:
                    print("Clase 1 detectada: Acción correspondiente")
                elif class_id == 2:
                    print("Clase 2 detectada: Acción correspondiente")
                elif class_id == 3:
                    print("Clase 3 detectada: Acción correspondiente")
                elif class_id == 4:
                    print("Clase 4 detectada: Acción correspondiente")
                elif class_id == 5:
                    print("Clase 5 detectada: Acción correspondiente")
                elif class_id == 6:
                    print("Clase 6 detectada: Acción correspondiente")
                elif class_id == 7:
                    print("Clase 7 detectada: Acción correspondiente")
                elif class_id == 8:
                    print("Clase 8 detectada: Acción correspondiente")
                elif class_id == 9:
                    print("Clase 9 detectada: Acción correspondiente")
                elif class_id == 10:
                    print("Clase 10 detectada: Acción correspondiente")
                else:
                    print(f"Clase desconocida detectada: {class_id}")
        
        global rutaCarpeta
        rutaCarpeta = str(folder_path)
        self.open_toplevel()

app = mainWindow()
app.mainloop()