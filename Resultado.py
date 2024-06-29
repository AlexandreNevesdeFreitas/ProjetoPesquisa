class Resultado:
    def __init__(self, sorteios=None, valor_angulo_solido=None, pts_no_angulo_solido=None):
        if sorteios is not None and valor_angulo_solido is not None and pts_no_angulo_solido is not None:
            self._qtde_sorteios = sorteios
            self._valor_angulo_solido = valor_angulo_solido
            self._pontos_no_angulo_solido = pts_no_angulo_solido
        else:
            self._qtde_sorteios = 0
            self._valor_angulo_solido = 0.0
            self._pontos_no_angulo_solido = []
    
    def get_qtde_sorteios(self):
        return self._qtde_sorteios

    def get_valor_angulo_solido(self):
        return self._valor_angulo_solido

    def get_pontos_no_angulo_solido(self):
        return self._pontos_no_angulo_solido

    def set_qtde_sorteios(self, sorteios):
        self._qtde_sorteios = sorteios

    def set_valor_angulo_solido(self, valor_angulo_solido):
        self._valor_angulo_solido = valor_angulo_solido

    def set_pontos_no_angulo_solido(self, pts_no_angulo_solido):
        self._pontos_no_angulo_solido = pts_no_angulo_solido
    
    def __str__(self):
        return f"Quantidade de sorteios: {self._qtde_sorteios}\n" \
            f"Pontos no ângulo sólido: {self._pontos_no_angulo_solido}\n" \
            f"Valor do ângulo sólido: {self._valor_angulo_solido}\n"