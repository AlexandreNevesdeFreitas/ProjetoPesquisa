import matplotlib.pyplot as plt
import pandas as pd



def ler_dados(arquivo):
    # Leitura do arquivo para um DataFrame do Pandas
    df = pd.read_csv(arquivo, delimiter='\s+', header=None, 
                     names=['Sorteios', 'Angulo_Solido', 'Erro', 'Tempo_Sorteio'])
    return df
    


def plotar_graficos(df):
    # Exemplo de plotagem, ajuste conforme necessário
    plt.figure(figsize=(18, 6))

    # Gráfico 1: Sorteios vs Angulo_Solido
    plt.subplot(1, 3, 1)
    plt.scatter(df['Sorteios'], df['Angulo_Solido'], c='blue', label='Angulo_Solido vs Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Angulo_Solido')
    plt.title('Relação entre Sorteios e Angulo_Solido')
    plt.legend()

    # Gráfico 2: Sorteios vs Erro
    plt.subplot(1, 3, 2)
    plt.scatter(df['Sorteios'], df['Erro'], c='red', label='Erro vs Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Erro')
    plt.title('Relação entre Sorteios e Erro')
    plt.legend()

    # Gráfico 3: Sorteios vs Tempo_Sorteio
    plt.subplot(1, 3, 3)
    plt.scatter(df['Sorteios'], df['Tempo_Sorteio'], c='green', label='Tempo_Sorteio vs Sorteios')
    plt.xlabel('Sorteios')
    plt.ylabel('Tempo_Sorteio')
    plt.title('Relação entre Sorteios e Tempo_Sorteio')
    plt.legend()

    plt.tight_layout()
    plt.show()


arquivo = "resultados.txt"

df = ler_dados(arquivo)
plotar_graficos(df)