import numpy as np
import time
import matplotlib.pyplot as plt
from metodos import *


raio = 10
centro = np.array([0, 0, 0])

eixo_cone = np.array([0, 0, 1])

theta = np.pi / 4
sorteios = [10**0, 10**1, 10**2, 10**3, 10**4, 10**5]
# , 10**6, 10**7, 10**8]
# 20000, 40000, 600000, 80000 e 100000

resultados = []
valores = []

arquivo = "resultados.txt"

inicio = time.time()
for i, qtde_sorteios in enumerate(sorteios):
    tempo_inicio = time.time()
    pts_no_angulo_solido = sorteia_pontos(qtde_sorteios, raio, centro, eixo_cone, theta)
    tempo_fim = time.time()

    valor = ((4 * np.pi) * pts_no_angulo_solido) / qtde_sorteios
    tempo_gasto = tempo_fim - tempo_inicio
    gerar_arquivo(sorteios[i], valor, tempo_gasto, arquivo)
     
    novo_resultado = {
        "Pontos no Ã¢ngulo sÃ³lido: ": pts_no_angulo_solido, 
        "Valor do Ã¢ngulo sÃ³lido": valor
    }
    resultados.append(novo_resultado)
    valores.append(valor)

fim =  time.time()


fig, axs = plt.subplots(len(resultados), 1, figsize=(6,10))

for i, resultado in enumerate(resultados):
    pts_no_angulo_solido = resultado["Pontos no Ã¢ngulo sÃ³lido: "]
    qtde_sorteios = sorteios[i]
    obter_resultados(pts_no_angulo_solido, qtde_sorteios, ax=axs[i])


print(resultados)
obter_tendencia_angulo_solido(valores, sorteios)

plt.tight_layout()
plt.show()

tempo_execucao = fim - inicio
print("Tempo: ", tempo_execucao)
print(resultados)