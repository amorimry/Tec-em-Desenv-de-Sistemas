import customtkinter as ctk

def calcular_imc():
    altura = float(altura_entrada.get())
    peso = float(peso_entrada.get())
    imc = peso / (altura * altura)

    return imc

def mudar():
    mostrar_imc.configure(text=f"Seu IMC é de {calcular_imc():.2f}")

app = ctk.CTk()
app.title("Calculadora IMC")
app.geometry("400x350")

# Título
titulo = ctk.CTkLabel(app, text="Calcule seu IMC!", font=("Serif", 20
, "bold"))
titulo.pack(pady=(50, 10))

# Subtítulo peso
subtitulo1 = ctk.CTkLabel(app, text="Preencha seu PESO abiaxo.", font=("Arial", 15))
subtitulo1.pack()

# Entrada do peso
peso_entrada = ctk.CTkEntry(app, placeholder_text="digite seu peso")
peso_entrada.pack(pady=(5, 10))

# Subtítulo altura
subtitulo2 = ctk.CTkLabel(app, text="Preencha sua ALTURA abaixo.", font=("Arial", 15))
subtitulo2.pack()

# Entrada do altura
altura_entrada = ctk.CTkEntry(app, placeholder_text="digite sua altura")
altura_entrada.pack(pady=(5, 10))

# Botão calcular
botao_calcular = ctk.CTkButton(app, text="Calcular", command=mudar)
botao_calcular.pack(pady=(20, 0))

# Mostrar o imc
mostrar_imc = ctk.CTkLabel(app, text="", font=("Arial", 15, "bold") ,text_color="red")
mostrar_imc.pack(pady=(15, 0))

app.mainloop()