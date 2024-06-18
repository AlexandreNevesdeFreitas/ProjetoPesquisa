import numpy as np
import time
import matplotlib.pyplot as plt
from metodos import *

inicio = time.time()
raio = 10
centro = np.array([0, 0, 0])

eixo_cone = np.array([0, 0, 1])

theta = np.pi / 4

pts_no_angulo_solido = sortea_pontos(1, raio, centro, eixo_cone, theta)

obter_resultados(pts_no_angulo_solido, 1)

pts_no_angulo_solido = sortea_pontos(10**3, raio, centro, eixo_cone, theta)
obter_resultados(pts_no_angulo_solido, 10**3)

pts_no_angulo_solido = sortea_pontos(10**6, raio, centro, eixo_cone, theta)
obter_resultados(pts_no_angulo_solido, 10**6)

fim =  time.time()

tempo_execucao = fim - inicio
print("Tempo: ", tempo_execucao)

# print("Contador de pontos: ", pts_no_angulo_solido)
# fim =  time.time()

# porcentagem_dentro = (pts_no_angulo_solido / qtde_sorteios) * 100
# porcentagem_fora = 100 - porcentagem_dentro

# rotulos = ['Dentro do ângulo sólido', 'Fora do ângulo sólido']
# porcentagens = [porcentagem_dentro, porcentagem_fora]

# plt.bar(rotulos, porcentagens, color = ['red', 'blue'])
# plt.ylabel('Porcentagem')
# plt.title('Porcentagem de Pontos Dentro/Fora do Ãngulo SÃ³lido')
# plt.ylim(0, 100)

# plt.show()