import numpy as np
import time
import matplotlib.pyplot as plt

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
    porcentagem_dentro = (pts_no_angulo_solido / qtde_sorteios) * 100
    porcentagem_fora = 100 - porcentagem_dentro

    rotulos = ['Dentro do ângulo sólido', 'Fora do ângulo sólido']
    porcentagens = [porcentagem_dentro, porcentagem_fora]

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    bars = ax.bar(rotulos, porcentagens, color=['red', 'blue'])
    ax.set_ylabel('Porcentagem')
    ax.set_title(f'sorteios: {qtde_sorteios}')
    ax.set_ylim(0, 100)

    for bar, percent in zip(bars, porcentagens):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{percent:.1f}%', ha='center', va='bottom')

    return ax