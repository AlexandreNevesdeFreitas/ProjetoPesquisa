import numpy as np
import time
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

getcontext().prec = 4

def esferico_para_cartesiano(raio, theta, phi):
    x = raio * np.sin(theta) * np.cos(phi)
    y = raio * np.sin(theta) * np.sin(phi)
    z = raio * np.cos(theta)
    return np.array([x, y, z])

def sortea_theta():
    return np.random.uniform(0, np.pi)

def sortea_phi():
    return np.random.uniform(0, 2 *np.pi)

def sortea_pontos(qtde_sorteios, raio, centro, eixo, theta):
    pts_no_angulo_solido = 0
    for i in range(qtde_sorteios):
        theta_sorteado = sortea_theta()
        phi_sorteado = sortea_phi()

        ponto = esferico_para_cartesiano(raio, theta_sorteado, phi_sorteado)

        vetor = ponto - centro
        comprimento_vetor = np.linalg.norm(vetor)

        projecao_vetor = np.dot(vetor, eixo)

        cos_angulo = projecao_vetor / comprimento_vetor
        cos_theta = np.cos(theta)

        if cos_angulo >= cos_theta:
            pts_no_angulo_solido += 1
    
    return pts_no_angulo_solido

def obter_resultados(pts_no_angulo_solido, qtde_sorteios, ax=None):    
    porcentagem_dentro = Decimal((pts_no_angulo_solido / qtde_sorteios) * 100)
    porcentagem_fora = Decimal(100 - porcentagem_dentro)

    rotulos = ['Dentro do Ã¢ngulo sÃ³lido', 'Fora do Ã¢ngulo sÃ³lido']
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
    plt.plot(sorteios, valores_angulo_solido, marker='o', linestyle='-', color='b', label='Valores do Ã¢ngulo sÃ³lido')

    plt.plot(sorteios, [pi] * len(sorteios), linestyle='--', color='r', label='Ï (3.14159...)')

    plt.title('TendÃªncia do Ãngulo SÃ³lido em RelaÃ§Ã£o a Ï')
    plt.xlabel('NÃºmero de Sorteios')
    plt.ylabel('Resultado (Ãngulo SÃ³lido)')
    plt.xticks(sorteios)
    plt.legend()
    plt.grid(True)


def gerar_arquivo(sorteios, angulo_solido, tempo_sorteio, arquivo):
    erro = angulo_solido - np.pi
    with open(arquivo, 'a') as f:
        f.write(f'{sorteios}        {angulo_solido}        {erro}          {tempo_sorteio}\n')