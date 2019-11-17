import redeNeural2 as rn

# Classe para a auxiliar na manipulacão dos dinossauros
class Dinossauro(object):
    def __init__(self):
        self.cerebro = rn.Neural(5,10,3)
    
    def inicializarGeracao(self, TamanhoPopulacao):
        populacao = []

        for i in range(TamanhoPopulacao):
            populacao.append(self.cerebro())
        
        return populacao
