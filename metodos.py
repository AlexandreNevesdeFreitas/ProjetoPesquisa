import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

getcontext().prec = 4

def esferico_para_cartesiano(raio, theta, phi):
    x = raio * np.sin(theta) * np.cos(phi)
    y = raio * np.sin(theta) * np.sin(phi)
    z = raio * np.cos(theta)
    return np.array([x, y, z])

def sorteia_theta():
    return np.random.uniform(0, np.pi)

def sorteia_phi():
    return np.random.uniform(0, 2 *np.pi)

def sorteia_pontos(qtde_sorteios, raio, centro, eixo, theta):
    pts_no_angulo_solido = 0
    for i in range(qtde_sorteios):
        theta_sorteado = sorteia_theta()
        phi_sorteado = sorteia_phi()

        ponto = esferico_para_cartesiano(raio, theta_sorteado, phi_sorteado)

        vetor = ponto - centro
        comprimento_vetor = np.linalg.norm(vetor)

        projecao_vetor = np.dot(vetor, eixo)

        cos_angulo = projecao_vetor / comprimento_vetor
        cos_theta = np.cos(theta)

        if cos_angulo >= cos_theta:
            pts_no_angulo_solido += 1
        print(i)
    
    return pts_no_angulo_solido

def obter_resultados(pts_no_angulo_solido, qtde_sorteios, ax=None):    
    porcentagem_dentro = Decimal((pts_no_angulo_solido / qtde_sorteios) * 100)
    porcentagem_fora = Decimal(100 - porcentagem_dentro)

    rotulos = ['Dentro do ângulo sólido', 'Fora do Ã¢ngulo sólido']
    porcentagens = [porcentagem_dentro, porcentagem_fora]

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 10))
    bars = ax.bar(rotulos, porcentagens, color=['green', 'gray'])
    ax.set_ylabel('Porcentagem')
    ax.set_title(f'sorteios: {qtde_sorteios}')
    ax.set_ylim(0, 100)

    for bar, percent in zip(bars, porcentagens):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{percent:.4f}%', ha='center', va='bottom')

    return ax

def obter_tendencia_angulo_solido(valores_angulo_solido, sorteios, ax=None):
    pi = np.pi
    
    plt.figure(figsize=(10, 6))
    plt.plot(sorteios, valores_angulo_solido, marker='o', linestyle='-', color='b', label='Valores do ângulo sólido')

    plt.plot(sorteios, [pi] * len(sorteios), linestyle='--', color='r', label='Ï (3.14159...)')

    plt.title('Tendência do ângulo Sólido em relaçao a pi')
    plt.xlabel('Número de Sorteios')
    plt.ylabel('Resultado (ângulo sólido)')
    plt.xticks(sorteios)
    plt.legend()
    plt.grid(True)


def gerar_arquivo(sorteios, angulo_solido, tempo_sorteio, arquivo):
    erro = angulo_solido - np.pi
    with open(arquivo, 'a') as f:
        f.write(f'\n{sorteios}        {angulo_solido}        {erro}          {tempo_sorteio}\n')

def ler_dados(arquivo):
    # Leitura do arquivo para um DataFrame do Pandas
    df = pd.read_csv(arquivo, delimiter='\s+', header=None, 
                     names=['Sorteios', 'Angulo_Solido', 'Erro', 'Tempo_Sorteio'])
    return df
    

def plotar_graficos(df):
    # Exemplo de plotagem, ajuste conforme necessário
    plt.figure(figsize=(10, 6))

    # Exemplo de gráfico de dispersão (scatter plot)
    plt.scatter(df['Sorteios'], df['Angulo_Solido'], c='blue', label='Angulo_Solido vs Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Angulo_Solido')
    plt.title('Relação entre Sorteios e Angulo_Solido')
    plt.legend()

    # Exemplo de histograma
    plt.figure(figsize=(10, 6))
    plt.hist(df['Erro'], bins=20, edgecolor='black')
    plt.xlabel('Erro')
    plt.ylabel('Frequência')
    plt.title('Histograma do Erro')

    plt.show()
