from ultralytics import YOLO
import customtkinter
import time, os
from tkinter import filedialog

model = YOLO('models/modelV3.pt')

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x230+550+175")
        self.title("IAgroscan | Batch Detection")
        self.wm_iconbitmap("data/imgs/Scanner.ico")

        self.label_deteccion = customtkinter.CTkLabel(self, text="Detección en Lote Exitosa!", font=customtkinter.CTkFont(family="Google Sans Medium", size=17))
        self.label_deteccion.pack(padx=20, pady=20)
        
        self.label_deteccion2 = customtkinter.CTkLabel(self, text="Detecciones Guardadas en: ", font=customtkinter.CTkFont(family="Google Sans Medium", size=15))
        self.label_deteccion2.pack(padx=20, pady=20)
        
        self.label_ruta = customtkinter.CTkLabel(self, text=rutaCarpeta, font=customtkinter.CTkFont(family="JetBrains Mono", size=12))
        self.label_ruta.pack(padx=20, pady=20)



def open_toplevel(self):
    if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        self.toplevel_window = ToplevelWindow(self)
    else:
        self.toplevel_window.focus()

def select_batch():
    
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
    open_toplevel()


select_batch()