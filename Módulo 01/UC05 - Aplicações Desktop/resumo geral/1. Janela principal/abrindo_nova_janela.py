import customtkinter as ctk
from tkinter import messagebox

# FUNÇÕES --------------------------------
def botao_calcular():
    altura = float(altura_entry.get())
    peso = float(peso_entry.get())
    imc = peso / (altura * altura)

    messagebox.showinfo('IMC calculado', f'Seu IMC é de {imc:.2f}')

# CÓDIGO --------------------------------
app = ctk.CTk()
app.title("Calculadora de IMC")
app.geometry("450x300")
app._set_appearance_mode('dark')

titulo = ctk.CTkLabel(app, text='Calcule seu IMC', font=('arial', 20, 'bold'),text_color= '#ffdcff')
titulo.grid(row=0, column=0, columnspan=2, pady=20)

altura_titulo = ctk.CTkLabel(app, text='Altura', font=('comfortaa', 15, 'bold'), text_color='#ffb8ff')
altura_titulo.grid(row=1, column=0, padx=20, sticky='w')

altura_entry = ctk.CTkEntry(app, placeholder_text='Digite sua altura...', width=300, height=30, corner_radius=5,border_width=1, border_color='#ff63ff', text_color='#ff00ff', placeholder_text_color='#ffdcff')
altura_entry.grid(row=1, column=1, pady=15)

peso_titulo = ctk.CTkLabel(app, text='Peso', font=('comfortaa', 15, 'bold'), text_color='#ffb8ff')
peso_titulo.grid(row=2, column=0, padx=20, sticky='w')

peso_entry = ctk.CTkEntry(app, placeholder_text='Digite seu peso...', width=300, height=30, corner_radius=5,border_width=1, border_color='#ff63ff', text_color='#ff00ff', placeholder_text_color='#ffdcff')
peso_entry.grid(row=2, column=1, pady=15)

botao_calcular = ctk.CTkButton(app, text='Calcular', fg_color='#990099', hover_color='#FF99FF', border_color='#330033', command=botao_calcular)
botao_calcular.grid(row=4, column=1, pady=15)


app.mainloop()