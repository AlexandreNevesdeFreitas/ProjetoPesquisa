from metodos import *
from metodos import update_plot
from Resultado import Resultado


raio = 10
centro = np.array([0, 0, 0])

eixo_cone = np.array([0, 0, 1])

theta = np.pi / 4
sorteios = [10**0, 10**1, 10**2, 10**3, 10**4, 2*10**4, 4*10**4, 6*10**4, 8*10**4, 10**5, 10**6]
# 10**7, 10**8]
# 20000, 40000, 600000, 80000 e 100000

resultados = []
arquivo = "resultados.txt"

inicio = time.time()
for i, qtde_sorteios in enumerate(sorteios):
    tempo_inicio = time.time()
    pts_no_angulo_solido = sorteia_pontos(qtde_sorteios, raio, centro, eixo_cone, theta)
    tempo_fim = time.time()

    valor = ((4 * np.pi) * pts_no_angulo_solido) / qtde_sorteios
    tempo_gasto = tempo_fim - tempo_inicio
    gerar_arquivo(sorteios[i], valor, tempo_gasto, arquivo)
    
    resultado = Resultado(qtde_sorteios, valor, pts_no_angulo_solido)
    resultados.append(resultado)

# fig, axs = plt.subplots(len(resultados), 1, figsize=(6,10))
fig, ax = plt.subplots(figsize=(6, 10))
current_plot = [0]
resultado = resultados[current_plot[0]]

obter_resultados(resultado.get_pontos_no_angulo_solido(), resultado.get_qtde_sorteios(), ax=ax)

fig.canvas.mpl_connect('key_press_event', lambda event: update_plot(event, resultados, fig, ax, current_plot))

plt.tight_layout()
plt.show()

for res in resultados:
    print(res)
valores = []
srt = []
pontos_no_angulo = []
for res in (resultados):
    valores.append(res.get_valor_angulo_solido())
    srt.append(res.get_qtde_sorteios())
    pontos_no_angulo.append(res.get_pontos_no_angulo_solido())
        
obter_tendencia_angulo_solido(valores, srt)
plt.show()