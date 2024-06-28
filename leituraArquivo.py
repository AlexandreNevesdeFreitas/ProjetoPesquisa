import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def ler_dados(arquivo):
    df = pd.read_csv(arquivo, delimiter='\s+', header=None, 
                     names=['Sorteios', 'Angulo_Solido', 'Erro', 'Tempo_Sorteio'])
    return df
    


def plotar_graficos(df):
    plt.figure(figsize=(18, 6))

    # Gráfico 1: Sorteios vs Angulo_Solido
    plt.subplot(1, 3, 1)
    plt.scatter(df['Sorteios'], df['Angulo_Solido'], c='blue', label='Angulo_Solido x Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Angulo_Solido')
    plt.title('Relação entre Sorteios e Angulo_Solido')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='π')
    plt.legend()
    plt.ylim(-3, 6)


    # Gráfico 2: Sorteios vs Erro
    plt.subplot(1, 3, 2)
    plt.scatter(df['Sorteios'], df['Erro'], c='red', label='Erro x Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Erro')
    plt.title('Relação entre Sorteios e Erro')
    plt.legend()
    plt.ylim(-3, 3)

    # Gráfico 3: Sorteios vs Tempo_Sorteio
    plt.subplot(1, 3, 3)
    plt.scatter(df['Sorteios'], df['Tempo_Sorteio'], c='green', label='Tempo_Sorteio x Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Tempo_Sorteio')
    plt.title('Relação entre Sorteios e Tempo_Sorteio')
    plt.legend()
    max_sorteios = df['Sorteios'].max()
    max_tempo = df['Tempo_Sorteio'].max()
    plt.plot([0, max_sorteios], [0, max_tempo], linestyle='-', color='blue', label='Linearidade')
    

    plt.tight_layout()
    plt.show()


arquivo = "resultados.txt"

df = ler_dados(arquivo)
plotar_graficos(df)