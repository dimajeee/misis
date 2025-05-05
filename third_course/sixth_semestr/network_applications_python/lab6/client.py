import tkinter as tk
from tkinter import ttk, messagebox, font
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

BASE_URL = "http://localhost:5000"

class FunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор функций")
        self.root.geometry("1000x800")
        
        self.big_font = font.nametofont("TkDefaultFont").copy()
        self.big_font.configure(size=12)
        
        self.bold_font = font.nametofont("TkDefaultFont").copy()
        self.bold_font.configure(size=12, weight="bold")
        
        self.button_font = font.nametofont("TkDefaultFont").copy()
        self.button_font.configure(size=14)
        
        self.create_widgets()
        
    def create_widgets(self):
        param_frame = ttk.LabelFrame(self.root, text="Параметры функции", padding=10)
        param_frame.pack(pady=15, padx=15, fill="x")
        
        ttk.Label(param_frame, text="Тип функции:", font=self.bold_font).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.func_type = tk.StringVar()
        func_combobox = ttk.Combobox(
            param_frame, 
            textvariable=self.func_type, 
            values=["sin", "quadratic", "rational"],
            font=self.big_font,
            height=25
        )
        func_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        func_combobox.current(0)
        
        ttk.Label(param_frame, text="a:", font=self.bold_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.a_var = tk.DoubleVar(value=1.0)
        ttk.Entry(param_frame, textvariable=self.a_var, font=self.big_font).grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        ttk.Label(param_frame, text="b:", font=self.bold_font).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.b_var = tk.DoubleVar(value=1.0)
        ttk.Entry(param_frame, textvariable=self.b_var, font=self.big_font).grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        ttk.Label(param_frame, text="c:", font=self.bold_font).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.c_var = tk.DoubleVar(value=0.0)
        ttk.Entry(param_frame, textvariable=self.c_var, font=self.big_font).grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        style = ttk.Style()
        style.configure("Big.TButton", font=self.button_font, padding=10)
        
        ttk.Button(
            button_frame, 
            text="Сгенерировать данные", 
            command=self.generate_data,
            style="Big.TButton"
        ).pack(side="left", padx=15)
        
        ttk.Button(
            button_frame, 
            text="Получить данные", 
            command=self.fetch_data,
            style="Big.TButton"
        ).pack(side="left", padx=15)
        
        self.text_output = tk.Text(
            self.root, 
            height=12,
            font=self.big_font,
            wrap=tk.WORD
        )
        self.text_output.pack(pady=15, padx=15, fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(self.text_output)
        scrollbar.pack(side="right", fill="y")
        self.text_output.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_output.yview)
        
        self.figure, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(pady=15, padx=15, fill="both", expand=True)
    
    def generate_data(self):
        try:
            params = {
                'func_type': self.func_type.get(),
                'a': self.a_var.get(),
                'b': self.b_var.get(),
                'c': self.c_var.get()
            }
            
            response = requests.get(f"{BASE_URL}/generate", params=params)
            result = response.json()
            
            if result.get('success'):
                messagebox.showinfo("Успех", f"Сгенерировано {result['count']} точек данных")
            else:
                messagebox.showerror("Ошибка", "Не удалось сгенерировать данные")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def fetch_data(self):
        try:
            response = requests.get(f"{BASE_URL}/get_data")
            data = response.json()
            
            if isinstance(data, list):
                self.text_output.delete(1.0, tk.END)
                for point in data[:50]:  
                    self.text_output.insert(tk.END, f"x: {point['x']:.2f}, y: {point['y']:.2f}\n")
                
                self.ax.clear()
                x_values = [point['x'] for point in data]
                y_values = [point['y'] for point in data]
                self.ax.scatter(x_values, y_values, s=5)
                self.ax.set_xlabel('X', fontsize=12)
                self.ax.set_ylabel('Y', fontsize=12)
                self.ax.set_title(f"График функции {self.func_type.get()}", fontsize=14)
                self.canvas.draw()
            else:
                messagebox.showerror("Ошибка", "Неверный формат данных")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionApp(root)
    root.mainloop()