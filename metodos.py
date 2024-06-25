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

    rotulos = ['Dentro do ângulo sólido', 'Fora do ângulo sólido']
    porcentagens = [porcentagem_dentro, porcentagem_fora]

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
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

    plt.plot(sorteios, [pi] * len(sorteios), linestyle='--', color='r', label='π (3.14159...)')

    plt.title('Tendência do Ângulo Sólido em Relação a π')
    plt.xlabel('Número de Sorteios')
    plt.ylabel('Resultado (Ângulo Sólido)')
    plt.xticks(sorteios)
    plt.legend()
    plt.grid(True)
    # pi = np.pi
    # if ax is None:
    #     fig, ax = plt.subplots(figsize=(10, 6))
    # ax.plot(sorteios, valores_angulo_solido, marker='o', linestyle='-', color='b', label='Valores do ângulo sólido')

    # # Adicionando linha de tendência para pi
    # ax.plot(sorteios, [pi] * len(sorteios), linestyle='--', color='r', label='π (3.14159...)')

    # ax.set_title('Tendência do Ângulo Sólido em Relação a π')
    # ax.set_xlabel('Número de Sorteios')
    # ax.set_ylabel('Resultado (Ângulo Sólido)')
    # ax.set_xticks(sorteios)
    # ax.legend()
    # ax.grid(True)
    
    # ax.set_ylim(min(valores_angulo_solido) - 0.1, max(valores_angulo_solido) + 0.1)
