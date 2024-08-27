import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def process_file(file_path, label_text):
    try:
        # Tentativa de leitura do arquivo com pandas
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='latin1', delimiter=';', header=None, names=['Nome', 'Telefone'])
        else:
            raise ValueError("Formato de arquivo não suportado. Por favor, selecione um arquivo .xlsx ou .csv")
        
        # Transformar os dados
        df['Telefone'] = df['Telefone'].apply(lambda x: f"55{x}")
        df['Etiquetas'] = f"{label_text}, sem nome"
        
        # Reorganizar as colunas
        new_df = df[['Telefone', 'Nome', 'Etiquetas']]
        
        # Definir o caminho para salvar a nova planilha
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
        file_label.config(text=file_path)
        execute_button.config(state=tk.NORMAL)
        execute_button.config(command=lambda: validate_and_process(file_path))

def validate_and_process(file_path):
    label_text = label_entry.get()
    if not label_text or label_text == "Nome":
        messagebox.showerror("Erro", "Por favor, insira um nome válido.")
        return
    process_file(file_path, label_text)

def clear_placeholder(event):
    if label_entry.get() == "Nome":
        label_entry.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Processador de Planilhas")

# Widgets
file_label = tk.Label(root, text="Nenhum arquivo selecionado")
file_label.pack()

select_button = tk.Button(root, text="Procurar Arquivo", command=select_file)
select_button.pack()

label_entry = tk.Entry(root)
label_entry.insert(0, "Nome")
label_entry.bind("<FocusIn>", clear_placeholder)
label_entry.pack()

execute_button = tk.Button(root, text="Executar", state=tk.DISABLED)
execute_button.pack()

# Executar a interface
root.mainloop()