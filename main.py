import numpy as np
import time
import matplotlib.pyplot as plt
from metodos import *

inicio = time.time()
raio = 10
centro = np.array([0, 0, 0])

eixo_cone = np.array([0, 0, 1])

theta = np.pi / 4

sorteios = [10, 10**3, 10**6]
resultados = []
for i, qtde_sorteios in enumerate(sorteios):
    pts_no_angulo_solido = sortea_pontos(qtde_sorteios, raio, centro, eixo_cone, theta)
    resultados.append([pts_no_angulo_solido, qtde_sorteios])
    obter_resultados(pts_no_angulo_solido, qtde_sorteios)



fim =  time.time()

tempo_execucao = fim - inicio
print("Tempo: ", tempo_execucao)
print(resultados)

# print("Contador de pontos: ", pts_no_angulo_solido)
# fim =  time.time()

# porcentagem_dentro = (pts_no_angulo_solido / qtde_sorteios) * 100
# porcentagem_fora = 100 - porcentagem_dentro

# rotulos = ['Dentro do Ã¢ngulo sÃ³lido', 'Fora do Ã¢ngulo sÃ³lido']
# porcentagens = [porcentagem_dentro, porcentagem_fora]

# plt.bar(rotulos, porcentagens, color = ['red', 'blue'])
# plt.ylabel('Porcentagem')
# plt.title('Porcentagem de Pontos Dentro/Fora do ÃÂngulo SÃÂ³lido')
# plt.ylim(0, 100)

# plt.show()