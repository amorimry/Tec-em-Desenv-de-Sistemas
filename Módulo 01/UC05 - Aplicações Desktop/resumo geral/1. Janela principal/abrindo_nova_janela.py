import customtkinter as ctk

app = ctk.CTk()
app.title("Calculadora de IMC")
app.geometry("550x350")
app._set_appearance_mode('dark') # temas: light, dark, system

titulo = ctk.CTkLabel(app, text='Calcule seu IMC', font=('arial', 20, 'bold'), text_color= '#ffdcff')
titulo.pack()

# text_color escolhe a cor do texto

altura_titulo = ctk.CTkLabel(app, text='Altura', font=('comfortaa', 15, 'bold'), text_color='#ffb8ff')
altura_titulo.pack()

altura_entry = ctk.CTkEntry(app, placeholder_text='Digite sua altura...')
altura_entry.pack()

peso_titulo = ctk.CTkLabel(app, text='Peso', font=('comfortaa', 15, 'bold'), text_color='#ffb8ff')
peso_titulo.pack()

peso_entry = ctk.CTkEntry(app, placeholder_text='Digite seu peso...')
peso_entry.pack()

botao_calcular = ctk.CTkButton(app, text='Calcular')
botao_calcular.pack()


app.mainloop()