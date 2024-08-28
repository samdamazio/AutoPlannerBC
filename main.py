import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import os

def process_file(file_path, label_text):
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='latin1', delimiter=';', header=None, names=['Nome', 'Telefone'])
        else:
            raise ValueError("Formato de arquivo não suportado. Por favor, selecione um arquivo .xlsx ou .csv")
        
        df['Telefone'] = df['Telefone'].apply(lambda x: f"55{x}")
        df['Etiquetas'] = f"{label_text}, sem nome"
        
        new_df = df[['Telefone', 'Nome', 'Etiquetas']]
        
        output_folder = os.path.join(os.getcwd(), "PlanilhasProntas")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        file_name = os.path.basename(file_path).replace(".xlsx", "_BC.xlsx").replace(".csv", "_BC.xlsx")
        new_file_path = os.path.join(output_folder, file_name)
        
        new_df.to_excel(new_file_path, index=False)
        
        messagebox.showinfo("Sucesso", f"Nova planilha criada: {new_file_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo: {e}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
    if file_path:
        file_name = os.path.basename(file_path)  # Obter apenas o nome do arquivo
        file_label.config(text=file_name)  # Atualizar o label para mostrar o nome do arquivo
        execute_button.config(state=tk.NORMAL)
        execute_button.config(command=lambda: validate_and_process(file_path, label_entry.get()))
        update_background()  # Forçar atualização da imagem de fundo

def validate_and_process(file_path, label_text):
    if not label_text or label_text == "Nome":
        messagebox.showerror("Erro", "Por favor, insira um nome válido.")
        return
    process_file(file_path, label_text)

def clear_placeholder(event):
    if label_entry.get() == "Nome":
        label_entry.delete(0, tk.END)

def resize_background(event):
    update_background()

def update_background():
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    ratio_width = new_width / original_width
    ratio_height = new_height / original_height
    ratio = max(ratio_width, ratio_height)
    new_size = (int(original_width * ratio), int(original_height * ratio))
    resized_image = original_background_image.resize(new_size, Image.LANCZOS)
    new_background_photo = ImageTk.PhotoImage(resized_image)
    background_label.config(image=new_background_photo)
    background_label.image = new_background_photo
    background_label.place(relwidth=1, relheight=1)

# Configuração da janela principal
root = tk.Tk()
root.title("Processador de Planilhas")
root.geometry("750x600")
root.resizable(True, True)

# Adicionando imagem de fundo
background_image_path = "staticfiles/background.png"
original_background_image = Image.open(background_image_path)
original_width, original_height = original_background_image.size
background_photo = ImageTk.PhotoImage(original_background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Redimensionar a imagem de fundo com a janela
root.bind('<Configure>', resize_background)

# Centralizando os widgets
center_frame = tk.Frame(root, padx=20, pady=20)  
center_frame.place(relx=0.5, rely=0.5, anchor='center')

file_label = tk.Label(center_frame, text="Nenhum arquivo selecionado")
file_label.pack(pady=10)

select_button = tk.Button(center_frame, text="Procurar Arquivo", command=select_file)
select_button.pack(pady=5)

label_entry = tk.Entry(center_frame)
label_entry.insert(0, "Nome")
label_entry.bind("<FocusIn>", clear_placeholder)
label_entry.pack(pady=5)

execute_button = tk.Button(center_frame, text="Executar", state=tk.DISABLED)
execute_button.pack(pady=10)

# Executar a interface
root.mainloop()