
# ========================================================================== #
# ===================== Calculadora de Juros Compostos ===================== #
# =====================                                ===================== #
# =====================       Código feito por         ===================== #
# =====================   Donathan Ramalho Gonçalves   ===================== #
# =====================      26/06/2022 - Curitiba     ===================== #
# ========================================================================== #


# Importando as bibliotecas
import locale
import tkinter as tk
from tkinter import ttk


# Definir local da moeda
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


# Criando a aplicação gráfica com Tkinter
janela = tk.Tk()
janela.title('Calculadora Juros Compostos')
janela.geometry('650x550')


# ========================================================================== #
# ================================= PAGE 1 ================================= #


# ------------------------------------
# --------- Funções ------------------

# Função que verifica se todos os valores foram preenchidos
def verificarDadosPreenchidos():
    
    # Lista com todas as entradas de valores para facilitar verificação
    lCampos = [valorInicial, valorMensal, taxaJuros, periodo]
    
    # Verificando se algum dado está vazio
    preenchidos = 1
    for i in lCampos:
        if i.get() == '':
            preenchidos = 0
            
    # Se 1 então todos foram preenchidos, se 0 então há algum não preenchido
    if preenchidos == 1:
        # Verificar se os valores foram preenchidos corretamente e salva-los
        try:
            lDados = [float(valorInicial.get()), float(valorMensal.get()), 
                      float(taxaJuros.get())/100, int(periodo.get()), taxaEscolha.get(), tempoEscolha.get()]
            calcularDados(lDados)
        except:
            None
        
    # Aviso para preencher todos os dados
    else:
        aviso = tk.Label(janela, text="*Preencha todos os dados", font='Georgia 12', fg='red')
        aviso.place(x=230, y=460)
        aviso.after(2500, aviso.destroy)



# Transformar juros anual para juros mensal
def taxaAnualMes(anual):
    return ((1+anual)**(1/12)-1)



# Cálculo dos dados
def calcularDados(listaDados):
    
    # Inicializando montante(Valor Total Final) com o capital inicial
    montante = listaDados[0]
    
    # Todos os dados são calculados com a taxa e o período mensal
    # então transformamos quando são Anuais
    
    # Verificando se o período é Anual ou mensal
    tempo = listaDados[3]
    if listaDados[5] == 'Anual':
        tempo = tempo*12
    
    # Verificando se a taxa é Anual ou mensal
    taxa = listaDados[2]
    if listaDados[4] == 'Anual':
        taxa = taxaAnualMes(taxa)

    # Cálculo para encontrar o montante final
    for i in range(tempo):
        montante += montante*taxa
        montante += listaDados[1]

    # Pegando dados do total investido e o total de juros ganho
    investido = listaDados[1]*tempo
    rentabilidade = montante-investido



    # ---- Mostrando valores calculados na tela do usuário -------------
    
    # Valor calculado (Valor Total)
    valorTotal = tk.Label(janela, text=locale.currency(montante, grouping=True), font='Georgia 11', background='white', relief="solid")
    valorTotal.place(x=50, y=360, width=150, height=80)
    
    # Título (Valor Total)
    txt_valorTotal = tk.Label(janela, text="Valor Total", font='Georgia 11', background='white', relief="solid")
    txt_valorTotal.place(x=50, y=350, width=150)
    
    
    
    # Valor calculado (Valor Investido)
    valorInvestido = tk.Label(janela, text=locale.currency(investido, grouping=True), font='Georgia 11', background='white', relief="solid")
    valorInvestido.place(x=248, y=360, width=150, height=80)

    # Título (Valor Investido)
    txt_valorInvestido = tk.Label(janela, text="Valor Investido", font='Georgia 11', background='white', relief="solid")
    txt_valorInvestido.place(x=248, y=350, width=150)
    


    # Valor calculado (Valor dos Juros)
    valorJuros = tk.Label(janela, text=locale.currency(rentabilidade, grouping=True), font='Georgia 11', background='white', relief="solid")
    valorJuros.place(x=450, y=360, width=150, height=80)

    # Título (Valor Investido)
    txt_valorJuros = tk.Label(janela, text="Valor dos Juros", font='Georgia 11', background='white', relief="solid")
    txt_valorJuros.place(x=450, y=350, width=150)
    


# Limpar os dados de preenchimento
def limparDados():
    valorInicial.delete(0, tk.END)
    valorMensal.delete(0, tk.END)
    taxaJuros.delete(0, tk.END)
    periodo.delete(0, tk.END)



# --------------------------------------------
# --------- Tela de Cálculo ------------------

# Criando título principal
titulo = tk.Label(janela, text="Calculadora de Juros Compostos", font='Helvetica 13 bold')
titulo.place(x=30, y=20)



# Legenda das entradas de dados
txt_valorInicial = tk.Label(janela, text="Valor Inicial", font='Georgia 11')
txt_valorInicial.place(x=30, y=70)

txt_valorMensal = tk.Label(janela, text="Valor Mensal", font='Georgia 11')
txt_valorMensal.place(x=370, y=70)

txt_taxaJuros = tk.Label(janela, text="Taxa de Juros", font='Georgia 11')
txt_taxaJuros.place(x=30, y=170)

txt_tempo = tk.Label(janela, text="Tempo", font='Georgia 11')
txt_tempo.place(x=370, y=170)



# R$ e % ao lado da entrada de dados
text1 = tk.Label(janela, text="R$", font='Georgia 12', background='white', relief="solid", borderwidth=1)
text1.place(x=30, y=95, width=30, height=30)

text2 = tk.Label(janela, text="R$", font='Georgia 12', background='white', relief="solid", borderwidth=1)
text2.place(x=370, y=95, width=30, height=30)

text3 = tk.Label(janela, text="%", font='Georgia 12', background='white', relief="solid", borderwidth=1)
text3.place(x=30, y=195, width=30, height=30)



# Entradas dos dados
valorInicial = tk.Entry(janela, font='Calibre 12')
valorInicial.place(x=60, y=95, width=200, height=30)

valorMensal = tk.Entry(janela, font='Calibre 12')
valorMensal.place(x=400, y=95, width=200, height=30)

taxaJuros = tk.Entry(janela, font='Calibre 12')
taxaJuros.place(x=60, y=195, width=118, height=30)

periodo = tk.Entry(janela, font='Calibre 12')
periodo.place(x=370, y=195, width=148, height=30)



# Entrada do comboBox (lista de escolha)
taxaEscolha = ttk.Combobox(janela, values=['Mensal', 'Anual'], font='Georgia 11')
taxaEscolha.place(x=180, y=195, width=80, height=30)
taxaEscolha.current(1)

tempoEscolha = ttk.Combobox(janela, values=['Mensal', 'Anual'], font='Georgia 11')
tempoEscolha.place(x=520, y=195, width=80, height=30)
tempoEscolha.current(1)



# Botão para calcular os rendimentos
botaoCalcular = tk.Button(janela, text='Calcular', font='Georgia 13', background='#000BA8', fg='white', command=verificarDadosPreenchidos)
botaoCalcular.place(x=380, y=250, width=100, height=40)

# Botão para limpar os dados inseridos
botaoLimpar = tk.Button(janela, text='Limpar', font='Georgia 13', relief="ridge", command=limparDados, fg='#000BA8')
botaoLimpar.place(x=500, y=250, width=100, height=40)



# =============================== Main Loop ================================ #


janela.mainloop()





