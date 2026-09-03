import tkinter as tk
from tkinter import messagebox

# Funções da aplicação
def calcular_medias():
    try:
        # Recupera os dados das entradas de texto
        n1, n2, n3 = entry_nome1.get(), entry_nome2.get(), entry_nome3.get()
        v1, v2, v3 = float(entry_nota1.get()), float(entry_nota2.get()), float(entry_nota3.get())

        # Valida se os nomes foram preenchidos
        if not (n1 and n2 and n3):
            messagebox.showwarning("Aviso", "Preencha todos os nomes dos alunos!")
            return

        # Processamento dos dados
        alunos = [
            {"nome": n1, "nota": v1},
            {"nome": n2, "nota": v2},
            {"nome": n3, "nota": v3}
        ]

        media_geral = (v1 + v2 + v3) / 3

        # Formatação do resultado para exibição
        resultado_texto = "--- NOTAS CADASTRADAS ---\n"
        for aluno in alunos:
            resultado_texto += f"• {aluno['nome']}: {aluno['nota']:.1f}\n"
        
        resultado_texto += f"\nMédia Geral da Turma: {media_geral:.2f}"

        # Atualiza a interface com o resultado
        lbl_resultado.config(text=resultado_texto, fg="#1a5276")

    except ValueError:
        messagebox.showerror("Erro de Digitação", "Insira apenas números válidos nas notas!")

def limpar_campos():
    for entry in (entry_nome1, entry_nota1, entry_nome2, entry_nota2, entry_nome3, entry_nota3):
        entry.delete(0, tk.END)
    lbl_resultado.config(text="")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Notas de Alunos")
janela.geometry("420x450")
janela.configure(padx=20, pady=20)

# Título do Sistema
tk.Label(
    janela, 
    text="SISTEMA DE NOTAS DE ALUNOS", 
    font=("Arial", 14, "bold")
).pack(pady=(0, 15))

# Container para os campos de formulário
frame_form = tk.Frame(janela)
frame_form.pack(fill="x")

# Cabeçalhos das colunas
tk.Label(frame_form, text="Nome do Aluno", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(frame_form, text="Nota", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Aluno 1
entry_nome1 = tk.Entry(frame_form, width=25)
entry_nome1.grid(row=1, column=0, padx=5, pady=5)
entry_nota1 = tk.Entry(frame_form, width=8)
entry_nota1.grid(row=1, column=1, padx=5, pady=5)

# Aluno 2
entry_nome2 = tk.Entry(frame_form, width=25)
entry_nome2.grid(row=2, column=0, padx=5, pady=5)
entry_nota2 = tk.Entry(frame_form, width=8)
entry_nota2.grid(row=2, column=1, padx=5, pady=5)

# Aluno 3
entry_nome3 = tk.Entry(frame_form, width=25)
entry_nome3.grid(row=3, column=0, padx=5, pady=5)
entry_nota3 = tk.Entry(frame_form, width=8)
entry_nota3.grid(row=3, column=1, padx=5, pady=5)

# Painel de Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

btn_calcular = tk.Button(
    frame_botoes, 
    text="Calcular Média", 
    command=calcular_medias, 
    bg="#27ae60", 
    fg="white", 
    font=("Arial", 10, "bold"),
    padx=10
)
btn_calcular.pack(side="left", padx=5)

btn_limpar = tk.Button(
    frame_botoes, 
    text="Limpar", 
    command=limpar_campos, 
    bg="#e74c3c", 
    fg="white", 
    font=("Arial", 10),
    padx=10
)
btn_limpar.pack(side="left", padx=5)

# Área para exibição de Resultados
lbl_resultado = tk.Label(
    janela, 
    text="", 
    font=("Arial", 11), 
    justify="left", 
    anchor="w"
)
lbl_resultado.pack(fill="both", expand=True, pady=10)

janela.mainloop()